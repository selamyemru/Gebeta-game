from main import main
import pygame
def welcome():
    # Constants
    SCREEN_WIDTH = 1536
    SCREEN_HEIGHT = 793
    BUTTON_WIDTH = 200
    BUTTON_HEIGHT = 50
    BUTTON_COLOR = (0, 255, 0)
    BUTTON_HOVER_COLOR = (0, 200, 0)
    BUTTON_TEXT_COLOR = (255, 255, 255)
    BUTTON_TEXT_HOVER_COLOR = (200, 200, 200)

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.RESIZABLE)
    clock = pygame.time.Clock()

    # Load fonts
    font = pygame.font.Font(None, 36)

    # Define game variables
    continue_button_rect = pygame.Rect(
        SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2,
        SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2,
        BUTTON_WIDTH,
        BUTTON_HEIGHT
    )
    continue_button_hovered = False

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and continue_button_rect.collidepoint(event.pos):
                    # Handle button click event
                    # You can navigate to another screen or execute the prepared code here
                    print("Continue button clicked")
                    main()

        # Update game logic
        # Check if the mouse is hovering over the continue button
        mouse_pos = pygame.mouse.get_pos()
        if continue_button_rect.collidepoint(mouse_pos):
            continue_button_hovered = True
        else:
            continue_button_hovered = False

        # Render the game
        screen.fill((0, 0, 0))  # Clear the screen

        # Draw the "Welcome to Gebeta Lite" message
        welcome_text = font.render("Welcome to Gebeta Lite", True, (255, 255, 255))
        welcome_text_rect = welcome_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        screen.blit(welcome_text, welcome_text_rect)

        # Draw the "Continue" button
        button_color = BUTTON_HOVER_COLOR if continue_button_hovered else BUTTON_COLOR
        pygame.draw.rect(screen, button_color, continue_button_rect)
        button_text = font.render("Continue", True, BUTTON_TEXT_HOVER_COLOR if continue_button_hovered else BUTTON_TEXT_COLOR)
        button_text_rect = button_text.get_rect(center=continue_button_rect.center)
        screen.blit(button_text, button_text_rect)

        # Update the display
        pygame.display.flip()
        clock.tick(60)  # Limit the frame rate

    # Quit the game
    pygame.quit()

welcome()