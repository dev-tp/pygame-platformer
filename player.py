import pygame

from pygame.locals import *
from pygame.math import Vector2 as Vector

from constants import *


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game

        width = 10
        height = 20

        self.acceleration = Vector(0, 0)
        self.position = Vector(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.velocity = Vector(0, 0)

        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.position

    def get_platform_collisions(self):
        self.rect.x += 1

        collisions = pygame.sprite.spritecollide(
            self,
            self.game.platforms,
            False
        )

        self.rect.x -= 1

        return collisions

    def jump(self):
        # Player needs to be stepping on a platform to jump
        if self.get_platform_collisions():
            self.velocity.y = -15

    def update(self):
        self.acceleration = Vector(0, PLAYER_GRAVITY)

        pressed_keys = pygame.key.get_pressed()

        # Handle keyboard events
        if pressed_keys[K_LEFT]:
            self.acceleration.x = -PLAYER_ACCELERATION

        if pressed_keys[K_RIGHT]:
            self.acceleration.x = PLAYER_ACCELERATION

        if pressed_keys[K_SPACE]:
            self.jump()

        # Control player's speed
        self.acceleration.x += self.velocity.x * PLAYER_FRICTION
        self.velocity += self.acceleration
        self.position += .5 * self.acceleration + self.velocity

        # Check if player is out of bounds
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0

        elif self.position.x < 0:
            self.position.x = SCREEN_WIDTH

        # Check for collisions with platforms
        if self.velocity.y > 0:
            collisions = self.get_platform_collisions()

            if collisions:
                # Offset one pixel to avoid colliding over and over again with
                # the same platform
                self.position.y = collisions[0].rect.top + 1
                self.velocity.y = 0

        # Update position
        self.rect.midbottom = self.position
