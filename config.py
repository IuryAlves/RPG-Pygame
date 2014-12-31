# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from pygame.sprite import RenderUpdates

"""
	Module that contains the configuration of the game
"""

SCREEN_SIZE = (800, 600)
FPS = 16
NAME = "RPG"
DEFAULT_BACKGROUND = "imagens/cenario2.png"

def config():
	"""
	Commom configuration of a pygame project
	"""

	# initialize the pygame
    pygame.init()

    # configure the screen size
    c_screen = pygame.display.set_mode(SCREEN_SIZE)

    # configure the name of the game
    pygame.display.set_caption(NAME)

    # initialize the clock
    c_clock = pygame.time.Clock()
    c_clock.tick(FPS)

    # load the default background
    c_background = pygame.image.load(DEFAULT_BACKGROUND)
    
    # copy the background to the screen
    c_screen.blit(c_background, (0, 0))

    # initalize the font`s module
    pygame.font.init()

    return c_background, c_screen
