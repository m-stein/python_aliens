from alien import Alien


class AlienFleet:
    def __init__(self, fb_rect):
        self.fb_rect = fb_rect
        self.spawn_period = 2.
        self.spawn_time = 0.
        self.aliens = []

    def update(self, delta_time):
        for alien in self.aliens.copy():
            alien.update(delta_time)
            if alien.finished_maneuver():
                self.aliens.remove(alien)
        self.spawn_time += delta_time
        if self.spawn_time > self.spawn_period:
            self.aliens.append(Alien(self.fb_rect))
            self.spawn_time %= self.spawn_period

    def draw(self, fb):
        for alien in self.aliens:
            alien.draw(fb)
