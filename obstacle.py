import pygame
from   consts import *

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, obs_type):
        super().__init__()
        self.width = obs_type["width"]
        self.height = obs_type["height"]
        self.image = pygame.image.load(obs_type["image"]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(x, GROUND_Y))

    def update(self, speed):
        self.rect.x -= speed

