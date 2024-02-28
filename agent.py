from pong import CustomPongEnv

class PongAgent():
    def __init__(self, env : CustomPongEnv):
        self.env = env
    
    def learn(self, state : tuple) -> None:
        pass
    
    def train(self, epsides : int ) -> None:
        pass
    
