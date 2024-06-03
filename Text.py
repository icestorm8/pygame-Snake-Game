import pygame


class Text:
    def __init__(self, x, y, screen, text: str, font_size: int = 30, color=(0, 0, 0)):
        font = pygame.font.SysFont('Comic Sans MS', font_size)
        text_surface = font.render(text, False, color)
        screen.blit(text_surface, (screen.get_width() / 2 - text_surface.get_width() / 2 + x, screen.get_height() / 2 -
                                   text_surface.get_height() / 2 + y))

    #  when getting 0 for x - sets the text horizontally centered, otherwise - goes to left or right based on x value
    #  when getting 0 for y - sets the text vertically centered, otherwise - goes to up or down based on y value
