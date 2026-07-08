from obstacle import Obstacle
import pygame
import random

class Ptero (Obstacle):
    def __init__(self, x ):
        super().__init__( x, {"image": "assets/Dino_Ptero1.png", "width": 170, "height": 100})
        self.rect.y = random.choice([270, 325])
        img2 = pygame.image.load("assets/Dino_Ptero2.png").convert_alpha()
        img2 = pygame.transform.scale(img2, (170, 100))
        self.frames = [self.image, img2]
        self.timer = 0
        self.current = 0

    def update(self, speed):
        super().update(speed)
        self.timer += 1
        if self.timer >= 12:
            self.timer = 0
            self.current = 1 - self.current
            self.image = self.frames[self.current]