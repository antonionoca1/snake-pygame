
import pygame
import sys

def handle_input(event, snake_block):
    """Handles user input for snake movement."""
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            return [-snake_block, 0]
        elif event.key == pygame.K_RIGHT:
            return [snake_block, 0]
        elif event.key == pygame.K_UP:
            return [0, -snake_block]
        elif event.key == pygame.K_DOWN:
            return [0, snake_block]
    return None

def wait_for_key(clock):
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_c:
                    waiting = False
        clock.tick(15)

def handle_game_events(game_over, snake_block):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True, None
        new_change = handle_input(event, snake_block)
        if new_change:
            return game_over, new_change
    return game_over, None
