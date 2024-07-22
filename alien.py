import pygame
import numpy as np
import vector2 as v2
from animation import Animation


class Alien:
    def __init__(self, fb_rect):
        self.image = pygame.image.load('content/alien.png').convert_alpha()
        self.fb_rect = fb_rect
        self.pos = np.array([0., -self.image.get_height()])
        self.draw_collider = False
        self.collider_offset = np.array([5, 6])
        self.collider_size = np.array([22, 13])
        self.animation = Animation(np.array([32, 32]), 3, 0.1)
        self.y_speed = float(20)
        self.curve_freq_factor = 1 / self.y_speed
        self.curve_ampl_factor = self.fb_rect.width / 2 - self.animation.frame_size[0] / 2
        self.curve_horizontal_shift = -self.animation.frame_size[0] / 2 + self.fb_rect.width / 2
        self.curve_vertical_shift = 0

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
        self.pos[1] = float(float(self.pos[1]) + self.y_speed * delta_time)
        self.pos[0] = self.curve_ampl_factor * np.sin((self.pos[1] - self.curve_vertical_shift) * self.curve_freq_factor) + self.curve_horizontal_shift

    def finished_maneuver(self):
        return self.pos[1] > self.fb_rect.height

    def collider(self):
        return pygame.Rect(int(self.pos[0] + self.collider_offset[0]),
                           int(self.pos[1] + self.collider_offset[1]),
                           int(self.collider_size[0]),
                           int(self.collider_size[1]))