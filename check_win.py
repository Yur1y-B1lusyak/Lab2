def check_win(grid, revealed):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != -1 and not revealed[r][c]:
                return False
    return True