import pygame

class Obstacle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load("assets/Dino_Cactus1.webp").convert_alpha()

    def update(self, speed):
        self.x -= speed

    def draw(self, screen):
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)



