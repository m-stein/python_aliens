import pygame
import numpy as np


class Bullet:
    def __init__(self, rifle_tip):
        self.image = pygame.image.load('content/bullet.png').convert()
        self.width = 3
        self.height = 7
        self.pos = np.array([rifle_tip[0] - self.width / 2, rifle_tip[1] - self.height])
        self.speed = 600.
        self.collider_offset = np.array([0, 0])
        self.collider_size = np.array([3, 7])

    def update(self, delta_time):
        self.pos[1] -= self.speed * delta_time

    def draw(self, fb):
        fb.blit(self.image, (self.pos[0], self.pos[1]))

    def out_of_sight(self):
        return self.pos[1] < -self.height

    def collider(self):
        return pygame.Rect(int(self.pos[0] + self.collider_offset[0]),
                           int(self.pos[1] + self.collider_offset[1]),
                           int(self.collider_size[0]),
                           int(self.collider_size[1]))
