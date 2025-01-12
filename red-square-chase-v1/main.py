#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author: Victor V. R. Matos (@vvrmatos) & Little Blue Square
# Description: This script implements a simple game using Pygame where the player controls
#              a blue square, which must collect red squares to increase the score. The blue
#              square moves horizontally based on keyboard input, and red squares are generated
#              at random positions on the screen.
# License: CC0 1.0 Universal

import sys
import pygame

from random import randint

pygame.init()

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 250)
RED = (250, 0, 0)
WHITE = (250, 250, 250)

# Screen Set
WIDTH, HEIGHT = 600, 400
x_position = WIDTH // 2
y_position = HEIGHT // 2
initial_position = (x_position, y_position)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Square Chase")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
score = 0

# Sprite Set
blue_square_size = 40
red_square_size = blue_square_size // 2
red_x_position = 0
speed = 3

# Time For FPS Control
clock = pygame.time.Clock()


def generate_random_position():
    while True:
        random_x_position = randint(0, WIDTH - red_square_size)
        if random_x_position + red_square_size < x_position or random_x_position > x_position + blue_square_size:
            return random_x_position


def draw_blue_square():
    pygame.draw.rect(surface=screen, color=BLUE, rect=(x_position, y_position, blue_square_size, blue_square_size),
                     width=5)


def draw_red_square():
    global red_x_position
    if not red_x_position:
        red_x_position = generate_random_position()
    pygame.draw.rect(surface=screen, color=RED,
                     rect=(red_x_position, y_position + red_square_size, red_square_size, red_square_size), width=4)


def write_score():
    font = pygame.font.Font("PressStart2P.ttf", 18)
    text = font.render("{}".format(score), True, BLACK)
    render_position = (20, 20)
    screen.blit(text, render_position)


# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Screen Actions
    screen.fill(WHITE)
    draw_blue_square()
    draw_red_square()
    write_score()

    # Key Events
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x_position > 0:
        x_position -= speed
    if keys[pygame.K_RIGHT] and x_position < WIDTH - blue_square_size:
        x_position += speed
    if red_x_position + red_square_size > x_position > red_x_position - blue_square_size:
        red_x_position = 0
        score += 1

    pygame.display.flip()
    clock.tick(60)
