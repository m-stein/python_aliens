import pygame
import numpy as np
from alien_bullet import AlienBullet
from animation import Animation
from enum import Enum


class AlienState(Enum):
    ALIVE = 0
    EXPLODING = 1
    DESTROYED = 2


class Alien:
    def __init__(self, fb_rect, alien_bullets, laser_sfx, image, explosion_img):
        self.image = image
        self.explosion_img = explosion_img
        self.state = AlienState.ALIVE
        self.fb_rect = fb_rect
        self.pos = np.array([0., -self.image.get_height()])
        self.draw_collider = False
        self.collider_offset = np.array([5, 6])
        self.collider_size = np.array([22, 13])
        self.animation = Animation(np.array([32, 32]), 3, 0.1)
        self.laser_sfx = laser_sfx
        self.explosion_animation = Animation(np.array([32, 32]), 20, 0.02, False)
        self.y_speed = np.random.uniform(20., 60.)
        self.curve_freq_factor = 1 / self.y_speed
        self.max_curve_ampl_factor = self.fb_rect.width / 2 - self.animation.frame_size[0] / 2
        self.curve_ampl_factor = np.random.uniform(self.max_curve_ampl_factor / 2, self.max_curve_ampl_factor)
        self.curve_horizontal_shift = -self.animation.frame_size[0] / 2 + self.fb_rect.width / 2
        self.curve_vertical_shift = np.random.uniform(0, 360)
        self.fire_timeout = self._new_fire_timeout()
        self.alien_bullets = alien_bullets

    @staticmethod
    def _new_fire_timeout():
        return np.random.uniform(1., 5.)

    def _draw_ship(self, fb):
        fb.blit(self.image, (self.pos[0], self.pos[1]), self.animation.frame_rectangle())

    def draw(self, fb):
        if self.draw_collider:
            pygame.draw.rect(
                fb, "red",
                pygame.Rect(int(self.pos[0] + self.collider_offset[0]),
                            int(self.pos[1] + self.collider_offset[1]),
                            int(self.collider_size[0]),
                            int(self.collider_size[1])))
        match self.state:
            case AlienState.ALIVE:
                self._draw_ship(fb)
            case AlienState.EXPLODING:
                if self.explosion_animation.frame < 15:
                    self._draw_ship(fb)
                fb.blit(self.explosion_img, (self.pos[0] + 1, self.pos[1]), self.explosion_animation.frame_rectangle())
            case AlienState.DESTROYED:
                pass

    def _fire_bullet(self):
        self.alien_bullets.append(AlienBullet(self.collider().midbottom, self.fb_rect.height))
        self.laser_sfx.play()

    def update(self, delta_time):
        match self.state:
            case AlienState.ALIVE:
                if self.fire_timeout > delta_time:
                    self.fire_timeout -= delta_time
                else:
                    self._fire_bullet()
                    self.fire_timeout = self._new_fire_timeout()
                self.animation.update(delta_time)
                self.pos[1] = float(float(self.pos[1]) + self.y_speed * delta_time)
                self.pos[0] = (
                        self.curve_ampl_factor *
                        np.sin((self.pos[1] - self.curve_vertical_shift) * self.curve_freq_factor) +
                        self.curve_horizontal_shift)
            case AlienState.EXPLODING:
                if self.explosion_animation.frame < 15:
                    self.animation.update(delta_time)
                self.explosion_animation.update(delta_time)
                if self.explosion_animation.finished:
                    self.state = AlienState.DESTROYED
            case AlienState.DESTROYED:
                pass

    def finished_maneuver(self):
        return self.pos[1] > self.fb_rect.height

    def collider(self):
        return pygame.Rect(int(self.pos[0] + self.collider_offset[0]),
                           int(self.pos[1] + self.collider_offset[1]),
                           int(self.collider_size[0]),
                           int(self.collider_size[1]))

    def explode(self):
        self.state = AlienState.EXPLODING

    def vulnerable(self):
        return self.state == AlienState.ALIVE

    def destroyed(self):
        return self.state == AlienState.DESTROYED
