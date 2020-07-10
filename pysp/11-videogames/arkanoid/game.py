import pygame
import sys
from settings import *
from pygame import Vector2


class Game:
    def __init__(self):
        """Create the game window, game clock and load required data."""
        pygame.mixer.pre_init(44100, -16, 2, 1024)
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(GAME_TITLE)
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.clock = pygame.time.Clock()
        self.load_data()

    def load_data(self):
        root_folder = path.dirname(__file__)
        img_folder = path.join(root_folder, "img")
        fx_folder = path.join(root_folder, "sound")





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

    # RUN
    def run(self):
        """The Game Loop! Quite simple in a real-time game: read events, call logic updates, draw everything, rinse, repeat!"""
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)/1000
            self.events()
            self.update()
            self.draw()

    # UPDATE
    def update(self):
        """Pygame sprites have an update method which should be responsible for updating the game logic."""
        self.all_sprites.update()
        self.update_collisions()

    def hitbox_collide(self, sprite, other):
        return sprite.hitbox.colliderect(other.hitbox)

    def update_collisions(self):
        hits = pygame.sprite.spritecollide(
            self.player, self.balls, False, self.hitbox_collide
        )
        for ball in hits:
            self.player.hit_ball(ball)

        brick_hits = pygame.sprite.groupcollide(
            self.balls, self.bricks, False, False, self.hitbox_collide
        )

        for ball, bricks in brick_hits.items():
            the_brick = bricks[0]
            ball.bounce(the_brick)

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
                quit()

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
