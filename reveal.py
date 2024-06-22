# Функція для відкриття порожніх клітинок
def reveal(grid, revealed, r, c):
    rows = len(grid)
    cols = len(grid[0])
    if 0 <= r < rows and 0 <= c < cols and not revealed[r][c]:
        revealed[r][c] = True
        if grid[r][c] == 0:
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if dr != 0 or dc != 0:
                        reveal(grid, revealed, r + dr, c + dc)
