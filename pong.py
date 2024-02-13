import gym
import pygame

class CustomPongEnv(gym.Env):
    def __init__(self):
        super(CustomPongEnv, self).__init__()
        
        self.observation_space = None
        self.action_space = None
        
        
    def step(self):
        pass
    
    def reset(self):
        pass
    
    def render(self):
        pass
    
    def close(self):
        pass
    
    
    