import math
import pygame
from os import path

from maps import Map
from settings import *
from sprites import Player, Fruit, Wall

class Game:
    # INIT
    def __init__(self):
        pygame.init()

        # Screen
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

        # Background
        self.background = pygame.image.load(BACKGROUND_IMG)

        # Caption
        pygame.display.set_caption(GAME_TITLE)

        # Icon
        icon = pygame.image.load(ICON)
        pygame.display.set_icon(icon)

        self.clock = pygame.time.Clock()

        self.large_font = pygame.font.SysFont("chicken_pie", 80)
        self.small_font = pygame.font.SysFont("chicken_pie", 32)
        self.smaller_font = pygame.font.SysFont("chicken_pie", 24)

        self.thin_small_font = pygame.font.SysFont("ubuntu", 24)

        self.score = 0
        self.font = pygame.font.SysFont("chicken_pie", 24)

        self.playing = False

        self.load_data()

    # LOAD DATA
    def load_data(self):
        root_folder = path.dirname(__file__)
        img_folder = path.join(root_folder, "images")
        fx_folder = path.join(root_folder, "sound")

        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.fruits = pygame.sprite.Group()

        # MAPS WITHOUT COLLISION
        self.map = Map()
        self.map.load_from_file('map.txt')
        self.map.create_sprites_from_map_data(self)

        # Load images
        self.head_image = pygame.image.load(
            path.join(IMG_FOLDER, SNAKE_HEAD)).convert_alpha()

        self.body_image = pygame.image.load(
            path.join(IMG_FOLDER, SNAKE_BODY)).convert_alpha()

        self.fruit_image = pygame.image.load(
            path.join(IMG_FOLDER, FRUIT)).convert_alpha()

        # Load FX
        self.music = pygame.mixer.music.load(
            path.join(FX_FOLDER, BACKGROUND_MUSIC))

        pygame.mixer.music.play(3)

    # -- Fruit collisions: place it on the right spot
    def avoid_walls(self):
        fruit_placed_successfully = False
        # Keep trying until success

        while not fruit_placed_successfully:
            self.fruit.teleport()

            fruit_hits_wall = pygame.sprite.spritecollide(self.fruit, self.walls, False)

            if len(fruit_hits_wall) == 0:
                fruit_placed_successfully = True

    # RUN
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
        self.game_over()

    # START GAME
    def start_game(self):
        self.load_data()
        self.fruit = Fruit(self)
        self.player = Player(self, 10, 10, self.map.player_entry_point)
        self.score = 0
        self.run()

    # EVENTS
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.paused()
                    #self.player.grow()

    # UPDATE
    def update(self):
        self.all_sprites.update()

        # SNAKE COLLISIONS
        # Collision with fruits
        hits_with_fruit = pygame.sprite.spritecollide(
            self.player, self.fruits, False)
        for fruit in hits_with_fruit:
            self.player.grow()
            self.avoid_walls()
            self.score += 1
            self.speed_up()

        # Collision with walls
        hits_with_wall = pygame.sprite.spritecollide(self.player, self.walls, False)
        for crash in hits_with_wall:
            self.game_over()

        self.playing = self.player.alive

    # DRAW
    def draw(self):
        self.screen.fill(BGCOLOR)

        # Background Image
        self.screen.blit(self.background, (0, 0))

        # Grids
        #for x in range(0, SCREEN_WIDTH, TILESIZE):
        #    pygame.draw.line(self.screen, WHITE, (x, 0), (x, SCREEN_HEIGHT))
        #for y in range(0, SCREEN_HEIGHT, TILESIZE):
        #    pygame.draw.line(self.screen, WHITE, (0, y), (SCREEN_WIDTH, y))

        self.all_sprites.draw(self.screen)
        self.player.draw_tail(self.screen)

        # Titles
        # Score
        score_text = self.small_font.render(f"Score: {self.score}", True, TEXT_OUTLINE_COLOR)
        self.screen.blit(score_text, (12, 12))

        score_text = self.small_font.render(f"Score: {self.score}", True, TEXT_COLOR)
        self.screen.blit(score_text, (10, 10))

        # Speed
        speed_text = self.small_font.render(f"Speed: {self.player.speed}", True, TEXT_OUTLINE_COLOR)
        self.screen.blit(speed_text, (332, 12))

        speed_text = self.small_font.render(f"Speed: {self.player.speed}", True, TEXT_COLOR)
        self.screen.blit(speed_text, (330, 10))

        # Pause
        pause_text = self.smaller_font.render(f"[SPACE] = Pause", True, TEXT_COLOR)
        self.screen.blit(pause_text, (147, 442))

        pause_text = self.smaller_font.render(f"[SPACE] = Pause", True, TEXT_OUTLINE_COLOR)
        self.screen.blit(pause_text, (145, 440))


        # Nothing else to draw, let's show it!
        pygame.display.flip()

    # SPEED UP
    def speed_up(self):
        if self.score % 5 == 0:
            self.player.speed += 1

    # MENU
    def main_menu(self):
        # BACKGROUND
        self.screen.fill(BGCOLOR)

        # TITLES
        # MAIN
        # Outline
        title_text = self.large_font.render(GAME_TITLE, True, TEXT_OUTLINE_COLOR)
        self.screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_rect().width//2, SCREEN_HEIGHT // 3 - title_text.get_rect().height//2))

        # Text
        title_text = self.large_font.render(GAME_TITLE, True, YELLOW)
        self.screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_rect().width//2, SCREEN_HEIGHT // 3.05 - title_text.get_rect().height//2))

        # INSTRUCTIONS
        # Outline
        instructions_text = self.small_font.render("Press any key to begin", True, TEXT_OUTLINE_COLOR)
        self.screen.blit(instructions_text, (SCREEN_WIDTH // 2 - instructions_text.get_rect().width//2, SCREEN_HEIGHT // 2 - instructions_text.get_rect().height//3))

        # Text
        instructions_text = self.small_font.render("Press any key to begin", True, WHITE)
        self.screen.blit(instructions_text, (SCREEN_WIDTH // 2 - instructions_text.get_rect().width//2, SCREEN_HEIGHT // 2.02 - instructions_text.get_rect().height//3))


        pygame.display.flip()

        in_main_menu = True

        while in_main_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    in_main_menu = False
        self.start_game()

    # PAUSE
    def paused(self):

        pause = True

        # Transparence
        pause_window = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        pause_window.set_alpha(LOW_TRANS)
        pause_window.fill((WHITE))
        self.screen.blit(pause_window, (0, 0))

        # MAIN
        # Outline
        title_text = self.large_font.render("PAUSED", True, TEXT_OUTLINE_COLOR)
        self.screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_rect().width//2, SCREEN_HEIGHT // 3 - title_text.get_rect().height//2))

        # Text
        title_text = self.large_font.render("PAUSED", True, YELLOW)
        self.screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_rect().width//2, SCREEN_HEIGHT // 3.05 - title_text.get_rect().height//2))

        # CONTINUE_TEXT
        # Outline
        continue_text = self.small_font.render(
            f"[Press SPACE to continue]", True, TEXT_OUTLINE_COLOR)
        self.screen.blit(continue_text, (SCREEN_WIDTH // 2 - continue_text.get_rect().width//2, SCREEN_HEIGHT // 2 - continue_text.get_rect().height//3))

        # Text
        continue_text = self.small_font.render(
            f"[Press SPACE to continue]", True, WHITE)
        self.screen.blit(continue_text, (SCREEN_WIDTH // 2 - continue_text.get_rect().width//2, SCREEN_HEIGHT // 2.02 - continue_text.get_rect().height//3))

        while pause:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:
                        pause = False

            pygame.display.update()
            self.clock.tick(15)


    # GAME OVER
    def game_over(self):
        # BACKGROUND
        self.screen.fill(BGCOLOR)

        # TITLES
        # MAIN
        # Outline
        main_text = self.large_font.render("GAME OVER", True, TEXT_OUTLINE_COLOR)
        self.screen.blit(main_text, (SCREEN_WIDTH // 2 - main_text.get_rect().width//2, SCREEN_HEIGHT // 3 - main_text.get_rect().height//2))

        # Text
        main_text = self.large_font.render("GAME OVER", True, YELLOW)
        self.screen.blit(main_text, (SCREEN_WIDTH // 2 - main_text.get_rect().width//2, SCREEN_HEIGHT // 3.05 - main_text.get_rect().height//2))

        # FINAL SCORE
        # Outline
        score_text = self.small_font.render(
            f"Score: {self.score}", True, TEXT_OUTLINE_COLOR)
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_rect().width//2, SCREEN_HEIGHT // 2 - score_text.get_rect().height//3))

        # Text
        score_text = self.small_font.render(
            f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_rect().width//2, SCREEN_HEIGHT // 2.02 - score_text.get_rect().height//3))

        # INDICATIONS
        # Outline
        any_key_text = self.small_font.render("[Press any key]", True, TEXT_OUTLINE_COLOR)
        self.screen.blit(any_key_text, (SCREEN_WIDTH // 2 - any_key_text.get_rect().width//2, SCREEN_HEIGHT // 1.6 - any_key_text.get_rect().height//3))

        # Text
        any_key_text = self.small_font.render("[Press any key]", True, YELLOW)
        self.screen.blit(any_key_text, (SCREEN_WIDTH // 2 - any_key_text.get_rect().width//2, SCREEN_HEIGHT // 1.62 - any_key_text.get_rect().height//3))

        pygame.display.flip()
        pygame.time.delay(2000)

        in_game_over = True

        while in_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    in_main_menu = False
                    self.start_game()


game = Game()
game.main_menu()
game.start_game()
