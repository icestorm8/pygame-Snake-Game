import pygame
from pygame import Vector2


class Snake:
    def __init__(self, cell_size, color, direction: str = "RIGHT"):
        self.head_position = Vector2(1, 5)
        self.cell_size = cell_size
        self.direction = self.change_direction(direction)
        self.color = color
        self.body_size = 4
        self.body = [self.head_position, Vector2(self.head_position.x + 1, self.head_position.y),
                     Vector2(self.head_position.x + 2, self.head_position.y)]

    def change_direction(self, direction: str) -> Vector2:
        direction_vector = Vector2()
        if direction == "UP":
            direction_vector = Vector2(0, - 1)
        if direction == "DOWN":
            direction_vector = Vector2(0, 1)
        if direction == "RIGHT":
            direction_vector = Vector2(1, 0)
        if direction == "LEFT":
            direction_vector = Vector2(- 1, 0)
        self.direction = direction_vector
        return direction_vector

    def draw(self, screen):
        # fitting the logic to the screen/board size is done only on drawing!
        for cell in self.body:
            pygame.draw.rect(screen, self.color, pygame.Rect(cell.x * self.cell_size,
                                                             cell.y * self.cell_size,
                                                             self.cell_size, self.cell_size))

    def move(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]
