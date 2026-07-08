import pygame
import random
from   consts    import *
from   obstacle  import Obstacle
from   character import Character
from   enum      import Enum, auto
from   ptero     import Ptero

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

def load_high_score():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read())
    except (FileNotFoundError, ValueError):
        return 0

def save_high_score(value):
    with open("highscore.txt", "w") as f:
        f.write(str(value))

high_score = load_high_score()
score = 0

#DINO
dino = Character(CHARACTER_X, CHARACTER_Y, CHARACTER_WIDTH, CHARACTER_HEIGHT)

#OBSTACLES
obstacle_group = pygame.sprite.Group()

cactus_speed = CACTUS_SPEED

class GameState(Enum):
    MENU = auto()
    PLAYING = auto()
    GAME_OVER = auto()

game_state= GameState.MENU

def reset():
    global  obstacle_group, cactus_speed, score, dino
    obstacle_group.empty()
    cactus_speed = CACTUS_SPEED
    score = 0
    dino.alive= True
    dino.ducking = False
    dino.jumping = False
    dino.velocity_y = 0

#3f3f3f
bg_x = 0
next_gap = 600
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
                if event.key == pygame.K_s and dino.jumping:
                    dino.fast_fall()
                if event.key == pygame.K_s and not dino.jumping:
                    dino.duck()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    dino.unduck()
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
        if bg_x <= -1280:
            bg_x = 0

    if game_state == GameState.PLAYING:
        text = font.render("Score: " + str(int(score)), True, (0, 0, 0))
        screen.blit(text, (20, 20))

        cactus_speed = min(cactus_speed + 0.005, MAX_SPEED)

        dino.draw(screen)

        if len(obstacle_group) == 0 or obstacle_group.sprites()[-1].rect.x < 1280 - next_gap:
            if random.random() < 0.5:
                obstacle_group.add(Obstacle(1280, random.choice(CACTUS_TYPES)))
            else:
                obstacle_group.add(Ptero(1280))
            next_gap = 400 + cactus_speed * 17 + random.randint(0, 250)

        obstacle_group.update(cactus_speed)
        obstacle_group.draw(screen)

        for obs in obstacle_group:
            if dino.get_rect().colliderect(obs.rect):
                dino.die()
                game_state = GameState.GAME_OVER
                if score > high_score:
                    high_score = int(score)
                    save_high_score(high_score)
            if obs.rect.right < 0:
                score += 1
                obs.kill()

        dino.update()

    if game_state == GameState.GAME_OVER:
        text = font.render("GAME OVER, PRESS R TO RESTART", True, (0, 0, 0))
        dino.draw(screen)
        screen.blit(text, (350,  305))

    if game_state == GameState.MENU:
        text = font.render("PRESS SPACE TO START", True, (0, 0, 0))
        screen.blit(text, (425, 305 ))
        high_sc = font.render("HIGH SCORE: " + str(high_score), True, (0, 0, 0))
        screen.blit(high_sc, (480, 260))

    pygame.display.flip()
    clock.tick(60)



