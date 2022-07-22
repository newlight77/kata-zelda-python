from src.csv_util import import_csv_layout
from src.pygame_util import import_folder
import pygame 
from config.settings import TILESIZE
from src.debug import debug
from src.tile import Tile
from src.player import Player
from random import choice

class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

	def create_map(self):
		layouts = {
			'boundary': import_csv_layout('assets/map/map_FloorBlocks.csv'),
			'grass': import_csv_layout('assets/map/map_Grass.csv'),
			'object': import_csv_layout('assets/map/map_Objects.csv'),
		}

		graphics = {
			'grass': import_folder('assets/graphics/grass'),
			'object': import_folder('assets/graphics/objects'),
        }

		for style, layout in layouts.items():
			for row_index,row in enumerate(layout):
				for col_index, col in enumerate(row):
					if (col != '-1'):
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if (style == 'boundary'):
							Tile((x,y), [self.obstacle_sprites], 'invisible')
						if (style == 'grass'):
							random_grass_image = choice(graphics['grass'])
							Tile((x,y), [self.visible_sprites,self.obstacle_sprites],'grass',random_grass_image)
						if (style == 'object'):
							large_object = graphics['object'][int(col)]
							Tile((x,y), [self.visible_sprites,self.obstacle_sprites],'object',large_object)

		self.player =  Player((2000,1430),[self.visible_sprites],self.obstacle_sprites)

	def run(self):
		# update and draw the game
		# self.visible_sprites.draw(self.display_surface)
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()
		debug(self.player.direction)


class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		# general setup 
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

		# creating the floor
		self.floor_surf = pygame.image.load('assets/graphics/tilemap/ground.png').convert()
		self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

	def custom_draw(self,player):

		# getting the offset 
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		# drawing the floor
		floor_offset_pos = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_surf, floor_offset_pos)

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)
