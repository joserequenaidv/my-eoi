import pygame
import random
import math

from settings import *

#class Background(pygame.sprite.Sprite):
 #   def __init__(self, image_file, location):
  #      self.groups = game.all_sprites
   #     pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
    #    self.image = pygame.image.load(image_file)
     #   self.rect = self.image.get_rect()
      #  self.rect.left, self.rect.top = location

#######################################
# PLAYER
#######################################
class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y, position):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        #self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image = game.head_image
        #self.image.fill(YELLOW)

        self.rect = self.image.get_rect()
        #self.tail_image = pygame.Surface((TILESIZE, TILESIZE))
        self.tail_image = game.body_image
        #self.tail_image.fill(LIGHTBLUE)

        self.position = position

        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

        self.rect.x = position.x * TILESIZE
        self.rect.y = position.y * TILESIZE

        self.speed = 10
        self.turn = 0

        self.eating_sound = pygame.mixer.Sound("sound/fruta.wav")

        self.tail = []
        self.tail_length = 1
        self.alive = True

    def grow(self):
        self.eating_sound.play()
        self.tail_length += 1

    def update(self):
        self.move()
        self.wrap_around_world()
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def move(self):
        self.turn += self.speed * self.game.dt

        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT] and self.dx == 0:
            self.dx = -1
            self.dy = 0
        if keystate[pygame.K_RIGHT] and self.dx == 0:
            self.dx = 1
            self.dy = 0
        if keystate[pygame.K_UP] and self.dy == 0:
            self.dy = -1
            self.dx = 0
        if keystate[pygame.K_DOWN] and self.dy == 0:
            self.dy = 1
            self.dx = 0

        if (self.turn >= 1):
            self.turn = 0
            self.update_tail()
            self.x += self.dx
            self.y += self.dy
            self.check_death()

    #MAP WITHOUT BORDERS
    def wrap_around_world(self):
        if self.x >= GRIDWIDTH:
            self.x = 0
        if self.x < 0:
            self.x = GRIDWIDTH-1
        if self.y >= GRIDHEIGHT:
            self.y = 0
        if self.y < 0:
            self.y = GRIDHEIGHT-1

    def update_tail(self):
        if len(self.tail) > self.tail_length:
            self.tail.pop()
        self.tail.insert(0, (self.x, self.y))

    def draw_tail(self, surface):
        for i in range(0, len(self.tail)):
            x = self.tail[i][0] * TILESIZE
            y = self.tail[i][1] * TILESIZE
            surface.blit(self.tail_image, (x, y))

    def check_death(self):
        is_stopped = self.dx != 0 or self.dy != 0
        if is_stopped and (self.x, self.y) in self.tail:
            self.alive = False
            print("OUCH!")

#######################################
# FRUIT
#######################################
class Fruit(pygame.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites, game.fruits
        pygame.sprite.Sprite.__init__(self, self.groups)
        #self.image = pygame.Surface((TILESIZE, TILESIZE))
        #self.image.fill(RED)
        self.image = game.fruit_image
        self.rect = self.image.get_rect()
        self.teleport()

    def teleport(self):
        x = random.randint(0, GRIDWIDTH-1)
        y = random.randint(0, GRIDHEIGHT-1)
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def avoid_walls(self):
        fruit_placed_successfully = False
        # Keep trying until success

        while not fruit_placed_successfully:
            self.teleport()

            fruit_hits_wall = pygame.sprite.spritecollide(self.fruit, self.walls, False)

            if len(fruit_hits_wall) == 0:
                fruit_placed_successfully = True

#######################################
# WALL
#######################################
class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.rect.x, self.rect.y = x * TILESIZE, y * TILESIZE

