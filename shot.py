from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)  # Initialize with zero velocity
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS)
    
    def update(self, dt):
        self.position += self.velocity * dt