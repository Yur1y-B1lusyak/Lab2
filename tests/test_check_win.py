from main import check_win


def test_check_win(self):
    grid = [
        [0, 1, -1],
        [0, 1, 1],
        [0, 0, 0]
    ]
    revealed = [
        [True, True, False],
        [True, True, True],
        [True, True, True]
    ]
    self.assertTrue(check_win(grid, revealed))

    revealed = [
        [True, True, False],
        [True, True, False],
        [True, True, True]
    ]
    self.assertFalse(check_win(grid, revealed))
