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

dino = pygame.image.load("dino.png").convert_alpha()
dino = pygame.transform.scale(dino, (135, 145))

pygame.mixer.music.load("collisionSound.wav")

cactus_x = 1280
cactus_speed = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                velocity_y = -17
                jumping = True

    cactus_x -= cactus_speed
    if cactus_x < 0 :
        cactus_x = 1280
    velocity_y += 0.8
    y += velocity_y
    if y > 400 :
        y = 400
        jumping = False
    if cactus_x - 50 == x + 135 and y == 400:
        pygame.mixer.music.play()
        print("Faaahh")
    screen.fill((255, 255, 255))
    cactus = pygame.draw.rect(screen , (0 , 0 , 0), ( cactus_x , 487, 50 ,50))
    screen.blit(dino, (x, y))
    pygame.display.flip()
    clock.tick(60)


