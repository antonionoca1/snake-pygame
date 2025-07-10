import pygame
import sys
import random

# --- Domain ---

def initialize_game():
    """Initializes pygame and returns the screen."""
    pygame.init()
    screen = pygame.display.set_mode((600, 400), pygame.RESIZABLE)
    pygame.display.set_caption('Snake Game')
    return screen

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

# --- Application ---

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

def draw_text(screen, text, font, color, rect, aa=False, bkg=None):
    y = rect.top
    line_spacing = -2

    # get the height of the font
    font_height = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + font_height > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the screen
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        screen.blit(image, (rect.left, y))
        y += font_height + line_spacing

        # remove the text we just blitted
        text = text[i:]

    return text

def draw_game_elements(screen, snake_body, food_position, snake_block):
    """Draws all game elements on the screen."""
    screen.fill((0, 0, 0)) # Black background
    for segment in snake_body:
        pygame.draw.rect(screen, (255, 255, 255), [segment[0], segment[1], snake_block, snake_block])
    pygame.draw.rect(screen, (255, 0, 0), [food_position[0], food_position[1], snake_block, snake_block])

def show_screen(screen, title, subtitle, font, clock, color=(255, 255, 255)):
    """Displays a generic screen with a title and subtitle, waiting for a key press."""
    screen.fill((0, 0, 0))
    
    title_rect = pygame.Rect(screen.get_width() / 6, screen.get_height() / 4, screen.get_width() * 2 / 3, screen.get_height() / 4)
    draw_text(screen, title, font, color, title_rect)

    subtitle_rect = pygame.Rect(screen.get_width() / 6, screen.get_height() / 2, screen.get_width() * 2 / 3, screen.get_height() / 2)
    draw_text(screen, subtitle, font, color, subtitle_rect)
    
    pygame.display.update()
    
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

def game_loop(screen):
    """The main game loop."""
    game_over = False
    
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

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
            new_change = handle_input(event, snake_block)
            if new_change:
                position_change = new_change

        snake_position = update_snake_position(snake_position, position_change)

        if is_out_of_bounds(snake_position, screen_width, screen_height) or has_self_collided(snake_body):
            game_over = True

        ate_food = is_collision(snake_position, food_position)
        if ate_food:
            food_position = create_food(screen_width, screen_height, snake_block)
            score += 1

        snake_body = update_snake_body(snake_body, snake_position, ate_food)

        draw_game_elements(screen, snake_body, food_position, snake_block)
        draw_text(screen, f"Score: {score}", font, (255, 255, 255), pygame.Rect(10, 10, 200, 50))
        pygame.display.update()

        if game_over:
            show_screen(screen, f"Game Over! Score: {score}", "Press C to Play Again or Q to Quit", font, clock, color=(255,0,0))
            game_loop(screen) # Restart

        clock.tick(15)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main_screen = initialize_game()
    game_loop(main_screen)