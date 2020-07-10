import pygame
from settings import *
from pygame import Vector2, Surface

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.rect.x, self.rect.y = x * TILESIZE, y * TILESIZE

class Player(pygame.sprite.Sprite):
    def __init__(self, game, position):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.position = position * TILESIZE
        self.desired_velocity = Vector2(0, 0)
        self.velocity = Vector2(0, 0)
        self.grounded = False


    def update(self):
        self.handle_input()

        if self.grounded:
            self.velocity -= self.velocity * DRAG * self.game.dt

        self.velocity += (Vector2(0, GRAVITY) + self.desired_velocity * PLAYER_ACCELERATION) * self.game.dt
        if self.velocity.magnitude() > PLAYER_MAX_SPEED:
            self.velocity.scale_to_length(PLAYER_MAX_SPEED)


        self.position += self.velocity * self.game.dt


        self.rect.x = self.position.x
        self.collide_with_walls("x")
        self.rect.y = self.position.y
        self.collide_with_walls("y")

    def handle_input(self):
        vx, vy = 0, 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            vx = -1
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            vx = 1
        if key[pygame.K_UP] or key[pygame.K_w]:
            vy = -1
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            vy = 1

        self.desired_velocity = Vector2(vx, vy)
        if self.desired_velocity.magnitude() > 0:
            self.desired_velocity = self.desired_velocity.normalize()

    def collide_with_walls(self, dir):
        hits = pygame.sprite.spritecollide(self, self.game.walls, False)
        if len(hits) == 0:
            self.grounded = False
            return

        if dir == 'x':
            if self.velocity.x > 0:
                self.position.x = hits[0].rect.left - self.rect.width
            if self.velocity.x < 0:
                self.position.x = hits[0].rect.right
            self.velocity.x = 0
            self.rect.x = self.position.x

        if dir == 'y':
            if self.velocity.y > 0:
                self.position.y = hits[0].rect.top - self.rect.height
                self.grounded = True
            if self.velocity.y < 0:
                self.position.y = hits[0].rect.bottom
            self.velocity.y = 0
            self.rect.y = self.position.y
