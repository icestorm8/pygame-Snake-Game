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


# EATEN_FRUIT = pygame.USEREVENT + 1
# Run until the user asks to quit/ or wins or loses


class Game:
    def __init__(self, fps: int):
        self.speed_of_snake = fps
        self.GAME_OVER = pygame.USEREVENT + 1
        self.EATEN_FRUIT = pygame.USEREVENT + 2
        self.screen = pygame.display.set_mode((CELL_SIZE * NUMBER_OF_CELLS, CELL_SIZE * NUMBER_OF_CELLS))
        self.__snake = Snake(CELL_SIZE, CELADON)
        self.__target = Food(NUMBER_OF_CELLS, CELL_SIZE)
        self.player_score = 0
        self.running = True
        self.end_screen = EndScreen(self.screen)
        while self.running:
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
                        self.__snake.change_direction('UP')
                    if event.key == pygame.K_DOWN:
                        self.__snake.change_direction('DOWN')
                    if event.key == pygame.K_LEFT:
                        self.__snake.change_direction('LEFT')
                    if event.key == pygame.K_RIGHT:
                        self.__snake.change_direction("RIGHT")
                if event.type == self.GAME_OVER:
                    print("game is over!!!")
                    self.running = False
                if event.type == self.EATEN_FRUIT:
                    print("yam!")
                    self.player_score += 1
                    self.__snake.grow()
                    self.__target = Food(NUMBER_OF_CELLS, CELL_SIZE)
            # Fill the background
            self.screen.fill(EUCALYPTUS)

            self.update_game()
            self.__draw_objects()

            clock.tick(self.speed_of_snake)

            pygame.display.flip()

        # Done! Time to quit.
        self.end_screen.run(self)

    # this method is a private method used to draw the snake & the target on the board
    # it also prints the text of the player score on the screen
    def __draw_objects(self):
        self.__snake.draw(self.screen)
        self.__target.draw(self.screen)
        Text(250, 270, self.screen, f'points: {self.player_score}', 20, WHITE)

    # this method is used to check if the game is over, if there was a collision (food eaten by snake) and for
    # moving the snake forward in each loop
    # this method is using other private method of the class to make it more readable (this is where events are posted
    # so the game loop could react to the events triggerd)
    def update_game(self):
        self.__snake.move()
        if self.__check_collision():
            pygame.event.post(pygame.event.Event(self.EATEN_FRUIT))
        if self.__is_game_over():
            pygame.event.post(pygame.event.Event(self.GAME_OVER))

    # this is a private method that checks if the snakes head (body[0]) touched the food by comparing their positions
    # (both are vectors). if the position is equals the snake eats the food
    def __check_collision(self) -> bool:
        return self.__target.position == self.__snake.body[0]

    # this method checks if game's over using private methods
    def __is_game_over(self) -> bool:
        return self.__is_touching_border() or self.__is_touching_self()

    # this method checks if the snake's head is touching anywhere on the snakes body
    def __is_touching_self(self) -> bool:
        # checking if head of snake is touching its own body
        for cell in self.__snake.body[1:]:
            if cell.x == self.__snake.body[0].x and cell.y == self.__snake.body[0].y:
                return True
        return False

    # this method checks if snake's body touched any of the borders by checking if snake's body is in
    # range of cells on board
    def __is_touching_border(self) -> bool:
        # check if touching border:
        # left & right border
        if not 0 <= self.__snake.body[0].x < NUMBER_OF_CELLS:
            return True
        # top & bottom border
        if not 0 <= self.__snake.body[0].y < NUMBER_OF_CELLS:
            return True
        return False

    # this method restarts the game by resting it to its default parameters
    def restart(self) -> None:
        self.running = True
        self.player_score = 0
        Game(self.speed_of_snake)
    # pygame.display.quit()
    # pygame.quit()
    # quit()
