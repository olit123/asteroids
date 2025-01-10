from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)
            vec2 = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            ast1.velocity = self.velocity.rotate(rand_angle) * 1.2
            ast2 = Asteroid(self.position.x, self.position.y, new_radius)
            ast2.velocity = self.velocity.rotate(-rand_angle) * 1.2
