import pygame, sys


class Game(object):
    def __init__(self):
        # config
        self.tps_max = 100.0
        # initialization
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        while True:
            # obsługa zdarzeń
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tps_delta -= 1 / self.tps_max

            # rysowanie
            screen.fill((0, 0, 0))
            pygame.draw()
            pygame.display.flip()

    def tick(self):
        # input
        keys = pygame.key.get_pressed()

    def draw(self):
        pygame.draw.rect(self.screen, (0, 150, 255), pygame.Rect(10,10,50,50))

if __name__ == "__main__":
    Game()