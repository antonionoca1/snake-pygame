
import pygame
import sys
from domain import *
from drawing import *
from input import *

def initialize_game():
    """Initializes pygame and returns the screen."""
    pygame.init()
    screen = pygame.display.set_mode((600, 400), pygame.RESIZABLE)
    pygame.display.set_caption('Snake Game')
    return screen

def show_screen(screen, title, subtitle, font, clock, color=(255, 255, 255)):
    """Displays a generic screen with a title and subtitle, waiting for a key press."""
    screen.fill((0, 0, 0))
    title_rect = pygame.Rect(screen.get_width() / 6, screen.get_height() / 4, screen.get_width() * 2 / 3, screen.get_height() / 4)
    draw_text(screen, title, font, color, title_rect)
    subtitle_rect = pygame.Rect(screen.get_width() / 6, screen.get_height() / 2, screen.get_width() * 2 / 3, screen.get_height() / 2)
    draw_text(screen, subtitle, font, color, subtitle_rect)
    pygame.display.update()
    wait_for_key(clock)

def update_game_state(snake_position, position_change, snake_body, food_position, score, screen_width, screen_height, snake_block):
    snake_position = update_snake_position(snake_position, position_change)
    game_over = is_out_of_bounds(snake_position, screen_width, screen_height) or has_self_collided(snake_body)
    ate_food = is_collision(snake_position, food_position)
    if ate_food:
        food_position = create_food(screen_width, screen_height, snake_block)
        score += 1
    snake_body = update_snake_body(snake_body, snake_position, ate_food)
    return snake_position, snake_body, food_position, score, game_over, ate_food

def game_loop(screen):
    """The main game loop."""
    screen_width, screen_height = screen.get_size()
    snake_block = 10
    snake_position = get_initial_snake_position(screen_width, screen_height)
    snake_body = get_initial_snake_body(snake_position)
    position_change = [0, 0]
    food_position = create_food(screen_width, screen_height, snake_block)
    score = 0
    font = pygame.font.SysFont(None, 50)
    clock = pygame.time.Clock()
    show_screen(screen, "Snake Game", "Press C to Play or Q to Quit", font, clock)
    game_over = False
    while not game_over:
        game_over, new_change = handle_game_events(game_over, snake_block)
        if new_change:
            position_change = new_change
        snake_position, snake_body, food_position, score, game_over, ate_food = update_game_state(snake_position, position_change, snake_body, food_position, score, screen_width, screen_height, snake_block)
        draw_game(screen, snake_body, food_position, snake_block, score, font)
        if game_over:
            show_screen(screen, f"Game Over! Score: {score}", "Press C to Play Again or Q to Quit", font, clock, color=(255,0,0))
            game_loop(screen) # Restart
        clock.tick(15)
    pygame.quit()
    sys.exit()
