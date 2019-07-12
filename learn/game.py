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
heroes = pygame.sprite.Group()
heroes.add(player)
pidgeons = pygame.sprite.Group()

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

    screen.fill((0, 0, 0))
    # Draw the player to the screen
    pressed_keys = pygame.key.get_pressed()
    for hero in heroes:
        hero.update(pressed_keys)
        screen.blit(hero.surf, hero.rect)
    for pidgeon in pidgeons:
        pidgeon.update()
        screen.blit(pidgeon.surf, pidgeon.rect)

    if pygame.sprite.spritecollideany(player, pidgeons):
        player.kill()
        # running = False
    # Update the display
    pygame.display.flip()
