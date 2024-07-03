import pygame
from vpython import vector as Vector3


class Bullet:
    def __init__(self, rifle_tip):
        self.image = pygame.image.load('content/bullet.png')
        self.width = 3
        self.height = 7
        self.pos = Vector3(rifle_tip.x - self.width / 2, rifle_tip.y - self.height, 0)
        self.speed = 600.

    def update(self, delta_time):
        self.pos.y -= self.speed * delta_time

    def draw(self, fb):
        fb.blit(self.image, (self.pos.x, self.pos.y))

    def out_of_sight(self):
        return self.pos.y < -self.height
