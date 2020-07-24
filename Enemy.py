import pygame 
import random
from utils import *

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self, lowspeed=5,highspeed=10,playerPosition=SCREEN_HEIGHT/2):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("images/enemy.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # self.surf = pygame.Surface((20, 10))
        # self.surf.fill((255, 255, 255))
        
        # check player position
        bot = playerPosition - 300
        top = playerPosition + 300
        if bot < 0:
            bot = 0;
        if top > SCREEN_HEIGHT:
            top = SCREEN_HEIGHT

        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(bot, top),
            )
            
        )
        self.speed = random.randint(lowspeed, highspeed)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()