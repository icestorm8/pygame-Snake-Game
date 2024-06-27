import sys

import pygame

from Button import Button
from Game import Game
from Text import Text

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
SUCCESS_COLOR = (144, 238, 144)
DANGER_COLOR = (240, 144, 144)
BACKGROUND_COLOR = (255, 255, 255)
LIGHT_COLOR = (240, 240, 240)
FPS_EASY = 5
FPS_HARD = 15


class Menu:
    def __init__(self):
        self.start_button = None
        self.exit_button = None
        self.easy_button = None
        self.hard_button = None
        pygame.init()  # initialize pygame
        pygame.display.set_caption('Snake game')  # set window title
        self.screen = pygame.display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH], pygame.RESIZABLE)  # creating a window
        self.fps = FPS_EASY  # easy by default
        # for the game

        running = True
        while running:
            self.screen.fill(BACKGROUND_COLOR)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # occurs when x is clicked on window itself
                    running = False
                if event.type == pygame.FULLSCREEN:
                    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                if event.type == pygame.MOUSEBUTTONUP:  # occurs once when the mouse button is released
                    if self.start_button.mouseover():
                        print(self.start_button.text)
                        self.game = Game(self.fps)
                    elif self.exit_button.mouseover():
                        print(self.exit_button.text)
                        running = False
                    elif self.easy_button.mouseover():
                        self.fps = FPS_EASY
                        print("easy")
                    elif self.hard_button.mouseover():
                        self.fps = FPS_HARD
                        print("hard")

            clock = pygame.time.Clock()  # creating a clock for the game
            self.show_menu_buttons()  # adding buttons
            # text of the menu screen
            header = Text(0, -180, self.screen, "Snake game", 60)
            level = Text(0, -130, self.screen, f"level: {'easy' if self.fps == FPS_EASY else 'hard'}")
            footer = Text(0, 200, self.screen, "by shaked tamam 2024", 10)
            pygame.display.update()
        pygame.quit()
        sys.exit()

    # displays the menu buttons (start, exit & levels on the screen)
    def show_menu_buttons(self):
        self.start_button = Button(SUCCESS_COLOR, self.screen.get_width() / 2 - 100, self.screen.get_height() / 2 - 100,
                                   200,
                                   100, "START", 50)
        self.exit_button = Button(DANGER_COLOR, self.screen.get_width() / 2 - 75, self.screen.get_height() / 2 + 50,
                                  150, 50,
                                  "EXIT", 30)
        self.easy_button = Button(LIGHT_COLOR, self.screen.get_width() / 2 - 150, self.screen.get_height() / 2 + 125,
                                  150, 50,
                                  "EASY", 30)
        self.hard_button = Button(LIGHT_COLOR, self.screen.get_width() / 2 + 30, self.screen.get_height() / 2 + 125,
                                  150, 50,
                                  "HARD", 30)
        self.start_button.draw(self.screen, True)
        self.exit_button.draw(self.screen, True)
        self.easy_button.draw(self.screen, True)
        self.hard_button.draw(self.screen, True)
