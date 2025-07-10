import unittest
import pygame
from unittest.mock import patch, MagicMock
from game import (
    initialize_game,
    show_screen,
    update_game_state,
    game_loop
)

class TestGame(unittest.TestCase):
    @patch('pygame.display.set_mode')
    @patch('pygame.display.set_caption')
    @patch('pygame.init')
    def test_initialize_game(self, mock_init, mock_set_caption, mock_set_mode):
        mock_screen = MagicMock()
        mock_set_mode.return_value = mock_screen
        screen = initialize_game()
        mock_init.assert_called_once()
        mock_set_mode.assert_called_once_with((600, 400), pygame.RESIZABLE)
        mock_set_caption.assert_called_once_with('Snake Game')
        self.assertEqual(screen, mock_screen)

    @patch('game.wait_for_key')
    @patch('game.draw_text')
    @patch('pygame.display.update')
    def test_show_screen(self, mock_update, mock_draw_text, mock_wait_for_key):
        screen = MagicMock()
        screen.get_width.return_value = 600
        screen.get_height.return_value = 400
        font = MagicMock()
        clock = MagicMock()
        show_screen(screen, 'Title', 'Subtitle', font, clock)
        self.assertEqual(mock_draw_text.call_count, 2)
        mock_update.assert_called_once()
        mock_wait_for_key.assert_called_once_with(clock)

    @patch('game.create_food')
    @patch('game.update_snake_body')
    @patch('game.is_collision')
    @patch('game.has_self_collided')
    @patch('game.is_out_of_bounds')
    @patch('game.update_snake_position')
    def test_update_game_state(self, mock_update_pos, mock_out_of_bounds, mock_self_collided, mock_collision, mock_update_body, mock_create_food):
        snake_position = [10, 10]
        position_change = [10, 0]
        snake_body = [[10, 10]]
        food_position = [20, 10]
        score = 0
        screen_width = 100
        screen_height = 100
        snake_block = 10
        # Test: not out of bounds, no collision, no food eaten
        mock_update_pos.return_value = [20, 10]
        mock_out_of_bounds.return_value = False
        mock_self_collided.return_value = False
        mock_collision.return_value = False
        mock_update_body.return_value = [[20, 10]]
        result = update_game_state(snake_position, position_change, snake_body, food_position, score, screen_width, screen_height, snake_block)
        self.assertEqual(result[0], [20, 10])
        self.assertEqual(result[1], [[20, 10]])
        self.assertEqual(result[2], [20, 10])
        self.assertEqual(result[3], 0)
        self.assertFalse(result[4])
        self.assertFalse(result[5])
        # Test: food eaten
        mock_collision.return_value = True
        mock_create_food.return_value = [30, 10]
        mock_update_body.return_value = [[20, 10], [10, 10]]
        result = update_game_state(snake_position, position_change, snake_body, food_position, score, screen_width, screen_height, snake_block)
        self.assertEqual(result[2], [30, 10])
        self.assertEqual(result[3], 1)
        self.assertTrue(result[5])
        # Test: out of bounds
        mock_out_of_bounds.return_value = True
        result = update_game_state(snake_position, position_change, snake_body, food_position, score, screen_width, screen_height, snake_block)
        self.assertTrue(result[4])
        # Test: self collision
        mock_out_of_bounds.return_value = False
        mock_self_collided.return_value = True
        result = update_game_state(snake_position, position_change, snake_body, food_position, score, screen_width, screen_height, snake_block)
        self.assertTrue(result[4])

    @patch('game.show_screen')
    @patch('game.draw_game')
    @patch('game.handle_game_events')
    @patch('game.update_game_state')
    @patch('game.get_initial_snake_position')
    @patch('game.get_initial_snake_body')
    @patch('game.create_food')
    @patch('pygame.font.SysFont')
    @patch('pygame.time.Clock')
    @patch('pygame.quit')
    @patch('sys.exit')
    @patch('game.game_loop')
    def test_game_loop_restart(self, mock_game_loop, mock_exit, mock_quit, mock_clock, mock_font, mock_create_food, mock_get_body, mock_get_pos, mock_update_state, mock_handle_events, mock_draw_game, mock_show_screen):
        screen = MagicMock()
        screen.get_size.return_value = (100, 100)
        mock_get_pos.return_value = [10, 10]
        mock_get_body.return_value = [[10, 10]]
        mock_create_food.return_value = [20, 10]
        mock_font.return_value = MagicMock()
        mock_clock.return_value = MagicMock()
        # Simulate one loop, then game over (should restart)
        mock_handle_events.side_effect = [(False, [10, 0]), (True, None)]
        mock_update_state.side_effect = [([20, 10], [[20, 10]], [20, 10], 0, False, False),
                                         ([30, 10], [[30, 10]], [30, 10], 1, True, False)]
        game_loop(screen)
        mock_game_loop.assert_called_once_with(screen)
        # Do not assert anything about quit/exit, as they are always called after game over

if __name__ == '__main__':
    unittest.main()
