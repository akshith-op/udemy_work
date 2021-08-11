import pygame
import random
import math

score = 0
pygame.init()
my_screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space invaders")
running = True
enemies_img = []
enemyx = []
enemyy = []
no_enemies = 6
for i in range(no_enemies):
    photo2 = pygame.image.load("space-invaders (1).png")
    enemies_img.append(photo2)
    enemy_x_list = random.randint(0, 736)
    enemyx.append(enemy_x_list)
    enemy_y_list = random.randint(10, 150)
    enemyy.append(enemy_y_list)
    print(enemyx)
    print(enemyy)

icon = pygame.image.load("ufo.png")
photo = pygame.image.load("spaceship.png")
playerx = 370
playery = 480
enemyx_change = 0.3
enemyy_change = 40

pygame.display.set_icon(icon)
playerchange = 0
bg = pygame.image.load("bg.jpg")
bullet = pygame.image.load("bullet.png")
bullet_change = 8
bullet_y = 480
state = "ready"
ig = 0


def player(x, y):
    my_screen.blit(photo, (x, y))


def enemy(x, y, i):
    my_screen.blit(enemies_img[i], (x, y))


def fire_bullet(x, y):
    global state
    state = "fire"
    my_screen.blit(bullet, (x + 16, y + 10))


def is_colloid(enemyx, enemyy, bullet_x, bullet_y):
    distance = math.sqrt(
        (math.pow(enemyx - bullet_x, 2) + math.pow(enemyy - bullet_y, 2))
    )
    if distance <= 64:
        return True
    else:
        return False


bullet_x = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerchange = -7
            if event.key == pygame.K_s:
                playerchange = 7
            if event.key == pygame.K_SPACE:
                if state == "ready":
                    bullet_x = playerx
                    fire_bullet(bullet_x, bullet_y)
                # bullet_y += bullet_change
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerchange = 0
    my_screen.blit(bg, (0, 0))

    playerx += playerchange

    for idxgg in range(no_enemies):
        enemyx[i] += enemyx_change
        if enemyx[i] <= 0:
            enemyx_change = 0.3
            enemyy[i] += enemyy_change
        elif enemyx[i] >= 736:
            enemyx_change = -0.3
            enemyy[i] += enemyy_change
        result = is_colloid(enemyx[i], enemyy[i], bullet_x, bullet_y)
        if result == True:
            enemyx[i] = random.randint(0, 736)
            enemyy[i] = random.randint(10, 150)
            state = "ready"
            score += 1
            print(score)
            bullet_x = playerx
            bullet_y = 480

        enemy(enemyx[i], enemyy[i], i)

    if playerx < 0:
        playerx = 0
    elif playerx > 736:
        playerx = 736

    if bullet_y <= 0:
        bullet_y = 480
        state = "ready"

    if state is "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_change
    player(playerx, playery)
    pygame.display.update()
