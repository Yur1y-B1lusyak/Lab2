import sys
from settings import *
from create_grid import create_grid
from draw_grid import draw_grid
from reveal import reveal
from check_win import check_win
from draw_end_screen import draw_end_screen

# Основна функція гри
def main():
    while True:
        grid, mines = create_grid(ROWS, COLS, MINE_COUNT)
        revealed = [[False for _ in range(COLS)] for _ in range(ROWS)]
        flags = [[False for _ in range(COLS)] for _ in range(ROWS)]
        game_over = False
        game_won = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                    x, y = event.pos
                    r, c = y // TILE_SIZE, x // TILE_SIZE
                    if event.button == 1:  # Ліва кнопка миші
                        if not flags[r][c]:
                            if grid[r][c] == -1:
                                game_over = True
                            else:
                                reveal(grid, revealed, r, c)
                                if check_win(grid, revealed):
                                    game_won = True
                                    game_over = True
                    elif event.button == 3:  # Права кнопка миші
                        if not revealed[r][c]:
                            flags[r][c] = not flags[r][c]

            screen.fill(WHITE)
            draw_grid(grid, revealed, flags)

            if game_over:
                if game_won:
                    message = "You win!"
                else:
                    message = "Game Over"
                button_rect = draw_end_screen(message)
                pygame.display.flip()

                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if button_rect.collidepoint(event.pos):
                                main()
                            break
                    else:
                        continue
                    break

            pygame.display.flip()

if __name__ == "__main__":
    main()
