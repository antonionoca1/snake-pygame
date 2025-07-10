import unittest
import pygame
import drawing
from unittest.mock import patch

class TestDrawing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.init()
        cls.screen = pygame.Surface((300, 200))
        cls.font = pygame.font.SysFont(None, 24)

    def test_get_line_wrap(self):
        text = "This is a test string for wrapping."
        width = 100
        i = drawing.get_line_wrap(text, self.font, width)
        self.assertIsInstance(i, int)
        self.assertGreater(i, 0)

    def test_render_line(self):
        rect = pygame.Rect(0, 0, 100, 30)
        # Should not raise
        drawing.render_line(self.screen, "Test", self.font, (255,255,255), rect)
        drawing.render_line(self.screen, "Test", self.font, (255,255,255), rect, aa=True, bkg=(0,0,0))

    def test_draw_text(self):
        rect = pygame.Rect(0, 0, 100, 50)
        text = "This is a test string for drawing."
        remaining = drawing.draw_text(self.screen, text, self.font, (255,255,255), rect)
        self.assertIsInstance(remaining, str)

    def test_draw_game_elements(self):
        snake_body = [[10,10],[20,10]]
        food_position = [30,30]
        snake_block = 10
        # Should not raise
        drawing.draw_game_elements(self.screen, snake_body, food_position, snake_block)

    @patch('pygame.display.update')
    def test_draw_game(self, mock_update):
        snake_body = [[10,10],[20,10]]
        food_position = [30,30]
        snake_block = 10
        score = 5
        # Should not raise
        drawing.draw_game(self.screen, snake_body, food_position, snake_block, score, self.font)
        mock_update.assert_called()

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

if __name__ == "__main__":
    unittest.main()
