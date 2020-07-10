import pygame
import sys
from settings import *
from pygame import Vector2


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


class Player(pygame.sprite.Sprite):
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


class Game:
    def __init__(self):
        """Create the game window, game clock and load required data."""
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("comicsansms", 18)
        self.score = 0

    def reset(self):
        """Prepare sprite groups and main entities"""
        self.all_sprites = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()
        self.bricks = pygame.sprite.Group()

        self.player = Player(self, WIDTH / 2, HEIGHT - PAD_HEIGHT*3)
        self.ball = Ball(self, WIDTH/2, HEIGHT - PAD_HEIGHT * 4)

        self.create_stage()

    def create_stage(self):
        """Just create a wall of bricks"""
        for x in range(0, 11):
            for y in range(0, 7):
                Brick(self,  BRICK_WIDTH * 2.5 + x * BRICK_WIDTH + x *
                      5, BRICK_HEIGHT * 4 + y * BRICK_HEIGHT + y * 5)

    def run(self):
        """The Game Loop! Quite simple in a real-time game: read events, call logic updates, draw everything, rinse, repeat!"""
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)/1000
            self.events()
            self.update()
            self.draw()

    def update(self):
        """Pygame sprites have an update method which should be responsible for updating the game logic."""
        self.all_sprites.update()

        hits = pygame.sprite.groupcollide(
            self.balls, self.bricks, False, False)
        for ball, bricks in hits.items():
            ball.bounce(bricks[0])
            self.score += 1
            bricks[0].hit()

        hits = pygame.sprite.spritecollide(
            self.player, self.balls, False, False)
        for ball in hits:
            self.player.hit_ball(ball)

    def ball_lost(self):
        """Reset the game state"""
        self.player.kill()
        self.ball.kill()

        self.player = Player(self, WIDTH / 2, HEIGHT - PAD_HEIGHT*3)
        self.ball = Ball(self, WIDTH/2, HEIGHT - PAD_HEIGHT * 4)

    def events(self):
        """Event handling"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.player.move(-1)
        if keystate[pygame.K_RIGHT]:
            self.player.move(1)
        if keystate[pygame.K_ESCAPE]:
            self.quit()

    def draw(self):
        """Drawing the game can be tricky, but right now we'll just clear with a plain color, draw bricks, pad,
        ball and score and flip the buffer. """
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.draw_ui()

        pygame.display.flip()

    def draw_ui(self):
        score_text = self.font.render(f"Score: {self.score}", True, GREEN)
        self.screen.blit(score_text, (10, 10))

    def quit(self):
        """Just quit the game and exit"""
        pygame.quit()
        sys.exit()

    def draw_grid(self):
        """A quite handy function that will show the actual tile size of our tile-based game"""
        for x in range(0, WIDTH, BRICK_WIDTH):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, BRICK_HEIGHT):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def show_start_screen(self):
        pass

    def show_ending_screen(self):
        pass


game = Game()

while True:
    game.reset()
    game.run()
