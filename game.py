import sys
import pygame
import logging
from level_scene import LevelScene
from intro_scene import IntroScene


class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.fb_rect = pygame.rect.Rect(0, 0, 400, 400)
        self.fb = pygame.surface.Surface((self.fb_rect.width, self.fb_rect.height))
        self.fb_blit_rect = self.fb_rect.fit(self.display.get_rect())
        self.clock = pygame.time.Clock()
        self.max_fps = 60
        self.scene = IntroScene(self.fb_rect)
        pygame.display.set_caption("Aliens!")
        pygame.mouse.set_visible(False)

    def run(self):
        while True:
            delta_time = self.clock.tick(self.max_fps) / 1000
            if self.scene.finished:
                match self.scene.next_scene:
                    case "level":
                        self.scene = LevelScene(self.fb_rect)
                    case "intro":
                        self.scene = IntroScene(self.fb_rect)
                    case _:
                        logging.info("failed to determine next scene, exiting")
                        sys.exit()

            self._handle_events()
            self.scene.update(delta_time)
            self._update_display()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            self.scene.handle_event(event)

    def _update_display(self):
        self.scene.draw(self.fb)
        fb = pygame.transform.scale(self.fb, self.fb_blit_rect.size)
        self.display.blit(fb, self.fb_blit_rect.topleft)
        pygame.display.update()
