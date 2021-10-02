import pygame
import random
import math
from pygame import mixer

score = 0
pygame.init()
my_screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space invaders")
running = True
enemies_img = []
enemyx = []
enemyy = []
enemyy_change = []
enemyx_change = []
font2 = pygame.font.Font("freesansbold.ttf", 62)
font = pygame.font.Font("freesansbold.ttf", 32)

textx = 10
texty = 10
no_enemies = 6
for i in range(no_enemies):
    photo2 = pygame.image.load("space-invaders (1).png")
    enemies_img.append(photo2)
    enemy_x_list = random.randint(0, 736)
    enemyx.append(enemy_x_list)
    enemy_y_list = random.randint(10, 150)
    enemyy.append(enemy_y_list)
    enemyyc = 35
    enemyy_change.append(enemyyc)
    enemyxc = 4
    enemyx_change.append(enemyxc)
mixer.music.load("tenet.mp3")
mixer.music.play(-1)

icon = pygame.image.load("ufo.png")
photo = pygame.image.load("spaceship.png")
playerx = 370
playery = 480

pygame.display.set_icon(icon)
playerchange = 0
bg = pygame.image.load("red_blue.png")
bullet = pygame.image.load("bullet.png")
bullet_change = 8
bullet_y = 480
state = "ready"
ig = 0


def player(x, y):
    my_screen.blit(photo, (x, y))


def enemy(x, y, i):
    global enemies_img
    my_screen.blit(enemies_img[i], (x, y))


def fire_bullet(x, y):
    global state
    state = "fire"
    my_screen.blit(bullet, (x + 16, y + 10))


def is_colloid(enemyx, enemyy, bullet_x, bullet_y):
    distance = math.sqrt(
        (math.pow(enemyx - bullet_x, 2) + math.pow(enemyy - bullet_y, 2))
    )
    if distance <= 40:
        return True
    else:
        return False


bullet_x = 0
clock = pygame.time.Clock()
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerchange = -8
            if event.key == pygame.K_s:
                playerchange = 8
            if event.key == pygame.K_SPACE:
                if state == "ready":
                    LASER_SOUND = mixer.Sound("laser.mp3")
                    LASER_SOUND.play()
                    bullet_x = playerx
                    fire_bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerchange = 0
    my_screen.blit(bg, (0, 0))
    gma = False
    playerx += playerchange
    for i in range(no_enemies):
        if enemyy[i] > 243:
            gma = True
            for j in range(no_enemies):
                enemyy[j] = 2000
            quit_over = font2.render(f"GAME OVER!!!", True, (26, 238, 170))
            my_screen.blit(quit_over, (220, 200))
            mixer.music.stop()
            g_SOUND = mixer.Sound("game_over.wav")
            g_SOUND.play()
            state = "ready"
            playerchange = 0
            break

        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 4
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 736:
            enemyx_change[i] = -4
            enemyy[i] += enemyy_change[i]
        result = is_colloid(enemyx[i], enemyy[i], bullet_x, bullet_y)
        if result == True:
            e_SOUND = mixer.Sound("explosion.mp3")
            e_SOUND.play()
            enemyx[i] = random.randint(0, 736)
            enemyy[i] = random.randint(10, 150)
            state = "ready"
            score += 1
            bullet_x = playerx
            bullet_y = 480
        enemy(enemyx[i], enemyy[i], i)

    if playerx < 0:
        playerx = 0
    elif playerx > 736:
        playerx = 736
    # if bullet_y > 200:
    #     state = "ready"
    if bullet_y <= -30:
        bullet_y = 480
        state = "ready"

    if state is "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_change
    score_idx = font.render(f"Score: {score}", True, (26, 238, 170))
    my_screen.blit(score_idx, (textx, texty))
    player(playerx, playery)
    pygame.display.update()
