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
        
        # make a speed (for quick game tuning)
        self.speed = 10

        # load the correct sprites
        self.images = {}
        self.images['default']  = pygame.image.load("images/player.png").convert() 
        self.images['up']       = pygame.image.load("images/playerUp.png").convert()
        self.images['down']     = pygame.image.load("images/playerDown.png").convert()
        self.images['left']     = pygame.image.load("images/playerLeft.png").convert()
        self.images['right']    = pygame.image.load("images/playerRight.png").convert()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        '''Update object suraface every key press.'''

        # if there is no keypress use the static image
        self.surf = self.images['default']
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        # on key up
        if pressed_keys[K_UP]:
            # move the rectangle
            self.rect.move_ip(0, -self.speed)
            # change the sprite
            self.surf = self.images['up']
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            # play the sound
            move_up_sound.play()
        # on key down
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)
            self.surf = self.images['down']
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            move_down_sound.play()
        # on key left
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
            self.surf = self.images['left']
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            move_left_sound.play()

        # on key right
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
            self.surf = self.images['right']
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            move_right_sound.play()


        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
