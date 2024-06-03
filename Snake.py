import pygame


class Snake:
    def __init__(self, cell_size, color, direction: str = "RIGHT", head_position=None):
        if head_position is None:
            head_position = [100, 50]
        self.direction = direction
        self.head_position = head_position
        # self.body = [head_position, [head_position[0]-cell_size, head_position[1]], [head_position[0]-cell_size*2,
        #                                                                              head_position[1]],
        #              [head_position[0] - cell_size*3, head_position[1]]]
        self.color = color
        self.cell_size = cell_size
        self.body_size = 4
        self.body = self.generate_body()

    def change_direction(self, direction: str):
        self.direction = direction
        for cell in self.body:
            if direction == "RIGHT":
                cell[0] += self.cell_size
            if direction == "LEFT":
                cell[0] -= self.cell_size
            if direction == "UP":
                cell[1] -= self.cell_size
            if direction == "DOWN":
                cell[1] += self.cell_size

    def draw_snake(self, screen):
        for cell in range(self.body_size):
            pygame.draw.rect(screen, self.color, pygame.Rect(self.head_position[0] - self.cell_size * cell,
                                                             self.head_position[1],
                                                             self.cell_size, self.cell_size))

    def generate_body(self) -> list:
        temp = list()
        temp.append(self.head_position)
        for index in range(1, self.body_size):
            temp.append([self.head_position[0] - self.cell_size * index, self.head_position[1]])
        return temp
