import pygame


class Button:
    def __init__(self, color, x, y, width: int, height: int, text: str = '', font_size: int = 30):
        self.rect = None
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text: str = text
        self.font_size: int = font_size

    def draw(self, window, outline=None):
        if outline:
            self.rect = pygame.draw.rect(window, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        self.rect = pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comics', self.font_size)
            text = font.render(self.text, 1, (0, 0, 0))
            window.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 -
                                                                                           text.get_height() / 2)))

    def mouseover(self):
        # this function will return true if mouse is on the button
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        return False
