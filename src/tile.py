from config.settings import TILESIZE, HITBOX_OFFSET
import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        y_offset = HITBOX_OFFSET[sprite_type]
        self.image = surface
        if (sprite_type == 'object'):
            adjusted_pos = (pos[0], pos[1] - TILESIZE)
            self.rect = self.image.get_rect(topleft=adjusted_pos)
        else:
            self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, y_offset)
