import sys

import pygame

from Button import Button

from Text import Text

SUCCESS_COLOR = (144, 238, 144)


class EndScreen:
    def __init__(self, screen):
        self.go_to_menu_button = None
        self.restart_game = None
        pygame.init()  # initialize pygame
        pygame.display.set_caption('Snake')  # set window title
        self.screen = screen
        self.show_menu_buttons()  # adding buttons
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # occurs when x is clicked on window itself
                    running = False
                elif event.type == pygame.FULLSCREEN:
                    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                elif event.type == pygame.MOUSEBUTTONUP:  # occurs once when the mouse button is released
                    if self.go_to_menu_button.mouseover():
                        return
                    elif self.restart_game.mouseover():
                        return

            clock = pygame.time.Clock()  # creating a clock for the game
            self.show_menu_buttons()  # adding buttons
            header = Text(0, -170, self.screen, "TicTacToe", 60)
            footer = Text(0, 200, self.screen, "by shaked tamam 2024", 10)
            pygame.display.update()
        pygame.quit()
        sys.exit()

    def show_menu_buttons(self):
        self.restart_game = Button(SUCCESS_COLOR, self.screen.get_width() / 2 - 100, self.screen.get_height() / 2 - 100,
                                   200,
                                   100, "restart game", 50)
        self.go_to_menu_button = Button(SUCCESS_COLOR, self.screen.get_width() / 2 - 75, self.screen.get_height() / 2 +
                                        50, 150, 50, "go to menu", 30)
        self.go_to_menu_button.draw(self.screen, True)
        self.restart_game.draw(self.screen, True)
