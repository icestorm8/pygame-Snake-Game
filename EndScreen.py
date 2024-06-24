import sys

import pygame

from Button import Button

from Text import Text

SUCCESS_COLOR = (144, 238, 144)
PUSH_ME_COLOR = (238, 144, 144)


class EndScreen:
    def __init__(self, screen):
        self.color = SUCCESS_COLOR
        self.did2secondsPass = False
        self.wait_for_click = pygame.event.custom_type()
        self.go_to_menu_button = None
        self.restart_game = None
        self.points = 0
        pygame.init()  # initialize pygame
        pygame.display.set_caption('Snake game')  # set window title
        self.screen = screen

    def run(self, finished_game):
        pygame.time.set_timer(self.wait_for_click, 300)
        running = True
        while running:
            self.points = finished_game.player_score
            self.show_menu_buttons()  # adding buttons
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # occurs when x is clicked on window itself
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.FULLSCREEN:
                    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                if event.type == pygame.MOUSEBUTTONUP:  # occurs once when the mouse button is released
                    if self.go_to_menu_button.mouseover():
                        pygame.time.set_timer(self.wait_for_click, 0)
                        running = False
                        return
                    if self.restart_game.mouseover():
                        pygame.time.set_timer(self.wait_for_click, 0)
                        running = False
                        finished_game.restart()
                if event.type == self.wait_for_click:
                    print("im waiting")
                    self.did2secondsPass = not self.did2secondsPass
                    if self.did2secondsPass:
                        self.color = PUSH_ME_COLOR
                    else:
                        self.color = SUCCESS_COLOR

            clock = pygame.time.Clock()  # creating a clock for the game

            pygame.display.update()

    def show_menu_buttons(self):
        self.restart_game = Button(self.color, self.screen.get_width() / 2 - 130,
                                   self.screen.get_height() / 2 - 100,
                                   260,
                                   100, "restart game", 50)
        self.go_to_menu_button = Button(SUCCESS_COLOR, self.screen.get_width() / 2 - 75, self.screen.get_height() / 2 +
                                        50, 150, 50, "go to menu", 30)
        self.go_to_menu_button.draw(self.screen, True)
        self.restart_game.draw(self.screen, True)
        Text(0, -200, self.screen, text=f"your score: {self.points}", color=(255, 255, 255), font_size=50)
