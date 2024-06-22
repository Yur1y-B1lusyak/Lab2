import random

# Функція для створення поля
def create_grid(rows, cols, mine_count):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    mines = set()

    while len(mines) < mine_count:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if (r, c) not in mines:
            mines.add((r, c))
            grid[r][c] = -1

    for r, c in mines:
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] != -1:
                    grid[rr][cc] += 1

    return grid, mines