




class Pad(pygame.sprite.Sprite):
    """Player pad. Moves from left to right and hits balls"""

    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((PAD_WIDTH, PAD_HEIGHT))
        self.image.fill(BLUE)
        self.velocity = Vector2(0, 0)
        self.rect = self.image.get_rect()
        self.rect.center = Vector2(x, y)

    def move(self, dx=0):
        self.velocity += Vector2(dx * PAD_ACCELERATION, 0) * self.game.dt
        if self.velocity.magnitude() > PAD_MAX_SPEED:
            self.velocity.scale_to_length(PAD_MAX_SPEED)

    def update(self):
        """Just move horizontally with a bit of incerce"""
        self.rect.centerx += self.velocity.x * self.game.dt
        self.velocity *= 0.5
        if self.velocity.magnitude() < 2:
            self.velocity = Vector2(0, 0)
        if self.rect.left < 0:
            self.rect.left = 1
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH - 1

    def hit_ball(self, ball):
        """Make ball bounce, but alter its horizontal velocity depending on where it hits"""
        ball.bounce(self)
        offset = 2 * (ball.rect.centerx - self.rect.centerx) / PAD_WIDTH
        ball.velocity.x = offset


class Brick(pygame.sprite.Sprite):
    """Bricks can be pretty simple. They are just sprites that are killed when ball hits them."""

    def __init__(self, game, x, y):
        self.groups = game.bricks, game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = Vector2(x, y)

    def hit(self):
        self.kill()


class Ball(pygame.sprite.Sprite):
    """Balls just bounce around, hitting things"""

    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.balls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((BALL_WIDTH, BALL_HEIGHT))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.velocity = Vector2(0, 0)
        self.rect.center = Vector2(x, y)
        self.speed = BALL_SPEED
        self.asleep = True

    def update(self):
        """Don't move until awoken"""
        if self.asleep:
            if self.game.player.velocity.magnitude() > 0:
                self.asleep = False
                self.velocity = self.game.player.velocity.normalize() - Vector2(0, 1)
            return

        self.rect.center += self.velocity.normalize() * BALL_SPEED * self.game.dt

        # Limit our position to world coordinates
        if self.rect.left < 0:
            self.rect.left = 1
            self.velocity.x *= -1
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH - 1
            self.velocity.x *= -1
        if self.rect.top < 0:
            self.rect.top = 1
            self.velocity.y *= -1

        if self.rect.top > HEIGHT:
            self.game.ball_lost()

    def bounce(self, thing):
        """Bounce vertically or horizontally depending on where we collide"""
        xDist = abs(self.rect.centerx - thing.rect.centerx) - \
            thing.rect.width / 2
        yDist = abs(self.rect.centery - thing.rect.centery) - \
            thing.rect.height / 2
        if xDist <= yDist:
            self.velocity.y = -self.velocity.y
            if self.rect.centery < thing.rect.centery:
                self.rect.bottom = thing.rect.top
            else:
                self.rect.top = thing.rect.bottom
        else:
            self.velocity.x = -self.velocity.x
            if self.rect.centerx < thing.rect.centerx:
                self.rect.right = thing.rect.left - 1
            else:
                self.rect.left = thing.rect.right + 1

