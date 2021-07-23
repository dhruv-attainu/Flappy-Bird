import os
import pathlib
import pygame
from util.constants import Constants

class Bird:
    def __init__(self):
        current_path = pathlib.Path(__file__).parent.parent.absolute()
        path = os.path.join(current_path, "Assets", "Images", "bird.png")
        self.image = pygame.image.load(path)
        self.cnt = 0


    def display(self, screen):
        bird_rect = self.image.get_rect()
        bird_rect.center = Constants.width//2 + self.cnt, Constants.height//2
        self.cnt += 0.17  # making the bird move with the speed as declared
        screen.blit(self.image, bird_rect)
