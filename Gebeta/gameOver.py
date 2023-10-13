import pygame

def gameOver(winner):
    # Constants
    WIDTH = 1536
    HEIGHT = 793

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
    font = pygame.font.SysFont(None, 80)
    win = font.render("Player "+str(winner) + ' won!', True, (0, 0, 0))
    text = font.render("Game Over", True, (0, 0, 0))
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    win_rect = win.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 100))
    screen.fill((255,255,255))
    screen.blit(text, text_rect)
    screen.blit(win, win_rect)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()

# gameOver(1)

