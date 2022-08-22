import pygame
from src.pygame_util import import_folder
from src.entity import Entity


class Enemy(Entity):
    def __init__(self, monster_name, pos, groups):

        # general setup
        super().__init__(groups)
        self.sprite_type = 'enemy'
        self.monster_name = monster_name

        # graphics setup
        self.import_graphics(monster_name)
        self.status = 'idle'
        self.frame_index = 0
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

    def import_graphics(self, name):
        self.animations = {'idle': [], 'move': [], 'attack': []}
        main_path = f'assets/graphics/monsters/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)
