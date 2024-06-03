# Import and initialize the pygame library
import sys

import pygame

from Board import Board

from EndScreen import EndScreen
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
NUMBER_OF_CELLS = 20

# game settings
speed_of_snake = 5


# Run until the user asks to quit/ or wins or loses

class Game:

    def __init__(self, mode: bool):
        mode: bool = mode  # true for 2 player, false for 1 player w/ bot
        self.screen = pygame.display.set_mode((CELL_SIZE * NUMBER_OF_CELLS, CELL_SIZE * NUMBER_OF_CELLS))
        self.board = Board()
        self.snake = Snake(CELL_SIZE, CELADON)
        self.target = Food(NUMBER_OF_CELLS, CELL_SIZE, CORAL_PINK)
        self.player_score = 0
        self.game_lost = False
        self.game_over = False

        while not self.game_over or not self.game_lost:
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

            # Fill the background with white
            self.screen.fill(EUCALYPTUS)
            self.update_game()

            self.snake.draw(self.screen)
            self.target.draw(self.screen)

            # if self.snake.head_position[0] < 0 or self.snake.head_position[0] > screen.get_width():
            #     game_over = True
            # if self.snake.head_position[1] < 0 or self.snake.head_position[1] > screen.get_height():
            #     game_over = True

            clock.tick(speed_of_snake)
            pygame.display.flip()
            if self.game_lost:
                EndScreen(self.screen)
        # Done! Time to quit.
        return

    def update_game(self):
        self.snake.move()
        self.check_collision()
        self.is_game_over()

    def check_collision(self):
        if self.target.position == self.snake.body[0]:
            self.target = Food(NUMBER_OF_CELLS, CELL_SIZE, CORAL_PINK)
            print("yam!")
            self.player_score += 1

    def is_game_over(self):
        # check if touching border:
        # left & right border
        if not 0 <= self.snake.body[0].x <= NUMBER_OF_CELLS:
            self.game_lost = True
        # top & bottom border
        if not 0 <= self.snake.body[0].y <= NUMBER_OF_CELLS:
            self.game_lost = True
        # check if touching itself:
        
    # pygame.display.quit()
    # pygame.quit()
    # quit()
