import math
import pygame

from settings import *
from mysprite import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption("Player")
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.player1 = Player(self, 10, 10)
        self.player2 = Player(self, 10, 10)
        self.player3 = Player(self, 10, 10)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(30)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False


    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        # grid

        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, DARKGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

        self.all_sprites.draw(self.screen)


        # Nothing else to draw, let's show it!
        pygame.display.flip()

game = Game()
game.run()
