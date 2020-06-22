import pygame
import math
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption("Face!!!")
        self.clock = pygame.time.Clock()

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
        pass

    def draw(self):



        pygame.draw.circle(self.screen, YELLOW, (WIDTH // 2, HEIGHT // 2), 128, 30)
        pygame.draw.circle(self.screen, DARKGREY, (WIDTH // 2, HEIGHT // 2), 128, 20)
        pygame.draw.circle(self.screen, WHITE, (280, 200), 10)
        pygame.draw.circle(self.screen, WHITE, (360, 200), 10)
        pygame.draw.circle(self.screen, RED, (320, 220), 10)
        pygame.draw.circle(self.screen, WHITE, (320, 217), 5)
        pygame.draw.arc(self.screen, WHITE, pygame.Rect(270, 200, 100, 50), math.radians(180), 0, 3)
        pygame.display.flip()

game = Game()
game.run()
