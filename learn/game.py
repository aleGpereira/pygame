import random

import pygame
from pygame.locals import *

from sprites import Player, Pidgeon
from events import LETGO_PIDGEON


pygame.init()
screen = pygame.display.set_mode((800, 600))

# Variable to keep our main loop running
running = True

player = Player()

pidgeons = pygame.sprite.Group()
characters = pygame.sprite.Group()
characters.add(player)

pygame.time.set_timer(LETGO_PIDGEON, 500)

# Our main loop!
while running:

    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals, which we imported earlier
        if event.type == KEYDOWN:
            # If the Esc key has been pressed set running to false to exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event; if QUIT, set running to false
        elif event.type == QUIT:
            running = False
        elif event.type == LETGO_PIDGEON:
            pidgeon = Pidgeon()
            pidgeons.add(pidgeon)
            print("pidgeon added")

    pressed_keys = pygame.key.get_pressed()
    # Draw the player to the screen
    screen.fill((0, 0, 0))
    for character in characters:
        character.update(pressed_keys)
        screen.blit(character.surf, character.rect)
    for pidgeon in pidgeons:
        pidgeon.update()
        screen.blit(pidgeon.surf, pidgeon.rect)

    # Update the display
    pygame.display.flip()
