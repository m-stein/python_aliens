import pygame
import sys
from player import Player
from bullet import Bullet
from alien import Alien


class Game:

    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.fb_rect = pygame.rect.Rect(0, 0, 400, 400)
        self.clock = pygame.time.Clock()
        self.bg_color = (25, 25, 25)
        self.player = Player(self.fb_rect)
        self.alien = Alien(self.fb_rect)
        self.max_fps = 60
        self.bullets = []
        self.max_num_bullets = 3
        self.fb_blit_rect = self.fb_rect.fit(self.display.get_rect())
        pygame.display.set_caption("Aliens!")

    def run(self):
        while True:
            delta_time = self.clock.tick(self.max_fps) / 1000
            self.player.update(delta_time)
            self.alien.update(delta_time)
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
        fb = pygame.surface.Surface((self.fb_rect.width, self.fb_rect.height))
        fb.fill(self.bg_color)
        self.player.draw(fb)
        self.alien.draw(fb)
        for bullet in self.bullets:
            bullet.draw(fb)
        fb = pygame.transform.scale(fb, self.fb_blit_rect.size)
        self.display.blit(fb, self.fb_blit_rect.topleft)
        pygame.display.update()

    def _update_bullets(self, delta_time):
        for bullet in self.bullets.copy():
            bullet.update(delta_time)
            if bullet.out_of_sight():
                self.bullets.remove(bullet)
