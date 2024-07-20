import pygame

class Score:
    def __init__(self):
        self.surface = None
        self.font = pygame.font.SysFont('Carlito Bold', 20)
        self.value = 0

    def update(self, delta_time):
        self.surface = self.font.render(f"Score: {self.value}", True, "White")

    def draw(self, surface):
        surface.blit(self.surface, (10, 10))

    def increment(self):
        self.value += 1
