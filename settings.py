import pygame

# Ініціалізація Pygame
pygame.init()

# Налаштування
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 20, 20
MINE_COUNT = 40
TILE_SIZE = WIDTH // COLS

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Вікно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

# Шрифти
FONT = pygame.font.Font(None, 36)
BUTTON_FONT = pygame.font.Font(None, 48)
