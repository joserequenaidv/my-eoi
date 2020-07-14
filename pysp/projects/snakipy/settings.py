from os import path

# Some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
LIGHTBROWN = (175, 126, 47)
DARKBROWN = (85, 0, 0)
LIGHTBLUE = (75, 175, 250)
DARKBEIGE = (228, 198, 134)
DARKPINK = (254, 102, 140)
REDBROWN = (160, 44, 44)

BGCOLOR = DARKPINK

TEXT_COLOR = WHITE
TEXT_OUTLINE_COLOR = REDBROWN

LOW_TRANS = 64
MED_TRANS = 160
HIGH_TRANS = 215

# Game settings
SCREEN_WIDTH = 480   # 16 * 64 or 32 * 32 or 64 * 16
SCREEN_HEIGHT = 480  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 30
GAME_TITLE = "SNAKIPY"
TITLE = "Tilemap Demo"

TILESIZE = 16
GRIDWIDTH = SCREEN_WIDTH / TILESIZE
GRIDHEIGHT = SCREEN_HEIGHT / TILESIZE

# Sprites
FRUIT = 'black_gums.png'
SNAKE_HEAD = 'bally-head.png'
SNAKE_BODY = 'cloudy-body.png'

# Files settings
ROOT_FOLDER = path.dirname(__file__)
IMG_FOLDER = path.join(ROOT_FOLDER, "images")
FX_FOLDER = path.join(ROOT_FOLDER, "sound")

ICON = 'images/bally-head.png'
BACKGROUND_MUSIC = 'BeepBox-Song.wav'
BACKGROUND_IMG = 'images/cloudy-river.png'
