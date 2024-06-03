# Import and initialize the pygame library
import sys

import pygame

from EndScreen import EndScreen
from Food import Food
from Snake import Snake
from Text import Text

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

# EATEN_FRUIT = pygame.USEREVENT + 1
# Run until the user asks to quit/ or wins or loses


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((CELL_SIZE * NUMBER_OF_CELLS, CELL_SIZE * NUMBER_OF_CELLS))
        self.snake = Snake(CELL_SIZE, CELADON)
        self.target = Food(NUMBER_OF_CELLS, CELL_SIZE, CORAL_PINK)
        self.player_score = 0
        self.game_over = False
        self.end_screen = EndScreen(self.screen)
        while not self.game_over:
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
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

            # Fill the background
            self.screen.fill(EUCALYPTUS)

            self.update_game()
            self.draw_objects()

            clock.tick(speed_of_snake)

            pygame.display.flip()

        # Done! Time to quit.
        self.end_screen.run(self)

    def draw_objects(self):
        self.snake.draw(self.screen)
        self.target.draw(self.screen)
        Text(250, 270, self.screen, f'points: {self.player_score}', 20, WHITE)

    def update_game(self):
        self.snake.move()
        self.check_collision()
        self.is_game_over()

    def check_collision(self):
        if self.target.position == self.snake.body[0]:
            self.snake.grow(self.target.position)
            self.target = Food(NUMBER_OF_CELLS, CELL_SIZE, CORAL_PINK)
            print("yam!")
            self.player_score += 1

    def is_game_over(self):
        self.is_touching_border()
        # check if touching itself:
        self.is_touching_self()

    def is_touching_self(self):
        # checking if head of snake is touching its own body
        for cell in self.snake.body[1:]:
            print(cell)
            if cell.x == self.snake.body[0].x and cell.y == self.snake.body[0].y:
                self.game_over = True

    def is_touching_border(self):
        # check if touching border:
        # left & right border
        if not 0 <= self.snake.body[0].x < NUMBER_OF_CELLS:
            self.game_over = True
        # top & bottom border
        if not 0 <= self.snake.body[0].y < NUMBER_OF_CELLS:
            self.game_over = True

    def restart(self):
        self.game_over = False
        self.player_score = 0
        Game()
    # pygame.display.quit()
    # pygame.quit()
    # quit()
