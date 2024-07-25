import numpy as np
import pygame
from alien import Alien


class AlienFleet:
    def __init__(self, fb_rect, alien_bullets, accuracy_bonus):
        self.fb_rect = fb_rect
        self.alien_bullets = alien_bullets
        self.accuracy_bonus = accuracy_bonus
        self.spawn_timeout = None
        self.spawn_timeout = self._new_spawn_timeout()
        self.explosion_sfx = pygame.mixer.Sound("sfx/alien_explosion.wav")
        self.explosion_sfx.set_volume(0.2)
        self.aliens = []
        self.laser_sfx = pygame.mixer.Sound("sfx/alien_laser.wav")
        self.laser_sfx.set_volume(0.1)
        self.alien_image = pygame.image.load('images/alien.png').convert_alpha()
        self.explosion_img = pygame.image.load('images/explosion.png').convert_alpha()

    def update(self, delta_time, bullets, score):
        for alien in self.aliens.copy():
            alien.update(delta_time)
            if alien.finished_maneuver() or alien.destroyed():
                self.aliens.remove(alien)
            if alien.vulnerable():
                for bullet in bullets.copy():
                    if bullet.collider().colliderect(alien.collider()):
                        alien.explode()
                        self.explosion_sfx.play()
                        bullets.remove(bullet)
                        score.increment_by(5 + self.accuracy_bonus[0])
                        self.accuracy_bonus[0] += 2

        if self.spawn_timeout > delta_time:
            self.spawn_timeout -= delta_time
        else:
            self.aliens.append(Alien(self.fb_rect, self.alien_bullets, self.laser_sfx, self.alien_image, self.explosion_img))
            self.spawn_timeout = self._new_spawn_timeout()

    @staticmethod
    def _new_spawn_timeout():
        return np.random.uniform(.5, 1.5)

    def draw(self, fb):
        for alien in self.aliens:
            alien.draw(fb)
