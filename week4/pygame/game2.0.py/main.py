import pygame

screen = pygame.display.set_mode((900, 500))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
