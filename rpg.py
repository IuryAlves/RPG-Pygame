# -*- coding: utf-8 -*-

from config import config
from Classes import *
from colors import *
import sys
from pygame.sprite import Sprite, RenderUpdates


# mover personagem para baixo


#=======================


# obs 27 == 'esc' 
keys = {
    K_LEFT: False, K_RIGHT: False, K_UP: False, 
    K_DOWN: False, K_RETURN: False, 27: False
    }  

def main():
    fundo, tela = config()
    musica = pygame.mixer.Sound("BGM/Firelink Shrine.wav")
    grupo = RenderUpdates()
    personagem = Hero(20, 290, "dante", grupo)
    frase = Text(40, 'Quem eh voce e oque faz aqui?', 'carolingia.ttf')

    lx = [b for b in range(-4, 76)]
    l1 = [-10]
    l2 = [6]

    parede = [x for x in range(-10, 16)]

    iniciarConversa = [43, 0]


    musica.play()
    fundo = fundo.convert()
    pygame.display.flip()
    while True:

        for e in pygame.event.get([KEYUP, KEYDOWN]):
            valor = (e.type == KEYDOWN)
            if e.key in keys.keys():
                keys[e.key] = valor

        if keys[27]:  # tecla ESC
            pygame.quit()
            sys.exit()

        if keys[K_LEFT]:
            personagem.move("LEFT")
        if keys[K_RIGHT]:
            personagem.move("RIGHT")
        if keys[K_UP]:
            personagem.move("UP")
        if keys[K_DOWN]:
            personagem.move("DOWN")

        if personagem.px == iniciarConversa[0] and personagem.py == iniciarConversa[1]:
            tela.blit(frase.frases, (200, 500))
            pygame.display.flip()

        #print(personagem.px, personagem.py)

        grupo.clear(tela, fundo)
        pygame.display.update(grupo.draw(tela))


if __name__ == '__main__':
    main()
