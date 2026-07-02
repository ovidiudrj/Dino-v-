import pygame
import random
from   consts    import *
from   obstacle  import Obstacle
from   character import Character

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Dino(v)")
clock = pygame.time.Clock()
pygame.mixer.music.load("sfx/collisionSound.wav")
font = pygame.font.Font("font/PressStart2P.ttf", 20)

dino = Character(CHARACTER_X, CHARACTER_Y, CHARACTER_WIDTH, CHARACTER_HEIGHT)
dino_img = dino.load_image()

Obstacle_list = [Obstacle(1280, GROUND_Y + CHARACTER_HEIGHT - 62 , 50 , 50),
                 Obstacle(2000, GROUND_Y + CHARACTER_HEIGHT - 50, 40 , 40)]

score = 0
cactus_speed = CACTUS_SPEED
GameState= "menu"

def reset():
    global  Obstacle_list, cactus_speed, score
    Obstacle_list = [Obstacle(1280, GROUND_Y + CHARACTER_HEIGHT - 62 , 50 , 50),
                     Obstacle(2000, GROUND_Y + CHARACTER_HEIGHT - 50,  40 ,  40)]
    cactus_speed = CACTUS_SPEED
    score = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if GameState == "playing":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not dino.jumping:
                    dino.jump()
                if event.key == pygame.K_s:
                    dino.fast_fall()
        if GameState == "game over":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset()
                    GameState = "playing"
        if GameState == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    GameState = "playing"

    if GameState == "playing":
        text = font.render("Score: " + str(int(score)), True, (0, 0, 0))

        cactus_speed += 0.01

        screen.fill((255, 255, 255))
        screen.blit(text, (15, 15))

        screen.blit(dino_img, (dino.x, dino.y))

        for obs in Obstacle_list:
            obs.update(cactus_speed)

            if obs.x < 0:
                obs.x = 1280 + random.randint(0, 600)
                score += 1

            obs.draw(screen)

            if dino.get_rect().colliderect(obs.get_rect()):
                pygame.mixer.music.play()
                print("Game Over")
                GameState = "game over"

        dino.update()

    if GameState == "game over":
        text = font.render("Game Over, press R to restart", True, (0, 0, 0))
        screen.blit(text, (350,  220))

    if GameState == "menu":
        screen.fill((255, 255, 255))
        text = font.render("Press SPACE to start", True, (0, 0, 0))
        screen.blit(text, (425, 340 ))

    pygame.display.flip()
    clock.tick(60)



