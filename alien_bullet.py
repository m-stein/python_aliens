import pygame
import numpy as np
from animation import Animation


class AlienBullet:
    def __init__(self, rifle_tip, fb_height):
        self.image = pygame.image.load('content/alien_bullet.png').convert_alpha()
        self.width = 8
        self.height = 8
        self.fb_height = fb_height
        self.pos = np.array([rifle_tip[0] - self.width / 2, rifle_tip[1] - self.height])
        self.speed = 200.
        self.collider_offset = np.array([1, 1])
        self.collider_size = np.array([6, 6])
        self.animation = Animation(np.array([8, 8]), 6, 0.1)

    def update(self, delta_time):
        self.animation.update(delta_time)
        self.pos[1] += self.speed * delta_time

    def draw(self, fb):
        fb.blit(self.image, (self.pos[0], self.pos[1]), self.animation.frame_rectangle())

    def out_of_sight(self):
        return self.pos[1] > self.fb_height

    def collider(self):
        return pygame.Rect(int(self.pos[0] + self.collider_offset[0]),
                           int(self.pos[1] + self.collider_offset[1]),
                           int(self.collider_size[0]),
                           int(self.collider_size[1]))
