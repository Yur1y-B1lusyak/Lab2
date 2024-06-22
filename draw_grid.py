from settings import *

# Функція для відображення поля
def draw_grid(grid, revealed, flags):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            rect = pygame.Rect(c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if revealed[r][c]:
                pygame.draw.rect(screen, GRAY, rect)
                if grid[r][c] > 0:
                    text = FONT.render(str(grid[r][c]), True, BLACK)
                    screen.blit(text, (c * TILE_SIZE + TILE_SIZE // 3, r * TILE_SIZE + TILE_SIZE // 4))
                elif grid[r][c] == -1:
                    pygame.draw.circle(screen, BLACK, rect.center, TILE_SIZE // 3)
            else:
                pygame.draw.rect(screen, WHITE, rect)
                if flags[r][c]:
                    pygame.draw.line(screen, RED, rect.topleft, rect.bottomright, 2)
                    pygame.draw.line(screen, RED, rect.topright, rect.bottomleft, 2)
            pygame.draw.rect(screen, BLACK, rect, 1)