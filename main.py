import pygame
pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Dino(v)")
clock = pygame.time.Clock()
running = True

x= 100
y= 600
velocity_y = 0

jumping = False

dino = pygame.image.load("assets/dino_no_bg.png").convert_alpha()
dino = pygame.transform.scale(dino, (135, 145))

pygame.mixer.music.load("sfx/collisionSound.wav")
font = pygame.font.Font("font/PressStart2P.ttf", 20)

cactus_x = 1280
cactus_speed = 7

score = 0

GameState= "menu"

def reset():
    global cactus_x, cactus_speed, score
    cactus_x = 1280
    cactus_speed = 7
    score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if GameState == "playing":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not jumping:
                    velocity_y = -18
                    jumping = True
                if event.key == pygame.K_s:
                    velocity_y += 12
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
        cactus_x -= cactus_speed
        cactus_speed += 0.01
        text = font.render("Score: " + str(int(score)), True, (0, 0, 0))

        if cactus_x < 0:
            cactus_x = 1280
            score += 1

        velocity_y += 0.8
        y += velocity_y

        if y > 400:
            jumping = False
            y = 400

        screen.fill((255, 255, 255))
        screen.blit(text, (15, 15))
        dino_rect = pygame.Rect(x + 30, y + 20, 135 - 60, 145 - 30)
        cactus = pygame.draw.rect(screen, (0, 0, 0), (cactus_x, 487, 50, 50))

        if dino_rect.colliderect(cactus):
            pygame.mixer.music.play()
            print("Game Over")
            GameState = "game over"

        screen.blit(dino, (x, y))

    if GameState == "game over":
        text = font.render("Game Over, press R to restart", True, (0, 0, 0))
        screen.blit(text, (350,  220))

    if GameState == "menu":
        screen.fill((255, 255, 255))
        text = font.render("Press SPACE to start", True, (0, 0, 0))
        screen.blit(text, (425, 340 ))

    pygame.display.flip()
    clock.tick(60)



