# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from pygame.sprite import RenderUpdates


'''
Módulo de configurações do jogo

'''


def config():
    pygame.init()  # inicializa o pygame
    TAMANHO_TELA = (800, 600)
    NOME = "RPG" # Define o nome que vai aparecer na janela
    c_tela = pygame.display.set_mode(TAMANHO_TELA)  # Configura a tela
    pygame.display.set_caption(NOME)
    c_clock = pygame.time.Clock()
    c_fundo = pygame.image.load("imagens/cenario2.png") # define a imagem de fundo
    c_tela.blit(c_fundo, (0, 0)) # copia a imagem de fundo para  o jogo
    return c_fundo, c_tela, c_clock
