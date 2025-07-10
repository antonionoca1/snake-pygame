
import pygame

def get_line_wrap(text, font, width):
    i = 1
    while font.size(text[:i])[0] < width and i < len(text):
        i += 1
    if i < len(text):
        i = text.rfind(" ", 0, i) + 1
    return i

def render_line(screen, text, font, color, rect, aa=False, bkg=None):
    if bkg:
        image = font.render(text, 1, color, bkg)
        image.set_colorkey(bkg)
    else:
        image = font.render(text, aa, color)
    screen.blit(image, (rect.left, rect.top))

def draw_text(screen, text, font, color, rect, aa=False, bkg=None):
    y = rect.top
    line_spacing = -2
    font_height = font.size("Tg")[1]

    while text:
        if y + font_height > rect.bottom:
            break
        i = get_line_wrap(text, font, rect.width)
        render_line(screen, text[:i], font, color, pygame.Rect(rect.left, y, rect.width, font_height), aa, bkg)
        y += font_height + line_spacing
        text = text[i:]
    return text

def draw_game_elements(screen, snake_body, food_position, snake_block):
    """Draws all game elements on the screen."""
    screen.fill((0, 0, 0)) # Black background
    for segment in snake_body:
        pygame.draw.rect(screen, (255, 255, 255), [segment[0], segment[1], snake_block, snake_block])
    pygame.draw.rect(screen, (255, 0, 0), [food_position[0], food_position[1], snake_block, snake_block])

def draw_game(screen, snake_body, food_position, snake_block, score, font):
    draw_game_elements(screen, snake_body, food_position, snake_block)
    draw_text(screen, f"Score: {score}", font, (255, 255, 255), pygame.Rect(10, 10, 200, 50))
    pygame.display.update()
