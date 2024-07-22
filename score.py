import pygame

class Score:
    def __init__(self):
        self.surface = None
        self.font = pygame.font.SysFont('Carlito Bold', 20)
        self.value = 0

    def update(self, accuracy_bonus):
        self.surface = self.font.render(f"Pts: {self.value}  Acc: {accuracy_bonus}", True, "White")

    def draw(self, fb):
        fb.blit(self.surface, (10, 10))

    def increment_by(self, value):
        self.value += value
