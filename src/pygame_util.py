from os import walk
import pygame


def import_folder(path):
    surface_list = []
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(surface)
    return surface_list


import_folder('../assets/graphics/grass')
