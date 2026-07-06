import pygame
from   consts import *

class Obstacle:
    def __init__(self, x, obs_type):
        self.x = x
        self.width = obs_type["width"]
        self.height = obs_type["height"]
        self.y = GROUND_Y
        self.image = pygame.image.load(obs_type["image"]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def update(self, speed):
        self.x -= speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
