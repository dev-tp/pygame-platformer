import pygame

from pygame.locals import *

from constants import *
from player import Player


class Game(object):

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Game')

        self.canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.is_running = True

    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.is_running = False

            if event.type == KEYDOWN:
                if event.key == K_w and pygame.key.get_mods() & KMOD_LCTRL:
                    self.is_running = False

    def render(self):
        self.canvas.fill(WHITE)
        self.all_sprites.draw(self.canvas)

        pygame.display.flip()

    def run(self):
        player = Player()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(player)

        while self.is_running:
            self.clock.tick(FRAMES_PER_SECOND)
            self.events()
            self.update()
            self.render()

    def update(self):
        self.all_sprites.update()


def main():
    game = Game()
    game.run()

    pygame.quit()


if __name__ == '__main__':
    main()
