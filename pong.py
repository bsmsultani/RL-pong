import pygame
import gymnasium as gym
from gymnasium import spaces
import numpy as np


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color = (255, 255, 255), width = 10, height = 60):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

class Ball(pygame.sprite.Sprite):
    def __init__(self, color = (255, 255, 255), radius = 10):
        super().__init__()
        self.image = pygame.Surface([radius * 2, radius * 2])
        self.image.fill(color)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect()


class CustomPongEnv(gym.Env):
    def __init__(
        self,
        width = 640,
        height = 480
    ):
        super().__init__()
        
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(low=0, high=255, shape=(210, 160, 3), dtype=np.uint8)
        
        pygame.init()
        pygame.display.set_caption('Pong')
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill((0, 0, 0))
        
        self.clock = pygame.time.Clock()
        
        self.paddle1 = Paddle()
        self.paddle1.rect.x = 20
        self.paddle1.rect.y = 210
        self.paddle2 = Paddle()
        self.paddle2.rect.x = 610
        self.paddle2.rect.y = 210
        self.ball = Ball()
        self.ball.rect.x = 320
        self.ball.rect.y = 240
        
        
        
    def step(self):
        pass
        
    
    def reset(self):
        pass
    
    def render(self):
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            self.screen.blit(self.paddle1.image, self.paddle1.rect)
            self.screen.blit(self.paddle2.image, self.paddle2.rect)
            self.screen.blit(self.ball.image, self.ball.rect)
            pygame.display.flip()
            self.clock.tick(60)
        
    
    def close(self):
        pass
    
env = CustomPongEnv()
env.render()