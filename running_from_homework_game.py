from cmath import rect

import pygame
import sys

pygame.init()

WIDTH = 1914
HEIGHT = 1104

s = 250
a = s
spood = 30
spood_mouse = 25
backround_color = ((0,0,1))

enemy_size = 52
enemy_pos = [100, 0]
enemy_spood = 20
enemy_pos2 = [100, 50]

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
good_guy_image = pygame.image.load('amio.png')
good_guy_image = pygame.transform.scale(good_guy_image, (s,s))
#good_guy_image = pygame.transform.flip(good_guy_image, True, True)

enemy = pygame.image.load('homework.png')
enemy = pygame.transform.scale(enemy, (s,s))

game_over = False

x = WIDTH//2 - s//2
y = HEIGHT//2 - a//2

direction_moving = ''

mouse_tracking = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                #y -= spood
                direction_moving = 'up'
            elif event.key == pygame.K_DOWN:
                #y += spood
                direction_moving = 'down'
            elif event.key == pygame.K_LEFT:
                #x -= spood
                direction_moving = 'left'
            elif event.key == pygame.K_RIGHT:
                #x += spood
                direction_moving = 'right'
        elif event.type == pygame.KEYUP:
            direction_moving = ''
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_tracking = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_tracking = False

    if mouse_tracking:
            mx, my = pygame.mouse.get_pos()
            #print(event)
            if x < mx:
                x += spood_mouse
            if x > mx:
                x -= spood_mouse
            if y < my:
                y += spood_mouse
            if y > my:
                y -= spood_mouse

    if direction_moving == 'up':
        y -= spood
    elif direction_moving == 'down':
        y += spood
    elif direction_moving == 'left':
        x -= spood
    elif direction_moving == 'right':
        x += spood

    if x > WIDTH:
        x = 0
    if x < 0:
        x = WIDTH
    if y > HEIGHT:
        y = 0
    if y < 0:
        y = HEIGHT

    if enemy_pos[0] < x:
        enemy_pos[0] += enemy_spood
    if enemy_pos[0] > x:
        enemy_pos[0] -= enemy_spood
    if enemy_pos[1] < y:
        enemy_pos[1] += enemy_spood
    if enemy_pos[1] > y:
        enemy_pos[1] -= enemy_spood

    screen.fill(backround_color)
    screen.blit(good_guy_image, (x-s/2, y-s/2))
    screen.blit(enemy, (enemy_pos[0]-s/2, enemy_pos[1]-a/2))
    #enemy = pygame.draw.rect(screen, (0, 0, 255), (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

    #pygame.draw.rect(screen, (255, 0, 0), (enemy_pos2[0], enemy_pos2[1], enemy_size, enemy_size))

    clock.tick(12)
    pygame.display.flip()