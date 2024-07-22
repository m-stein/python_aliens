import numpy as np
from alien import Alien


class AlienFleet:
    def __init__(self, fb_rect, alien_bullets):
        self.fb_rect = fb_rect
        self.alien_bullets = alien_bullets
        self.spawn_timeout = None
        self.spawn_timeout = self._new_spawn_timeout()
        self.aliens = []

    def update(self, delta_time, bullets, score):
        for alien in self.aliens.copy():
            alien.update(delta_time)
            if alien.finished_maneuver():
                self.aliens.remove(alien)
            for bullet in bullets.copy():
                if bullet.collider().colliderect(alien.collider()):
                    self.aliens.remove(alien)
                    bullets.remove(bullet)
                    score.increment()

        if self.spawn_timeout > delta_time:
            self.spawn_timeout -= delta_time
        else:
            self.aliens.append(Alien(self.fb_rect, self.alien_bullets))
            self.spawn_timeout = self._new_spawn_timeout()

    def _new_spawn_timeout(self):
        return np.random.uniform(.5, 1.5)

    def draw(self, fb):
        for alien in self.aliens:
            alien.draw(fb)
