import pygame
import numpy as np
from alien_bullet import AlienBullet
from animation import Animation


class Alien:
    def __init__(self, fb_rect, alien_bullets):
        self.image = pygame.image.load('content/alien.png').convert_alpha()
        self.fb_rect = fb_rect
        self.pos = np.array([0., -self.image.get_height()])
        self.draw_collider = False
        self.collider_offset = np.array([5, 6])
        self.collider_size = np.array([22, 13])
        self.animation = Animation(np.array([32, 32]), 3, 0.1)
        self.y_speed = np.random.uniform(20.,60.)
        self.curve_freq_factor = 1 / self.y_speed
        self.max_curve_ampl_factor = self.fb_rect.width / 2 - self.animation.frame_size[0] / 2
        self.curve_ampl_factor = np.random.uniform(self.max_curve_ampl_factor / 2, self.max_curve_ampl_factor)
        self.curve_horizontal_shift = -self.animation.frame_size[0] / 2 + self.fb_rect.width / 2
        self.curve_vertical_shift = np.random.uniform(0,360)
        self.max_fire_timeout = 5.
        self.min_fire_timeout = 1.
        self.fire_timeout = np.random.uniform(self.min_fire_timeout, self.max_fire_timeout)
        self.alien_bullets = alien_bullets

    def draw(self, fb):
        if self.draw_collider:
            pygame.draw.rect(
                fb, "red",
                pygame.Rect(int(self.pos[0] + self.collider_offset[0]),
                            int(self.pos[1] + self.collider_offset[1]),
                            int(self.collider_size[0]),
                            int(self.collider_size[1])))
        fb.blit(self.image, (self.pos[0], self.pos[1]), self.animation.frame_rectangle())

    def _fire_bullet(self):
        self.alien_bullets.append(AlienBullet(self.collider().midbottom, self.fb_rect.height))

    def update(self, delta_time):
        if self.fire_timeout > delta_time:
            self.fire_timeout -= delta_time
        else:
            self.fire_timeout = np.random.uniform(self.min_fire_timeout, self.max_fire_timeout)
            self._fire_bullet()
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