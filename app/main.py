import pygame
from app.game_state import GameState


def main():

    # pygame setup
    PLAYER_START_X, PLAYER_START_Y = 350, 10
    SCREEN_WIDTH, SCREEN_HEIGHT = 700, 400
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    gs = GameState(screen, (PLAYER_START_X, PLAYER_START_Y))

    running = True

    while running:

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        gs.update(keys, dt)
        gs.draw()

        pygame.display.flip()


pygame.quit()

if __name__ == "__main__":
    main()
