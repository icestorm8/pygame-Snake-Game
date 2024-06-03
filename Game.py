# Import and initialize the pygame library
import sys

import pygame

from Board import Board
from Food import Food
from Snake import Snake

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CELADON = (175, 225, 175)
DARK_GREEN = (2, 48, 32)
CADET_BLUE = (95, 158, 160)
EUCALYPTUS = (95, 133, 117)
CORAL_PINK = (248, 131, 121)

# window settings
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Tic Tac Toe")
HEIGHT, WIDTH = 500, 500

# board settings
CELL_SIZE = 30
NUMBER_OF_CELLS = 25

# game settings
player_score = 0
speed_of_snake = 15


# Run until the user asks to quit/ or wins or loses


# def draw_grid(screen):
#     for x in range(0, NUMBER_OF_CELLS, CELL_SIZE):
#         for y in range(0, NUMBER_OF_CELLS, CELL_SIZE):
#             rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
#             pygame.draw.rect(screen, CADET_BLUE, rect, 1)


class Game:
    def __init__(self, screen, mode: bool):
        mode: bool = mode  # true for 2 player, false for 1 player w/ bot
        screen = screen
        game_over = False
        self.board = Board()
        self.snake = Snake(CELL_SIZE, CELADON)
        self.target = Food()
        while not game_over:
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        # get back to menu on esc key press
                        return
                    if event.key == pygame.K_UP:
                        self.snake.change_direction('UP')
                    if event.key == pygame.K_DOWN:
                        self.snake.change_direction('DOWN')
                    if event.key == pygame.K_LEFT:
                        self.snake.change_direction('LEFT')
                    if event.key == pygame.K_RIGHT:
                        self.snake.change_direction("RIGHT")
                        print("right")

                        # Fill the background with white
            screen.fill(EUCALYPTUS)
            # draw_grid(screen)
            # Draw a solid blue circle in the center
            # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
            self.snake.draw_snake(screen)
            # Flip the display

            clock.tick(speed_of_snake)
            pygame.display.flip()

        # Done! Time to quit.
        pygame.quit()

    # pygame.display.quit()
    # pygame.quit()
    # quit()
