import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame Example")

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(white)

    # Draw a blue rectangle
    pygame.draw.rect(screen, blue, (200, 150, 400, 300))

    # Draw a red circle
    pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50)

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
#test