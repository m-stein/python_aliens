import pygame
import sys
from player import Player


class Aliens:
    """Class for managing the overall game state and actions."""

    def __init__(self):
        """Initialize the game without running it."""
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.bg_color = (25, 25, 25)
        self.player = Player(self.screen)
        self.max_fps = 60
        pygame.display.set_caption("Aliens!")

    def run_game(self):
        """Run the games main loop."""
        while True:
            delta_time = self.clock.tick(self.max_fps)
            self._process_global_events()
            self.player.update(delta_time)
            self._update_screen()

    @staticmethod
    def _process_global_events():
        """Call all game-global event handlers."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Draw the current frame onto the screen and flip it."""
        self.screen.fill(self.bg_color)
        self.player.draw()
        pygame.display.flip()
