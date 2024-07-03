import pygame
from random import randint


class Stars:
    def __init__(self, brightness, speed, fb_height):
        self.surface = pygame.surface.Surface((1200, 400))
        self.y_offset = 0
        self.fb_height = fb_height
        for i in range(200):
            pygame.draw.rect(
                self.surface, (brightness * 256, brightness * 256, brightness * 256),
                pygame.Rect(randint(0, self.surface.get_width()),
                            randint(0, self.surface.get_height()), 1, 1))
        self.surface.set_colorkey("black")
        self.speed = speed

    def draw(self, fb):
        fb.blit(self.surface, (0, self.y_offset))
        fb.blit(self.surface, (0, self.y_offset - self.surface.get_height()))

    def update(self, delta_time):
        self.y_offset = (self.y_offset + delta_time * self.speed) % self.surface.get_height()
