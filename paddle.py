import pygame

class Paddle():
    def __init__(self, position : tuple[int, int], size : tuple[int, int]) -> None:
        """
        Initialises a puddle object
        
        Arguments:
        - position: the position of the puddle (x, y)
        - size: the size of the puddle (width, height)
        
        """
        
        self.rect = pygame.Rect(position, size)
        
        
    
    def move(self) -> None:
        pass
    
    def get_position(self) -> None:
        pass
    
    