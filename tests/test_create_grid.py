from main import create_grid


def test_create_grid(self):
    rows, cols, mine_count = 5, 5, 5
    grid, mines = create_grid(rows, cols, mine_count)
    self.assertEqual(len(mines), mine_count)
    mine_cells = sum(row.count(-1) for row in grid)
    self.assertEqual(mine_cells, mine_count)
