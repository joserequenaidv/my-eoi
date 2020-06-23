import math
import pygame

from settings import *
from sprites import Player, Fruit

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption("Snakipy")
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.fruits = pygame.sprite.Group()

        self.player = Player(self, 10, 10)
        self.fruit = Fruit(self)

        self.score = 0
        self.font = pygame.font.SysFont("chicken_pie", 24)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.grow()

    def update(self):
        self.all_sprites.update()
        self.playing = self.playing and self.player.alive

        hits = pygame.sprite.spritecollide(
            self.player, self.fruits, False)
        for fruit in hits:
            self.player.grow()
            fruit.teleport()
            self.score += 1

    def draw(self):
        self.screen.fill(BGCOLOR)
        # grid

        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, DARKGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

        self.all_sprites.draw(self.screen)
        self.player.draw_tail(self.screen)

        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        # Nothing else to draw, let's show it!
        pygame.display.flip()

game = Game()
game.run()
