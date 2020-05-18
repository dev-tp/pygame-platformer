import pygame

from pygame.locals import *
from pygame.math import Vector2 as Vector

from constants import *


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        width = 10
        height = 20

        self.acceleration = Vector(0, 0)
        self.position = Vector(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.velocity = Vector(0, 0)

        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self):
        self.acceleration = Vector(0, 0)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.acceleration.x = -PLAYER_ACCELERATION

        if pressed_keys[K_RIGHT]:
            self.acceleration.x = PLAYER_ACCELERATION

        self.acceleration += self.velocity * PLAYER_FRICTION
        self.velocity += self.acceleration
        self.position += .5 * self.acceleration + self.velocity

        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0

        elif self.position.x < 0:
            self.position.x = SCREEN_WIDTH

        self.rect.center = self.position
