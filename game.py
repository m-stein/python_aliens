import pygame
import sys
from player import Player
from bullet import Bullet
from alien import  Alien


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.bg_color = (25, 25, 25)
        self.player = Player(self.screen)
        self.alien = Alien(self.screen)
        self.max_fps = 60
        self.bullets = []
        self.max_num_bullets = 3
        pygame.display.set_caption("Aliens!")

    def run(self):
        while True:
            delta_time = self.clock.tick(self.max_fps) / 1000
            self._process_global_events()
            self.player.update(delta_time)
            self.alien.update(delta_time)
            self._update_bullets(delta_time)
            self._update_screen()

    def _process_global_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    if len(self.bullets) < self.max_num_bullets:
                        self.bullets.append(Bullet(self.screen, self.player.rifle_tip()))

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.player.draw()
        self.alien.draw()
        for bullet in self.bullets:
            bullet.draw()
        pygame.display.flip()

    def _update_bullets(self, delta_time):
        for bullet in self.bullets.copy():
            bullet.update(delta_time)
            if bullet.out_of_screen():
                self.bullets.remove(bullet)
