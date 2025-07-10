import unittest
import domain

class TestDomain(unittest.TestCase):
    def test_get_initial_snake_position(self):
        pos = domain.get_initial_snake_position(100, 200)
        self.assertEqual(pos, [50, 100])

    def test_get_initial_snake_body(self):
        body = domain.get_initial_snake_body([10, 20])
        self.assertEqual(body, [[10, 20]])

    def test_create_food(self):
        food = domain.create_food(100, 100, 10)
        self.assertTrue(0 <= food[0] <= 90)
        self.assertTrue(0 <= food[1] <= 90)
        self.assertEqual(food[0] % 10, 0)
        self.assertEqual(food[1] % 10, 0)

    def test_is_collision(self):
        self.assertTrue(domain.is_collision([1, 2], [1, 2]))
        self.assertFalse(domain.is_collision([1, 2], [2, 1]))

    def test_is_out_of_bounds(self):
        self.assertTrue(domain.is_out_of_bounds([101, 50], 100, 100))
        self.assertTrue(domain.is_out_of_bounds([-1, 50], 100, 100))
        self.assertTrue(domain.is_out_of_bounds([50, 101], 100, 100))
        self.assertTrue(domain.is_out_of_bounds([50, -1], 100, 100))
        self.assertFalse(domain.is_out_of_bounds([50, 50], 100, 100))

    def test_has_self_collided(self):
        self.assertTrue(domain.has_self_collided([[1,2],[1,2],[3,4]]))
        self.assertFalse(domain.has_self_collided([[1,2],[3,4],[5,6]]))

    def test_update_snake_position(self):
        pos = domain.update_snake_position([5, 5], [1, 2])
        self.assertEqual(pos, [6, 7])

    def test_update_snake_body(self):
        body = [[2,2],[1,2]]
        new_body = domain.update_snake_body(body.copy(), [3,2], False)
        self.assertEqual(new_body, [[3,2],[2,2]])
        new_body = domain.update_snake_body(body.copy(), [3,2], True)
        self.assertEqual(new_body, [[3,2],[2,2],[1,2]])

if __name__ == "__main__":
    unittest.main()
