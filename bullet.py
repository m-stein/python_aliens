import pygame
import numpy as np


class Bullet:
    def __init__(self, rifle_tip):
        self.image = pygame.image.load('content/bullet.png')
        self.width = 3
        self.height = 7
        self.pos = np.array([rifle_tip[0] - self.width / 2, rifle_tip[1] - self.height])
        self.speed = 600.

    def update(self, delta_time):
        self.pos[1] -= self.speed * delta_time

    def draw(self, fb):
        fb.blit(self.image, (self.pos[0], self.pos[1]))

    def out_of_sight(self):
        return self.pos[1] < -self.height
