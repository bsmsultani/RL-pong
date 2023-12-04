import pygame

class Ball():
    def __init__(self, initial_position: tuple[int, int], size: tuple[int, int], speed: tuple[int, int]) -> None:
        """
        Initializes a Ball object.

        Parameters:
        - initial_position: A tuple representing the initial position of the ball (x, y).
        - size: A tuple representing the size of the ball (width, height).
        - speed: A tuple representing the speed of the ball (x_speed, y_speed).
        """

        self.position = initial_position
        self.size = size
        self.rect = pygame.Rect(self.position, self.size)
        self.speed = speed

    def move(self) -> None:
        """
        Moves the ball according to input from the user.

        Parameters:

        """
        keys = pygame.key.get_pressed()

        # Check for arrow key input
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed[0]
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed[0]
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed[1]
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed[1]
