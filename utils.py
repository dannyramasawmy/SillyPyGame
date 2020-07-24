# Import and initialize the pygame library
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# initialize the mixer in pygame (call before pygame.init())
pygame.mixer.init(44100, -16, 1, 512)

# Load all sound files
move_up_sound = pygame.mixer.Sound("sounds/soundUp.wav")
move_down_sound = pygame.mixer.Sound("sounds/soundDown.wav")
move_left_sound = pygame.mixer.Sound("sounds/soundLeft.wav")
move_right_sound = pygame.mixer.Sound("sounds/soundRight.wav")
collision_sound = pygame.mixer.Sound("sounds/soundCollision.wav")
