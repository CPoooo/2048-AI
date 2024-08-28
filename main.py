import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 750))
pygame.display.set_caption("2048 By Cameron Pool")
clock = pygame.time.Clock()

BACKGROUND_COLOR = (255, 245, 219)  # Light beige
TEXT_COLOR = (77, 70, 53)
EMPTY_SQUARE_COLOR = (201, 197, 187)
LINES_COLOR = (153, 149, 139)
WHITE = (255, 255, 255)  # Color for the text inside squares

# Title font "2048"
font = pygame.font.Font(None, 120)
text_surface = font.render('2048', True, TEXT_COLOR)

# New subtitle font
subtitle_font = pygame.font.Font(None, 20)
subtitle_surface = subtitle_font.render(
    "Join the numbers together and get to the 2048 tile!", True, TEXT_COLOR
)

# Score squares
score_square_height = 75
score_square_width = 100
square_color = LINES_COLOR
square_position = (350, 20)

# Font for text inside the squares
small_font = pygame.font.Font(None, 30)  # Adjust size as needed
score_text_surface = small_font.render('Score', True, WHITE)
best_text_surface = small_font.render('Best', True, WHITE)

# Font for text inside the new square
new_game_font = pygame.font.Font(None, 30)  # Adjust size as needed
new_game_text_surface = new_game_font.render('New Game', True, WHITE)

# Positioning text
title_rect = text_surface.get_rect(topleft=(20, 20))
subtitle_rect = subtitle_surface.get_rect(topleft=(20, 120))  # 20 pixels from left and below the title

# Calculate total width for the new rectangle
total_width = 2 * score_square_width + 10  # Two squares + margin

# Positioning the new rectangle
rectangle_position = (20, 120 + 75 + 10)  # 120 for subtitle + 75 for score square height + 10 margin
rectangle_height = 30

# Position for the "New Game" square
new_game_square_position = (350, 115)  # Under the previous rectangle + margin
new_game_square_width = total_width  # Same width as the combined score squares

# Draw the game board square
game_square_position = (40, 180)  # 20 pixels from the left, 150 pixels from the top
game_square_size = 520  # Size of the square

# Calculate the size of each empty square
empty_square_size = (game_square_size - 45) // 4  # 10 pixels spacing on each side of the grid

running = True

while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Initialize the screen
    screen.fill(BACKGROUND_COLOR)
    screen.blit(text_surface, title_rect)

    # Draw the rectangles
    pygame.draw.rect(screen, square_color,
                     pygame.Rect(square_position[0], square_position[1], score_square_width, score_square_height))
    pygame.draw.rect(screen, square_color,
                     pygame.Rect(square_position[0] + score_square_width + 10, square_position[1], score_square_width,
                                 score_square_height))

    # Calculate positions for the text to be centered in each square
    score_text_rect = score_text_surface.get_rect(
        center=(square_position[0] + score_square_width // 2, square_position[1] + score_square_height // 2 - 20))
    best_text_rect = best_text_surface.get_rect(center=(
        square_position[0] + score_square_width + 10 + score_square_width // 2,
        square_position[1] + score_square_height // 2 - 20))

    # Blit the text onto the screen
    screen.blit(score_text_surface, score_text_rect)
    screen.blit(best_text_surface, best_text_rect)

    # Blit the subtitle onto the screen
    screen.blit(subtitle_surface, subtitle_rect)

    # Draw the "New Game" rectangle
    pygame.draw.rect(screen, TEXT_COLOR, pygame.Rect(new_game_square_position[0], new_game_square_position[1],
                                                     new_game_square_width, rectangle_height))

    # Blit the "New Game" text onto the new rectangle
    new_game_text_rect = new_game_text_surface.get_rect(
        center=(new_game_square_position[0] + new_game_square_width // 2,
                new_game_square_position[1] + rectangle_height // 2))
    screen.blit(new_game_text_surface, new_game_text_rect)

    # Draw the game board square
    pygame.draw.rect(screen, LINES_COLOR,
                     pygame.Rect(game_square_position[0], game_square_position[1], game_square_size, game_square_size))

    # Draw the 4x4 grid of empty squares
    for row in range(4):
        for col in range(4):
            x = game_square_position[0] + 10 + col * (empty_square_size + 10)
            y = game_square_position[1] + 10 + row * (empty_square_size + 10)
            pygame.draw.rect(screen, EMPTY_SQUARE_COLOR, pygame.Rect(x, y, empty_square_size, empty_square_size))

    # Flip the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # Limits FPS to 60

pygame.quit()
