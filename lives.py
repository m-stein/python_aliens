import pygame
import numpy as np


class Lives:
    def __init__(self, fb_rect):
        self.max_count = 3
        self.count = self.max_count
        self.image = pygame.image.load('content/player.png').convert_alpha()
        self.image_src_rect = pygame.rect.Rect(0, 0, 32, 32)
        self.pos = np.array([float(fb_rect.width - 10), float(10)])

    def update(self, delta_time):
        pass

    def draw(self, fb):
        for i in range(self.count):
            fb.blit(self.image,
                    (self.pos[0] - i * self.image_src_rect.width - self.image_src_rect.width, self.pos[1]),
                    self.image_src_rect)

    def consume_a_life(self):
        if self.count > 0:
            self.count -= 1
            return True
        else:
            return False
