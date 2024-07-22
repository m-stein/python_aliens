from alien import Alien


class AlienFleet:
    def __init__(self, fb_rect):
        self.fb_rect = fb_rect
        self.spawn_period = 1.
        self.spawn_time = 0.
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

        self.spawn_time += delta_time
        if self.spawn_time > self.spawn_period:
            self.aliens.append(Alien(self.fb_rect))
            self.spawn_time %= self.spawn_period

    def draw(self, fb):
        for alien in self.aliens:
            alien.draw(fb)
