# Import and initialize the pygame library
import pygame

pygame.init()

HEIGHT, WIDTH = 500, 500
# Set up the drawing window

pygame.display.set_caption("Tic Tac Toe")


# Run until the user asks to quit


class Game:
    def __init__(self, screen, mode: bool):
        mode: bool = mode  # true for 2 player, false for 1 player w/ bot
        screen = screen
        running = True
        while running:
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        # get back to menu on esc key press
                        return

            # Fill the background with white
            screen.fill((255, 255, 255))

            # Draw a solid blue circle in the center
            pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

            # Flip the display
            pygame.display.flip()

        # Done! Time to quit.
        pygame.quit()
    # pygame.display.quit()
    # pygame.quit()
    # quit()
