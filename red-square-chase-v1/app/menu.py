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

    # Logo position
    logo_rect = logo.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    # Fade-in effect variables
    logo_alpha = 0

    while True:
        keys = pygame.key.get_pressed()

        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if keys[pygame.K_RETURN]:
                return

        if logo_alpha < 250:
            logo_alpha += 2
        else:
            pygame.time.wait(3000)
            return

        # Set logo transparency
        logo.set_alpha(logo_alpha)

        # Draw the logo
        screen.blit(logo, logo_rect)

        pygame.display.flip()
        clock.tick(60)
