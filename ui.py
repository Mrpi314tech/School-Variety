import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up window dimensions
width, height = 700, 600

# Create the window
display_surface = pygame.display.set_mode((width, height))

# Set the window title
pygame.display.set_caption("School Variety")

# Set up font and text
font = pygame.font.Font(None, 36)  # None means default font
text = font.render("School Variety", True, (0, 0, 0))  # Render text with black color

# Load images (substitute the file paths accordingly)
image1 = pygame.image.load("english.png")
image2 = pygame.image.load("spanish.png")
image3 = pygame.image.load("tour.png")
image4 = pygame.image.load("lunch.png")
image5 = pygame.image.load("school_variety.png")

# Resize images to fit the window
image1 = pygame.transform.scale(image1, (190, 50))
image2 = pygame.transform.scale(image2, (190, 50))
image3 = pygame.transform.scale(image3, (150, 115))
image4 = pygame.transform.scale(image4, (115, 115))
image5 = pygame.transform.scale(image5, (115, 115))

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update game logic here

    # Clear the screen
    display_surface.fill((255, 255, 255))  # Fill with white
    # Draw images on the screen (adjust positions accordingly)
    display_surface.blit(image1, (50, 50))
    display_surface.blit(image2, (450, 50))
    display_surface.blit(image3, (50, 450))
    display_surface.blit(image4, (450, 450))
    display_surface.blit(image5, (292.5, 240))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)
