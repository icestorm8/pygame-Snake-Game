import pygame

from Button import Button

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
SUCCESS_COLOR = (144, 238, 144)
DANGER_COLOR = (240, 144, 144)
BACKGROUND_COLOR = (255, 255, 255)


class Menu:
    def __init__(self):
        self.start_button = None
        self.exit_button = None
        pygame.init()  # initialize pygame
        pygame.display.set_caption('Tic Tac Toe')  # set window title
        self.screen = pygame.display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH])  # creating a window for the game
        self.screen.fill(BACKGROUND_COLOR)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # occurs when x is clicked on window itself
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:  # occurs once when the mouse button is released
                    if self.start_button.mouseover():
                        print(self.start_button.text)
                    if self.exit_button.mouseover():
                        print(self.exit_button.text)
                        running = False
            clock = pygame.time.Clock()  # creating a clock for the game
            self.show_menu_buttons()  # adding buttons

            pygame.display.update()
        pygame.quit()

    # takes care of the menu buttons
    def show_menu_buttons(self):
        self.start_button = Button(SUCCESS_COLOR, 150, 150, 200, 100, "START", 50)
        self.exit_button = Button(DANGER_COLOR, 170, 280, 150, 50, "EXIT", 30)
        self.start_button.draw(self.screen, True)
        self.exit_button.draw(self.screen, True)
