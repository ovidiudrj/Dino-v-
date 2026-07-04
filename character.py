import pygame
from   consts import *

class Character:
    def __init__(self, x , y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity_y = 0
        self.jumping = False
        self.alive = True

        self.run_image1= self.load_image("assets/Dino_Run1.png")
        self.run_image2= self.load_image("assets/Dino_Run2.png")
        self.dead_image = self.load_image("assets/Dino_Dead.png")

        self.jump_sound = pygame.mixer.Sound(JUMP_SOUND_PATH)
        self.collision_sound = pygame.mixer.Sound(COLLISION_SOUND_PATH)

        self.run_frames = [self.run_image1, self.run_image2]
        self.current_frame = 0
        self.timer = 0

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

    def load_image(self, path):
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(img, (120, 130))

    def draw(self, screen):
        if not self.alive:
            screen.blit(self.dead_image, (self.x, self.y))
            return
        if self.jumping:
            screen.blit(self.run_frames[0], (self.x, self.y))
            return

        self.timer += 1
        if self.timer >= 6:
            self.timer = 0
            self.current_frame = 1 - self.current_frame
        screen.blit(self.run_frames[self.current_frame], (self.x, self.y))





