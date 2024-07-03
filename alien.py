import pygame
from vpython import vector as Vector3
from animation import Animation


class Alien:
    def __init__(self, screen):
        self.image = pygame.image.load('content/alien.png')
        self.screen = screen
        self.pos = Vector3(100, 100, 0)
        self.draw_collider = False
        self.speed = 400.
        self.image_scale = 2
        self.collider_offset = Vector3(5, 6, 0) * self.image_scale
        self.collider_size = Vector3(22, 13, 0) * self.image_scale
        self.animation = Animation(Vector3(32, 32, 0) * self.image_scale, 3, 0.1)

    def draw(self):
        if self.draw_collider:
            pygame.draw.rect(
                self.screen, "red",
                pygame.Rect(self.pos.x + self.collider_offset.x,
                            self.pos.y + self.collider_offset.y,
                            self.collider_size.x,
                            self.collider_size.y))
        self.screen.blit(self.image, (self.pos.x, self.pos.y), self.animation.frame_rectangle())

    def update(self, delta_time):
        self.animation.update(delta_time)
        direction = Vector3(0, 0, 0)

        if direction.mag > 0:
            self.pos += direction.norm() * self.speed * delta_time

