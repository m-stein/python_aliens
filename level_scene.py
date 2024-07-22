import pygame
import numpy as np
from lives import Lives
from scene import Scene
from player import Player
from alien_fleet import AlienFleet
from stars import Stars
from score import Score
from bullet import Bullet
from enum import Enum


class LevelState(Enum):
    RUNNING = 0
    GAME_OVER = 1


class LevelScene(Scene):
    def __init__(self, fb_rect):
        super().__init__(next_scene="intro")
        self.state = LevelState.RUNNING
        self.bg_color = (10, 10, 10)
        self.score = Score()
        self.lives = Lives(fb_rect)
        self.player = Player(fb_rect)
        self.alien_bullets = []
        self.accuracy_bonus = [0]
        self.alien_fleet = AlienFleet(fb_rect, self.alien_bullets, self.accuracy_bonus)
        self.bullets = []
        self.max_num_bullets = 3
        self.stars_layers = [
            Stars(0.5, 30, fb_rect.height),
            Stars(0.3, 20, fb_rect.height),
            Stars(0.2, 10, fb_rect.height),
        ]
        self.game_over_font = pygame.font.SysFont('Carlito Bold', 40)
        self.game_over_surface = self.game_over_font.render("GAME OVER!", True, "White")
        self.game_over_pos = np.array([fb_rect.width / 2 - self.game_over_surface.get_width() / 2, fb_rect.height / 2 - self.game_over_surface.get_height() / 2])

    def handle_event(self, event):
        match self.state:
            case LevelState.RUNNING:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if self.player.ready_to_shoot() and len(self.bullets) < self.max_num_bullets:
                        self.bullets.append(Bullet(self.player.rifle_tip()))
            case LevelState.GAME_OVER:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.finished = True

    def update(self, delta_time):
        for stars in self.stars_layers:
            stars.update(delta_time)
        self._update_bullets(delta_time)
        self.alien_fleet.update(delta_time, self.bullets, self.score)
        if self.state == LevelState.RUNNING:
            self._update_player(delta_time)
        self.score.update(self.accuracy_bonus[0])
        self.lives.update(delta_time)

    def _hit_player(self):
        self.accuracy_bonus[0] = 0
        if self.lives.consume_a_life():
            self.player.respawn()
        else:
            self.state = LevelState.GAME_OVER

    def _update_player(self, delta_time):
        self.player.update(delta_time)
        if self.player.vulnerable():
            for alien in self.alien_fleet.aliens:
                if alien.collider().colliderect(self.player.collider()):
                    self._hit_player()
            for bullet in self.alien_bullets.copy():
                if bullet.collider().colliderect(self.player.collider()):
                    self._hit_player()
                    self.alien_bullets.remove(bullet)

    def _update_bullets(self, delta_time):
        for bullet in self.bullets.copy():
            bullet.update(delta_time)
            if bullet.out_of_sight():
                self.bullets.remove(bullet)
                if self.accuracy_bonus[0] > 0:
                    self.accuracy_bonus[0] -= 1
        for bullet in self.alien_bullets.copy():
            bullet.update(delta_time)
            if bullet.out_of_sight():
                self.alien_bullets.remove(bullet)

    def draw(self, fb):
        fb.fill(self.bg_color)
        for stars in self.stars_layers:
            stars.draw(fb)
        for bullet in self.bullets:
            bullet.draw(fb)
        for bullet in self.alien_bullets:
            bullet.draw(fb)
        self.alien_fleet.draw(fb)
        match self.state:
            case LevelState.RUNNING:
                self.player.draw(fb)
            case LevelState.GAME_OVER:
                fb.blit(self.game_over_surface, (self.game_over_pos[0], self.game_over_pos[1]))
        self.score.draw(fb)
        self.lives.draw(fb)
