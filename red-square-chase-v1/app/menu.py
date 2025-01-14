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

file_path = Path(__file__).parent.parent / "src"

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Function for the logo menu
def show_logo_menu(screen, clock):
    # Load logo
    logo = pygame.image.load(file_path / "logo.png")
    logo = pygame.transform.scale(logo, (400, 300))
    font = pygame.font.Font(None, 40)

    # Logo position
    logo_rect = logo.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    # Fade-in effect variables
    logo_alpha = 0
    fade_in = True

    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return


        if fade_in:
            logo_alpha += 1
            if logo_alpha >= 255:
                logo_alpha = 255
                fade_in = False
        else:
            pygame.time.wait(8000)
            return

        # Set logo transparency
        logo.set_alpha(logo_alpha)

        # Draw the logo
        screen.blit(logo, logo_rect)

        # Optional: Add "Press any key" text
        text = font.render("Press any key to continue...", True, BLACK)
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() - 50))
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)
