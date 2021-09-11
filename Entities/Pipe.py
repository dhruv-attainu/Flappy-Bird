import os
import pathlib
import random

from util.Constants import Constants
import pygame


class Pipe:
    def __init__(self):
        current_path = pathlib.Path(__file__).parent.parent.absolute()
        path = os.path.join(current_path, "assets", "images", "pipe.png")
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.pipes = list()

    def spawn_pipe(self):
        rect_bottom = self.image.get_rect()
        dy = random.randint(10, 200)
        rect_bottom.midbottom = (Constants.width + Pipe.width, Constants.height + Pipe.height // 2 + dy)

        rect_top = self.image.get_rect()
        rect_top.midtop = (Constants.width + Pipe.width, -Pipe.height // 2 + dy)

        self.pipes.append(rect_bottom)
        self.pipes.append(rect_top)
        return rect_bottom

    def move_pipe(self):
        for pipe in self.pipes:
            pipe.centerx += 2

    def display(self, screen):
        screen.blit(self.image, self.rect)
