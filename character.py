import pygame
from consts import *

class Character:
    def __init__(self, x , y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity_y = 0
        self.jumping = False

    def jump(self):
        if self.jumping: return

        self.jumping = True
        self.velocity_y = - 18

    def update(self):
        self.velocity_y += GRAVITY
        self.y += self.velocity_y

        if self.y > GROUND_Y:
            self.jumping = False
            self.y = CHARACTER_Y
            self.velocity_y = 0

    def get_rect(self):
        return pygame.Rect(self.x + 30, self.y + 20, self.width - 60, self.height - 30)

    def fast_fall(self):
        self.velocity_y += 12

    def load_image(self):
        img = pygame.image.load("assets/dino_no_bg.png").convert_alpha()
        img=  pygame.transform.scale(img, (135, 145))
        return img

