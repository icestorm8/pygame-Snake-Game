import random

import pygame
from pygame import Vector2


class Food:
    def __init__(self, cell_number, cell_size, color):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)
        print(self.position)
        self.cell_number = cell_number
        self.cell_size = cell_size
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position.x * self.cell_size,
                                                         self.position.y * self.cell_size,
                                                         self.cell_size, self.cell_size))
