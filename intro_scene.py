import numpy as np
import pygame

from linear_fader import LinearFader
from stars import Stars
from scene import Scene


class IntroScene(Scene):
    def __init__(self, fb_rect):
        super().__init__(next_scene="level")
        self.bg_color = (10, 10, 10)
        self.stars_layers = [
            Stars(0.5, 30, fb_rect.height),
            Stars(0.3, 20, fb_rect.height),
            Stars(0.2, 10, fb_rect.height),
        ]
        self.title_fader = LinearFader(0, 256, 3)
        self.title_font = pygame.font.SysFont('Carlito Bold', 40)
        self.title_surface = self.title_font.render(f"A L I E N S !", True, "White")
        self.title_pos = np.array(
            [fb_rect.width / 2 - self.title_surface.get_width() / 2,
             fb_rect.height / 2 - self.title_surface.get_height() / 2])

    def handle_event(self, event):
        if self.title_fader.finished and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.finished = True

    def update(self, delta_time):
        for stars in self.stars_layers:
            stars.update(delta_time)
        self.title_fader.update(delta_time)
        self.title_surface.set_alpha(int(self.title_fader.value))

    def draw(self, fb):
        fb.fill(self.bg_color)
        for stars in self.stars_layers:
            stars.draw(fb)
        fb.blit(self.title_surface, (self.title_pos[0], self.title_pos[1]))
