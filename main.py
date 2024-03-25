import random

import os
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

FPS = pygame.time.Clock()

HEIGHT = 800
WIDTH = 1200


FONT = pygame.font.SysFont('Verdana', 20)

COLOR_WHITE = (255, 255,255)
COLOR_RED = (255,0,0)
COLOR_BLUE = (0,0,255)
COLOR_YELLOW = (255,255,0)
COLOR_GREEN = (0,255,0)
COLOR_BLACK = (0, 0, 0)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.transform.scale(pygame.image.load('background.png'), (WIDTH,HEIGHT))
bg_x1 = 0
bg_x2 = bg.get_width()
bg_move = 3

IMAGE_PATH = "Goose"
PLAYER_IMAGES = os.listdir(IMAGE_PATH)

player_size = (50,50)
player = pygame.image.load('player.png').convert_alpha() 
player_rect = player.get_rect(midleft=(50, HEIGHT // 2))

player_move_down = [0,8]
player_move_right = [8,0]
player_move_top = [0, -8]
player_move_left = [-8, 0]

def create_enemy():
    enemy_size = (102.5,36)
    enemy = pygame.image.load('enemy.png'). convert_alpha()
    enemy = pygame.transform.scale(enemy, enemy_size)
    enemy_rect = pygame.Rect(WIDTH, random.randint(0,HEIGHT), *enemy_size)
    enemy_move = [random.randint(-16, -8), 0]
    return [enemy, enemy_rect, enemy_move]

def create_bonus():
    bonus_size = (89.5,149)
    bonus = pygame.image.load('bonus.png'). convert_alpha()
    bonus = pygame.transform.scale(bonus, bonus_size)
    bonus_rect = pygame.Rect(random.randint(0, WIDTH), 0, *bonus_size)
    bonus_move = [0, random.randint(8, 16)]
    return [bonus, bonus_rect, bonus_move]



ENEMY_CREATE_INTERVAL = 3000
ENEMY_SPEED = [-16, 0]
BONUS_CREATE_INTERVAL = 4000
BONUS_SPEED = [0, 8]

CREATE_ENEMY = pygame.USEREVENT + 1
CREATE_BONUSY = pygame.USEREVENT + 2

pygame.time.set_timer(CREATE_ENEMY, ENEMY_CREATE_INTERVAL)
pygame.time.set_timer(CREATE_BONUSY,BONUS_CREATE_INTERVAL)

CHANGE_IMAGE = pygame.USEREVENT+3
pygame.time.set_timer(CHANGE_IMAGE, 200)

enemies = []
bonusies = []

score = 0
image_index = 0

playing = True

while playing:
    FPS.tick(500)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
           enemies.append(create_enemy())
        if event.type == CREATE_BONUSY:
            bonusies.append(create_bonus())   
        if event.type == CHANGE_IMAGE:
            player = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES[image_index]))
            image_index += 1
        if image_index >= len(PLAYER_IMAGES):
            image_index = 0    

    bg_x1 -= bg_move
    bg_x2 -= bg_move

    if bg_x1 < -bg.get_width():
        bg_x1 = bg.get_width()

    if bg_x2 < -bg.get_width():
        bg_x2  = bg.get_width()

    main_display.blit(bg, (bg_x1,0))
    main_display.blit(bg, (bg_x2,0))

    keys = pygame.key.get_pressed()                         

    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)

    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_move_right)

    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(player_move_top)

    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left) 

    for enemy in enemies:
        enemy[1] = enemy[1].move(ENEMY_SPEED)
        main_display.blit(enemy[0], enemy[1])
        if player_rect.colliderect(enemy[1]):
            playing = False
        if enemy[1].right <= 0:
            enemies.pop(enemies.index(enemy))


    for bonus in bonusies:
        bonus[1] = bonus[1].move(BONUS_SPEED)
        main_display.blit(bonus[0], bonus[1])
        if player_rect.colliderect(bonus[1]):
            score += 1
            bonusies.pop(bonusies.index(bonus))
        if bonus[1].bottom >= HEIGHT:
            bonusies.pop(bonusies.index(bonus))

        

    main_display.blit(FONT.render(str(score),True, COLOR_BLUE), (WIDTH-50, 20))
    main_display.blit(player,player_rect)

    pygame.display.flip()

   