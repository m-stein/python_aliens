import pygame
import sys
from player import Player
from bullet import Bullet
from alien_fleet import AlienFleet
from stars import Stars


class Game:

    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.fb_rect = pygame.rect.Rect(0, 0, 400, 400)
        self.fb = pygame.surface.Surface((self.fb_rect.width, self.fb_rect.height))
        self.clock = pygame.time.Clock()
        self.bg_color = (10, 10, 10)
        self.player = Player(self.fb_rect)
        self.alien_fleet = AlienFleet(self.fb_rect)
        self.max_fps = 60
        self.bullets = []
        self.max_num_bullets = 3
        self.fb_blit_rect = self.fb_rect.fit(self.display.get_rect())
        self.stars_layers = [
            Stars(0.9, 60, self.fb_rect.height),
            Stars(0.7, 40, self.fb_rect.height),
            Stars(0.5, 20, self.fb_rect.height),
        ]
        pygame.display.set_caption("Aliens!")

    def run(self):
        while True:
            delta_time = self.clock.tick(self.max_fps) / 1000
            for stars in self.stars_layers:
                stars.update(delta_time)
            self.player.update(delta_time)
            self.alien_fleet.update(delta_time)
            self._update_bullets(delta_time)
            self._process_global_events()
            self._update_display()

    def _process_global_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    if len(self.bullets) < self.max_num_bullets:
                        self.bullets.append(Bullet(self.player.rifle_tip()))

    def _update_display(self):
        self.fb.fill(self.bg_color)
        for stars in self.stars_layers:
            stars.draw(self.fb)
        self.player.draw(self.fb)
        self.alien_fleet.draw(self.fb)
        for bullet in self.bullets:
            bullet.draw(self.fb)
        fb = pygame.transform.scale(self.fb, self.fb_blit_rect.size)
        self.display.blit(fb, self.fb_blit_rect.topleft)
        pygame.display.update()

    def _update_bullets(self, delta_time):
        for bullet in self.bullets.copy():
            bullet.update(delta_time)
            if bullet.out_of_sight():
                self.bullets.remove(bullet)
