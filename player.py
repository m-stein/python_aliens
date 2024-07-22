import pygame
import numpy as np
import vector2 as v2
from animation import Animation
from blink import Blink
from enum import Enum


class PlayerState(Enum):
    ALIVE = 0
    RESPAWNING = 1

class Player:
    def __init__(self, fb_rect):
        self.image = pygame.image.load('content/player.png').convert_alpha()
        self.fb_rect = fb_rect
        self.respawn_pos = np.array(
            [float(self.fb_rect.width / 2 - self.image.get_width() / 2),
             float(self.fb_rect.height - self.image.get_height())])
        self.draw_collider = False
        self.speed = 300.
        self.collider_offset = np.array([4, 9])
        self.collider_size = np.array([23, 19])
        self.min_y = self.fb_rect.height - 100 - self.collider_offset[1]
        self.max_y = self.fb_rect.height - self.collider_offset[1] - self.collider_size[1]
        self.min_x = -self.collider_offset[0]
        self.max_x = self.fb_rect.width - self.collider_offset[0] - self.collider_size[0]
        self.animation = Animation(np.array([32, 32]), 2, 0.1)
        self.max_respawning_timeout = 2
        self.respawning_blink = Blink(.15, False)
        self.pos = None
        self.state = None
        self.respawning_timeout = None
        self.respawn()

    def _draw_ship(self, fb):
        if self.draw_collider:
            pygame.draw.rect(fb, "red", self.collider())
        fb.blit(self.image, (self.pos[0], self.pos[1]), self.animation.frame_rectangle())

    def draw(self, fb):
        match self.state:
            case PlayerState.ALIVE:
                self._draw_ship(fb)
            case PlayerState.RESPAWNING:
                if self.respawning_blink.value:
                    self._draw_ship(fb)

    def _update_respawning_timeout(self, delta_time):
        if self.respawning_timeout > delta_time:
            self.respawning_timeout -= delta_time
        else:
            self.respawning_timeout = 0
            self.image.set_alpha(256)
            self.state = PlayerState.ALIVE

    def update(self, delta_time):
        match self.state:
            case PlayerState.ALIVE:
                self._update_position(delta_time)
                self.animation.update(delta_time)
            case PlayerState.RESPAWNING:
                self._update_position(delta_time)
                self.animation.update(delta_time)
                self.respawning_blink.update(delta_time)
                self._update_respawning_timeout(delta_time)

    def _update_position(self, delta_time):
        key_pressed = pygame.key.get_pressed()
        direction = np.array([0, 0])
        if key_pressed[pygame.K_LEFT]:
            direction[0] -= 1
        if key_pressed[pygame.K_RIGHT]:
            direction[0] += 1
        if key_pressed[pygame.K_UP]:
            direction[1] -= 1
        if key_pressed[pygame.K_DOWN]:
            direction[1] += 1
        if v2.length(direction) > 0:
            self.pos += v2.normalized(direction) * self.speed * delta_time
            if self.pos[0] < self.min_x:
                self.pos[0] = self.min_x
            if self.pos[0] > self.max_x:
                self.pos[0] = self.max_x
            if self.pos[1] < self.min_y:
                self.pos[1] = self.min_y
            if self.pos[1] > self.max_y:
                self.pos[1] = self.max_y

    def rifle_tip(self):
        return self.pos + np.array([15.5, 4])

    def collider(self):
        return pygame.Rect(int(self.pos[0] + self.collider_offset[0]),
                           int(self.pos[1] + self.collider_offset[1]),
                           int(self.collider_size[0]),
                           int(self.collider_size[1]))

    def vulnerable(self):
        return self.state == PlayerState.ALIVE

    def ready_to_shoot(self):
        return self.state == PlayerState.ALIVE

    def respawn(self):
        self.pos = self.respawn_pos.copy()
        self.respawning_blink.reset()
        self.image.set_alpha(128)
        self.respawning_timeout = self.max_respawning_timeout
        self.state = PlayerState.RESPAWNING
