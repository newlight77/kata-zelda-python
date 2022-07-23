import pygame
from src.pygame_util import import_folder

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, groups, obstacle_sprites):
		super().__init__(groups)
		self.image = pygame.image.load('assets/graphics/test/player.png').convert_alpha()
		self.rect = self.image.get_rect(topleft=pos)
		self.hitbox = self.rect.inflate(0, -26)

		# graphics setup
		self.import_assets()

		# movement
		self.direction = pygame.math.Vector2(0, 0)
		self.speed = 5
		self.attacking = False
		self.attack_time = None
		self.attack_cooldown = 400

		self.obstacle_sprites = obstacle_sprites
	
	def import_assets(self):
		character_path = 'assets/graphics/player'
		self.animations = {
			'up': [], 'down': [], 'left': [], 'right': [],
			'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': [],
			'up_attack': [], 'down_attack': [], 'left_attack': [], 'right_attack': [],
		}

		for animation in self.animations.keys():
			full_path = character_path + '/' + animation
			self.animations[animation] = import_folder(full_path)
		print(self.animations)

	def input(self):
		keys = pygame.key.get_pressed()

		# movement input
		if keys[pygame.K_LEFT]:
			self.direction.x = -1
		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
		if keys[pygame.K_UP]:
			self.direction.y = -1
		if keys[pygame.K_DOWN]:
			self.direction.y = 1

		# attack input
		if keys[pygame.K_SPACE] and not self.attacking:
			self.attacking = True
			self.attack_time = pygame.time.get_ticks()
			print('attack')

		# magic input
		if keys[pygame.K_LCTRL] and not self.attacking:
			self.attacking = True
			self.attack_time = pygame.time.get_ticks()
			print('magic')

	def cooldown(self):
		current_time = pygame.time.get_ticks()
		if self.attacking:
			if current_time - self.attack_time >= self.attack_cooldown:
				self.attacking = False

	def move(self, speed):
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.hitbox.x += self.direction.x * speed
		self.collision('horizontal')
		self.hitbox.y += self.direction.y * speed
		self.collision('vertical')
		self.rect.center = self.hitbox.center

	def collision(self,direction):
		if direction == 'horizontal':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.x > 0: # moving right
						self.hitbox.right = sprite.hitbox.left
					if self.direction.x < 0: # moving left
						self.hitbox.left = sprite.hitbox.right

		if direction == 'vertical':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.y > 0: # moving down
						self.hitbox.bottom = sprite.hitbox.top
					if self.direction.y < 0: # moving up
						self.hitbox.top = sprite.hitbox.bottom

	def update(self):
		self.input()
		self.move(self.speed)
		self.cooldown()
