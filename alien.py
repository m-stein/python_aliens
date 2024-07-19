import pygame
import numpy as np
import vector2 as v2
from animation import Animation


class Alien:
    def __init__(self, fb_rect):
        self.image = pygame.image.load('content/alien.png')
        self.fb_rect = fb_rect
        self.pos = np.array([100, 100])
        self.draw_collider = False
        self.speed = 400.
        self.collider_offset = np.array([5, 6])
        self.collider_size = np.array([22, 13])
        self.animation = Animation(np.array([32, 32]), 3, 0.1)

    def draw(self, fb):
        if self.draw_collider:
            pygame.draw.rect(
                fb, "red",
                pygame.Rect(int(self.pos[0] + self.collider_offset[0]),
                            int(self.pos[1] + self.collider_offset[1]),
                            int(self.collider_size[0]),
                            int(self.collider_size[1])))
        fb.blit(self.image, (self.pos[0], self.pos[1]), self.animation.frame_rectangle())

    def update(self, delta_time):
        self.animation.update(delta_time)
        direction = np.array([0, 0])

        if v2.length(direction) > 0:
            self.pos += v2.normalized(direction) * self.speed * delta_time
