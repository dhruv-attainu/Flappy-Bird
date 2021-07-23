import os.path
import sys
import pygame
from util.colour import Colour
from util.constants import Constants
from Entities.bird import Bird
from Entities.background import Background
from Entities.ground import Ground
import pathlib
import os


def run():
    pygame.init()
    screen = pygame.display.set_mode((Constants.game_dimension))

    background = Background()
    bird = Bird()
    ground = Ground()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        background.display(screen)
        bird.display(screen)
        ground.display(screen)
        pygame.display.flip()


if __name__=='__main__':
    run()

