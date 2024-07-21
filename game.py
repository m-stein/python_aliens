import sys
from level_scene import *


class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.fb_rect = pygame.rect.Rect(0, 0, 400, 400)
        self.fb = pygame.surface.Surface((self.fb_rect.width, self.fb_rect.height))
        self.fb_blit_rect = self.fb_rect.fit(self.display.get_rect())
        self.clock = pygame.time.Clock()
        self.max_fps = 60
        self.scene = LevelScene(self.fb_rect)
        pygame.display.set_caption("Aliens!")

    def run(self):
        while True:
            delta_time = self.clock.tick(self.max_fps) / 1000
            self.scene.update(delta_time)
            self._handle_events()
            self._update_display()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
            self.scene.handle_event(event)

    def _update_display(self):
        self.scene.draw(self.fb)
        fb = pygame.transform.scale(self.fb, self.fb_blit_rect.size)
        self.display.blit(fb, self.fb_blit_rect.topleft)
        pygame.display.update()
