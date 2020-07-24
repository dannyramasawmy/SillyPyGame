import pygame 
from utils import *

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("images/player.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # self.surf = pygame.Surface((75, 25))
        # self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        '''Update object suraface every key press.'''

        # if there is no keypress use the static image
        self.surf = pygame.image.load("images/player.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        # on key up
        if pressed_keys[K_UP]:
            # move the rectangle
            self.rect.move_ip(0, -5)
            # change the sprite
            self.surf = pygame.image.load("images/playerUp.png").convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # on key down
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            self.surf = pygame.image.load("images/playerDown.png").convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # on key left
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
            self.surf = pygame.image.load("images/playerLeft.png").convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # on key right
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            self.surf = pygame.image.load("images/playerRight.png").convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)


        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
