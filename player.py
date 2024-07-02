import pygame
import vpython as vp
from animation import Animation


class Player:
    """Class for managing the players input, state and visual output."""

    def __init__(self, screen):
        """Initialize player and its visual according to the screen."""
        self.image = pygame.image.load('content/player.png')
        self.screen = screen
        self.pos = vp.vector(
            screen.get_width() / 2 - self.image.get_width() / 2,
            screen.get_height() - self.image.get_height(), 0)
        self.speed = 400
        self.image_scale = 2
        self.collider_offset = vp.vector(8, 16, 0) * self.image_scale
        self.collider_size = vp.vector(17, 14, 0) * self.image_scale
        self.animation = Animation(vp.vector(32, 32, 0) * self.image_scale, 2, 0.1)

    def draw(self):
        """Draw players visual to the screen."""
        self.screen.blit(self.image, (self.pos.x, self.pos.y), self.animation.frame_rectangle())

    def update(self, delta_time):
        """Update internal state to elapsed time since the last call."""
        self.animation.update(delta_time)
        key_pressed = pygame.key.get_pressed()

        direction = vp.vector(0, 0, 0)
        if key_pressed[pygame.K_LEFT]:
            direction.x -= 1
        if key_pressed[pygame.K_RIGHT]:
            direction.x += 1

        if direction.mag > 0:
            self.pos += direction.norm() * self.speed * delta_time
            min_x = -self.collider_offset.x
            if self.pos.x < min_x:
                self.pos.x = min_x
            min_y = -self.collider_offset.y
            if self.pos.y < min_y:
                self.pos.y = min_y
            max_x = self.screen.get_width() - self.collider_offset.x - self.collider_size.x
            if self.pos.x > max_x:
                self.pos.x = max_x
            max_y = self.screen.get_height() - self.collider_offset.y - self.collider_size.y
            if self.pos.y > max_y:
                self.pos.y = max_y
