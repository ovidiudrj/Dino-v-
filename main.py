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

dino = pygame.image.load("assets/dino.png").convert_alpha()
dino = pygame.transform.scale(dino, (135, 145))

pygame.mixer.music.load("sfx/collisionSound.wav")
font = pygame.font.Font("font/PressStart2P.ttf", 20)

cactus_x = 1280
cactus_speed = 7

score = 0
Game_over = False

GameState= "playing"

while running:
    if GameState == "playing":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not jumping:
                    velocity_y = -18
                    jumping = True

        cactus_x -= cactus_speed

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
        dino_rect = pygame.Rect(x, y, 135, 145)
        cactus = pygame.draw.rect(screen, (0, 0, 0), (cactus_x, 487, 50, 50))

        if dino_rect.colliderect(cactus):
            pygame.mixer.music.play()
            Game_over = True
            score = 0
            GameState = "game over"
            print("Game Over")
            cactus_x = 1280

        screen.blit(dino, (x, y))
        pygame.display.flip()
        clock.tick(60)

    if GameState == "game over":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    GameState = "playing"
        text = font.render("Game Over, press R to restart", True, (0, 0, 0))
        screen.blit(text, (380, 340 ))
        pygame.display.flip()
        clock.tick(60)


