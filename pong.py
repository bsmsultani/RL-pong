import pygame
from ball import Ball
from paddle import Paddle

class Pong():
    def __init__(self, width: int, height: int) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()
        self.ball = Ball((width / 2, height / 2), (width / 80, height / 80), (5, 5))
        self.left_paddle = Paddle((10, height / 2 ), (width / 100, height / 10))
        self.right_paddle = Paddle((width - 10, height / 2), (width / 100, height / 10))

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.screen.fill((0, 0, 0))
            self.ball.move()
            pygame.draw.rect(self.screen, (255, 255, 255), self.ball.rect)
            pygame.draw.rect(self.screen, (255, 255, 255), self.left_paddle)
            pygame.draw.rect(self.screen, (255, 255, 255), self.right_paddle)
            pygame.display.flip()
            self.clock.tick(60)

    def reset(self) -> None:
        pass

if __name__ == "__main__":
    pong = Pong(800, 600)
    pong.run()
