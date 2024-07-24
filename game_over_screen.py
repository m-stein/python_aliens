import pygame
import numpy as np
from linear_fader import LinearFader


class GameOverScreen:
    def __init__(self, fb_rect):
        self.fader = LinearFader(0, 256, 3)
        self.font = pygame.font.SysFont('Carlito Bold', 40)
        self.surface = self.font.render("GAME OVER!", True, "Red")
        self.pos = np.array(
            [fb_rect.width / 2 - self.surface.get_width() / 2, fb_rect.height / 2 - self.surface.get_height() / 2])
        self.surface.set_alpha(self.fader.value)

    def update(self, delta_time):
        self.fader.update(delta_time)
        self.surface.set_alpha(self.fader.value)

    def draw(self, fb):
        fb.blit(self.surface, (self.pos[0], self.pos[1]))
