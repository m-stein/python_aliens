import pygame
from vpython import vector as Vector3
from animation import Animation


class Player:
    def __init__(self, fb_rect):
        self.image = pygame.image.load('content/player.png')
        self.fb_rect = fb_rect
        self.pos = Vector3(
            self.fb_rect.width / 2 - self.image.get_width() / 2,
            self.fb_rect.height - self.image.get_height(), 0)
        self.draw_collider = False
        self.speed = 300.
        self.collider_offset = Vector3(4, 9, 0)
        self.collider_size = Vector3(23, 19, 0)
        self.min_y = self.fb_rect.height - 100 - self.collider_offset.y
        self.max_y = self.fb_rect.height - self.collider_offset.y - self.collider_size.y
        self.min_x = -self.collider_offset.x
        self.max_x = self.fb_rect.width - self.collider_offset.x - self.collider_size.x
        self.animation = Animation(Vector3(32, 32, 0), 2, 0.1)

    def draw(self, fb):
        if self.draw_collider:
            pygame.draw.rect(
                fb, "red",
                pygame.Rect(self.pos.x + self.collider_offset.x,
                            self.pos.y + self.collider_offset.y,
                            self.collider_size.x,
                            self.collider_size.y))
        fb.blit(self.image, (self.pos.x, self.pos.y), self.animation.frame_rectangle())

    def update(self, delta_time):
        self.animation.update(delta_time)
        key_pressed = pygame.key.get_pressed()

        direction = Vector3(0, 0, 0)
        if key_pressed[pygame.K_LEFT]:
            direction.x -= 1
        if key_pressed[pygame.K_RIGHT]:
            direction.x += 1
        if key_pressed[pygame.K_UP]:
            direction.y -= 1
        if key_pressed[pygame.K_DOWN]:
            direction.y += 1

        if direction.mag > 0:
            self.pos += direction.norm() * self.speed * delta_time
            if self.pos.x < self.min_x:
                self.pos.x = self.min_x
            if self.pos.x > self.max_x:
                self.pos.x = self.max_x
            if self.pos.y < self.min_y:
                self.pos.y = self.min_y
            if self.pos.y > self.max_y:
                self.pos.y = self.max_y

    def rifle_tip(self):
        return self.pos + Vector3(15.5, 4, 0)
