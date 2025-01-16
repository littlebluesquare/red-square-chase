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
from pathlib import Path
from random import randint
from menu import show_logo_menu

pygame.init()

file_path = Path(__file__).parent.parent / "src"

# Colors
BLACK = pygame.color.Color((0, 0, 0))
BLUE  = pygame.color.Color((0, 0, 250))
RED   = pygame.color.Color((250, 0, 0))
WHITE = pygame.color.Color((250, 250, 250))

# Screen Set
WIDTH, HEIGHT = 600, 400
x_position = WIDTH // 2
y_position = HEIGHT // 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Square Chase")
icon = pygame.image.load(file_path / "icon.png")
pygame.display.set_icon(icon)
score = 0

# Sprite Set
blue_square_size = 40
blue_square_x_position = x_position
blue_square_y_position = y_position
blue_square_width = 5
speed = 3

red_square_size = blue_square_size // 2
red_square_x_position = 0
red_square_width = blue_square_width - 1

clock = pygame.time.Clock()


def generate_random_position():
    while True:
        random_x_position = randint(0, WIDTH - red_square_size)
        if (random_x_position + red_square_size < blue_square_x_position or
            random_x_position > blue_square_x_position + blue_square_size):
            return random_x_position


def draw_blue_square():
    pygame.draw.rect(surface=screen, color=BLUE, rect=(blue_square_x_position, blue_square_y_position,
                                                       blue_square_size, blue_square_size), width=blue_square_width)


def draw_red_square():
    global red_square_x_position
    if not red_square_x_position:
        red_square_x_position = generate_random_position()
    pygame.draw.rect(surface=screen, color=RED, rect=(red_square_x_position, blue_square_y_position + red_square_size,
                                                      red_square_size, red_square_size), width=red_square_width)


def write_score():
    font = pygame.font.Font(file_path / "PressStart2P.ttf", 18)
    text = font.render("{}".format(score), True, BLACK)
    render_position = (20, 20)
    screen.blit(text, render_position)


def reset():
    global score
    score = 0
    show_logo_menu(screen, clock)  # Show the logo menu when resetting
    main_game()

# Main Loop
def main_game():
    global blue_square_x_position, red_square_x_position, score
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

        if keys[pygame.K_LEFT] and blue_square_x_position > 0:
            blue_square_x_position -= speed
        if keys[pygame.K_RIGHT] and blue_square_x_position < WIDTH - blue_square_size:
            blue_square_x_position += speed
        if red_square_x_position + red_square_size > blue_square_x_position > red_square_x_position - blue_square_size:
            red_square_x_position = 0
            score += 1
        if keys[pygame.K_r]:
            reset()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    show_logo_menu(screen, clock)
    main_game()
