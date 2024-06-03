import pygame
from pygame import Vector2


class Snake:
    def __init__(self, cell_size, color):
        self.head_position = Vector2(1, 5)
        self.cell_size = cell_size
        self.direction = Vector2(1, 0)
        self.color = color
        self.body = [self.head_position]

    def change_direction(self, direction: str) -> None:
        if direction == "UP" and self.direction.y != 1:
            self.direction = Vector2(0, - 1)
        if direction == "DOWN" and self.direction.y != -1:
            self.direction = Vector2(0, 1)
        if direction == "RIGHT" and self.direction.x != -1:
            self.direction = Vector2(1, 0)
        if direction == "LEFT" and self.direction.x != -1:
            self.direction = Vector2(- 1, 0)

    def draw(self, screen):
        # fitting the logic to the screen/board size is done only on drawing!
        for cell in self.body:
            pygame.draw.rect(screen, self.color, pygame.Rect(cell.x * self.cell_size,
                                                             cell.y * self.cell_size,
                                                             self.cell_size, self.cell_size))

    def move(self):
        if len(self.body) > 1:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
        else:
            self.body = [self.body[0] + self.direction]

    def grow(self, fruit_pos):
        # append position of fruit eaten by snake
        # self.body.append(self.body.)
        body_copy = self.body[:]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]


