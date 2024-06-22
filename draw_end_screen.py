from settings import *

def draw_end_screen(message):
    screen.fill(WHITE)
    text = BUTTON_FONT.render(message, True, GREEN if message == "You win!" else RED)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 - 50))

    button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 60)
    pygame.draw.rect(screen, BLUE, button_rect)
    button_text = BUTTON_FONT.render("Restart", True, WHITE)
    screen.blit(button_text, (button_rect.x + 25, button_rect.y + 10))

    return button_rect