
import random

def get_initial_snake_position(screen_width, screen_height):
    """Returns the initial position for the snake."""
    return [screen_width / 2, screen_height / 2]

def get_initial_snake_body(snake_position):
    """Returns the initial snake body."""
    return [list(snake_position)]

def create_food(screen_width, screen_height, snake_block):
    """Creates a food item at a random position."""
    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
    return [foodx, foody]

def is_collision(pos1, pos2):
    """Checks if two positions are the same."""
    return pos1[0] == pos2[0] and pos1[1] == pos2[1]

def is_out_of_bounds(position, screen_width, screen_height):
    """Checks if a position is out of the screen bounds."""
    x, y = position
    return x >= screen_width or x < 0 or y >= screen_height or y < 0

def has_self_collided(snake_body):
    """Checks if the snake has collided with itself."""
    return snake_body[0] in snake_body[1:]

def update_snake_position(snake_position, change):
    """Updates the snake's head position."""
    snake_position[0] += change[0]
    snake_position[1] += change[1]
    return snake_position

def update_snake_body(snake_body, snake_position, ate_food):
    """Updates the snake's body."""
    snake_body.insert(0, list(snake_position))
    if not ate_food:
        snake_body.pop()
    return snake_body
