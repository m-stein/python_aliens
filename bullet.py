import pygame
from vpython import vector as Vector3


class Bullet:
    def __init__(self, screen, rifle_tip):
        self.image = pygame.image.load('content/bullet.png')
        self.screen = screen
        self.image_scale = 2
        self.width = 3
        self.height = 7
        self.pos = Vector3(rifle_tip.x - self.width / 2 * self.image_scale,
                           rifle_tip.y - self.height * self.image_scale, 0)
        self.speed = 800.

    def update(self, delta_time):
        self.pos.y -= self.speed * delta_time

    def draw(self):
        """Draw players visual to the screen."""
        self.screen.blit(self.image, (self.pos.x, self.pos.y))

    def out_of_screen(self):
        return self.pos.y < -self.height
