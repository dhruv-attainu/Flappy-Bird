import os.path
import sys
import pygame
from util.colour import Colour
from util.constants import Constants
import pathlib
import os


def run():
    pygame.init()
    screen = pygame.display.set_mode((Constants.game_dimension))

    background = Background()
    bird = Bird()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        background.display(screen)
        bird.display(screen)
        pygame.display.flip()


if __name__=='__main__':
    run()

