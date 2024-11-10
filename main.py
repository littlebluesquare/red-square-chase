#!/usr/bin/env python

import sys
import pygame
from random import randint

pygame.init()

# Colors
WHITE = (250, 250, 250)
BLUE = (0, 0, 250)
RED = (250, 0, 0)

# Screen
WIDTH, HEIGHT = 600, 400
x_position = WIDTH / 2
y_position = HEIGHT / 2
initial_position = (x_position, y_position)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Little Blue Square")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
score = 0

# Sprite
square_size = 40
speed = 2.7
red_x_position = 0


# Time
clock = pygame.time.Clock()


def generate_random_position():
    return randint(0, WIDTH - square_size)


def draw_blue_square():
    pygame.draw.rect(surface=screen, color=BLUE, rect=(x_position, y_position, square_size, square_size), width=5)


def draw_red_square():
    global red_x_position
    if not red_x_position:
        red_x_position = generate_random_position()
    pygame.draw.rect(surface=screen, color=RED,
                     rect=(red_x_position, y_position + square_size / 2, square_size / 2, square_size / 2), width=4)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(score)
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    draw_blue_square()
    draw_red_square()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x_position > 0:
        x_position -= speed
    if keys[pygame.K_RIGHT] and x_position < WIDTH - square_size:
        x_position += speed
    if red_x_position + square_size / 2 > x_position > red_x_position - square_size:
        red_x_position = 0
        score += 1

    pygame.display.flip()

    clock.tick(60)
