import unittest
from main import reveal

class TestMinesweeper(unittest.TestCase):
    def test_reveal(self):
        grid = [
            [0, 0, 0],
            [0, -1, 0],
            [0, 0, 0]
        ]
        revealed = [
            [False, False, False],
            [False, False, False],
            [False, False, False]
        ]
        reveal(grid, revealed, 0, 0)
        expected_revealed = [
            [True, True, True],
            [True, False, True],
            [True, True, True]
        ]
        self.assertEqual(revealed, expected_revealed)
