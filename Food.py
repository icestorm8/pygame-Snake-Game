import random

import pygame
from pygame import Vector2

COLORS = [(248, 131, 121), (252, 245, 95), (250, 160, 160), (233, 116, 81), (216, 191, 216), (224, 176, 255),
          (250, 200, 152)]


class Food:
    def __init__(self, cell_number, cell_size):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)
        print(self.position)
        self.cell_number = cell_number
        self.cell_size = cell_size
        self.color = random.choice(COLORS)

    # food is created each time last food item was eaten. so when we create a new food item, we set its position to be
    # anywhere random on the board by using a random x & y values in range. the color is set randomly too using the
    # color array set as constant
    # this method draws the fruit/food item on the board, using the screen received from the game
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position.x * self.cell_size,
                                                         self.position.y * self.cell_size,
                                                         self.cell_size, self.cell_size))
