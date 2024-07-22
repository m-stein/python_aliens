import pygame
from player import Player
from alien_fleet import AlienFleet
from stars import Stars
from score import Score
from bullet import Bullet


class LevelScene:
    def __init__(self, fb_rect):
        self.bg_color = (10, 10, 10)
        self.score = Score()
        self.player = Player(fb_rect)
        self.alien_fleet = AlienFleet(fb_rect)
        self.bullets = []
        self.max_num_bullets = 3
        self.stars_layers = [
            Stars(0.9, 60, fb_rect.height),
            Stars(0.7, 40, fb_rect.height),
            Stars(0.5, 20, fb_rect.height),
        ]

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if len(self.bullets) < self.max_num_bullets:
                self.bullets.append(Bullet(self.player.rifle_tip()))

    def update(self, delta_time):
        for stars in self.stars_layers:
            stars.update(delta_time)
        self.player.update(delta_time)
        self._update_bullets(delta_time)
        self.alien_fleet.update(delta_time, self.bullets, self.score)
        self.score.update(delta_time)

    def _update_bullets(self, delta_time):
        for bullet in self.bullets.copy():
            bullet.update(delta_time)
            if bullet.out_of_sight():
                self.bullets.remove(bullet)

    def draw(self, fb):
        fb.fill(self.bg_color)
        for stars in self.stars_layers:
            stars.draw(fb)
        self.player.draw(fb)
        self.alien_fleet.draw(fb)
        for bullet in self.bullets:
            bullet.draw(fb)
        self.score.draw(fb)
