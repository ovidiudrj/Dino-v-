import pygame
import random
from   consts    import *
from   obstacle  import Obstacle
from   character import Character
from   enum      import Enum, auto

#WINDOW
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Dino(v)")
clock = pygame.time.Clock()

#FONT
font = pygame.font.Font(FONT_PATH, 20)

#BACKGROUND
background = pygame.image.load("assets/Dino_Background.png").convert_alpha()
background = pygame.transform.scale(background, (1280, 720))
background2 = background.copy()
score = 0

#DINO
dino = Character(CHARACTER_X, CHARACTER_Y, CHARACTER_WIDTH, CHARACTER_HEIGHT)

#OBSTACLES
obstacle_list = [Obstacle(1280, GROUND_Y + CHARACTER_HEIGHT - 100 , 60, 135),
                 Obstacle(2000, GROUND_Y + CHARACTER_HEIGHT - 108, 60 , 135)]

cactus_speed = CACTUS_SPEED

class GameState(Enum):
    MENU = auto()
    PLAYING = auto()
    GAME_OVER = auto()

game_state= GameState.MENU

def reset():
    global  obstacle_list, cactus_speed, score, dino
    obstacle_list = [Obstacle(1280, GROUND_Y + CHARACTER_HEIGHT - 100 , 60, 135),
                 Obstacle(2000, GROUND_Y + CHARACTER_HEIGHT - 108, 60 , 135)]
    cactus_speed = CACTUS_SPEED
    score = 0
    dino.alive= True

#3f3f3f
bg_x = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_state == GameState.PLAYING:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not dino.jumping:
                    dino.jump_sound.play()
                    dino.jump()
                if event.key == pygame.K_s:
                    dino.fast_fall()
        if game_state == GameState.GAME_OVER:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset()
                    game_state = GameState.PLAYING
        if game_state == GameState.MENU:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = GameState.PLAYING

    screen.blit(background, (bg_x, 0))
    screen.blit(background2, (bg_x + 1280, 0))

    if game_state != GameState.GAME_OVER:
        bg_x -= 0.3

    if game_state == GameState.PLAYING:
        text = font.render("Score: " + str(int(score)), True, (0, 0, 0))
        screen.blit(text, (20, 20))

        cactus_speed += 0.005

        dino.draw(screen)

        for obs in obstacle_list:
            obs.update(cactus_speed)

            if obs.x + obs.width < 0:
                max_right = max( o.x for o in obstacle_list)
                obs.x = max_right+ 200 + random.randint(0, 600) if max_right > 1280 else 1280
                score += 1

            obs.draw(screen)

            if dino.get_rect().colliderect(obs.get_rect()):
                dino.collision_sound.play()
                dino.alive = False
                game_state = GameState.GAME_OVER

        dino.update()

    if game_state == GameState.GAME_OVER:
        text = font.render("GAME OVER, PRESS R TO RESTART", True, (0, 0, 0))
        dino.draw(screen)
        screen.blit(text, (350,  305))

    if game_state == GameState.MENU:
        text = font.render("PRESS SPACE TO START", True, (0, 0, 0))
        screen.blit(text, (425, 305 ))

    pygame.display.flip()
    clock.tick(60)



