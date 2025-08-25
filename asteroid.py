import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 5
        
        angle = random.uniform(20, 50)
        random_angle = self.velocity.rotate(angle)
        random_angle_neg = self.velocity.rotate(-angle)

        newRadius = self.radius - ASTEROID_MIN_RADIUS

        asteroidOne = Asteroid(self.position[0], self.position[1], newRadius)
        asteroidTwo = Asteroid(self.position[0], self.position[1], newRadius)

        asteroidOne.velocity = random_angle * 1.2
        asteroidTwo.velocity = random_angle_neg * 1.2

        if self.radius >= ASTEROID_MAX_RADIUS:
            return 1
        
        return 3