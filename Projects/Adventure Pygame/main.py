import pygame

# Initialize Pygame
pygame.init()

# Set the window dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the window caption
pygame.display.set_caption("Star of Dawn")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Render text
    font = pygame.font.Font(None, 30)
    text = font.render("Chapter 1: Ashen Queen", True, (255, 255, 255))
    screen.blit(text, (250, 250))

    # Update the screen
    pygame.display.update()

# Exit Pygame
pygame.quit()
