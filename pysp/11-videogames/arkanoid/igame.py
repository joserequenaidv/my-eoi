import pygame
from settings import *

class Game:
    # __INIT__
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(GAME_TITLE)
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.clock = pygame.time.Clock()

    # START GAME
    def start_game(self):
        self.all_sprites = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()
        self.bricks = pygame.sprite.Group()

        self.player = Pad(self, WIDTH // 2, HEIGHT - 64)
        self.ball = Ball(self, WIDTH // 2, HEIGHT - 128)
        self.build_brick_wall()
        self.run()

    # BRICK WALL
    def build_brick_wall(self):
        for x in range(13):
            for y in range(7):
                brick_x = 80 + BRICK_WIDTH * x
                brick_y = 40 + 40 + BRICK_HEIGHT * y + 2*y
                Brick(self, brick_x, brick_y)

    # RUN
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    # EVENTS
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    # UPDATE
    def update(self):
        self.all_sprites.update()

        hits = pygame.sprite.spritecollide(self.player, self.balls, False)
        for ball in hits:






game = Game()
game.run()
