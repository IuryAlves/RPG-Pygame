# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from pygame.sprite import RenderUpdates

#
# Module that contains the configuration of the game
#


def config():
    pygame.init()
    SCREEN_SIZE = (800, 600)
    NAME = "RPG"
    c_screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(NAME)
    c_clock = pygame.time.Clock()
    c_background = pygame.image.load("imagens/cenario2.png")
    c_screen.blit(c_background, (0, 0))
    return c_background, c_screen, c_clock
