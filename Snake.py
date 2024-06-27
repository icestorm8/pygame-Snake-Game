import pygame
from pygame import Vector2


class Snake:
    def __init__(self, cell_size, color):
        self.head_position = Vector2(1, 5)
        self.cell_size = cell_size
        self.direction = Vector2(1, 0)
        self.color = color
        self.body = [self.head_position]

    # this method takes the direction as string and converts it to a vector that will be used to set the
    # direction of the snake in the game
    def change_direction(self, direction: str) -> None:
        if direction == "UP" and self.direction.y != 1:
            self.direction = Vector2(0, - 1)
        if direction == "DOWN" and self.direction.y != -1:
            self.direction = Vector2(0, 1)
        if direction == "RIGHT" and self.direction.x != -1:
            self.direction = Vector2(1, 0)
        if direction == "LEFT" and self.direction.x != -1:
            self.direction = Vector2(- 1, 0)

    # draws the snake on the screen/ board of the game
    def draw(self, screen):
        # fitting the logic to the screen/board size is done only on drawing!
        for cell in self.body:
            pygame.draw.rect(screen, self.color, pygame.Rect(cell.x * self.cell_size,
                                                             cell.y * self.cell_size,
                                                             self.cell_size, self.cell_size))

    # moves the snake body
    # when the snake doesn't yet have a body (1 cell), it moves it every loop one step in the direction set
    # since the head position & the direction are both vector of 2, it connects the x's & the y's togather so the snake
    # moves in the correct direction 1 step at a time(loop)
    # when the snake has a body (bigger than 1) we create a copy of the body without the last cell
    # than insert a new head position in the direction set and set this to be the new body
    # this way the snake looks like it's going forward when in fact we remove one cell from the end and add a cell
    # at the top, creating a new head position
    def move(self):
        if len(self.body) > 1:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
        else:
            self.body = [self.body[0] + self.direction]

    # this method increases the snakes body by 1, using the direction it's sets to.
    # since snake grows by one when it eats the food, its head is in the position of the food
    # which is the previous head position + 1 in the direction set
    def grow(self):
        # append position of fruit eaten by snake
        # self.body.append(self.body.)
        body_copy = self.body[:]  # creating a copy of the list
        # inserting the new position(where head ate the food) to the beginning of the body (as the new head)
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]  # setting the new copy of body to be the new body
