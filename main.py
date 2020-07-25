''' FirstPyGame

Author: Danny Ramasawmy and Irina Grigorescu
Date Created:

A simple game following the tutorial by [1] which is a great intro!

Ref:
[1]: https://realpython.com/pygame-a-primer/
'''

# Import and initialize the pygame library
import pygame
import json
from utils import *
from Player import Player
from Enemy import Enemy
from Cloud import Cloud


# Initialise pygame
pygame.init()

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_image = pygame.image.load("images/spacebck.jpg").convert()

# add text surface
font = pygame.font.Font('freesansbold.ttf', 20) 

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 500)
# Create a custom event for adding a new cloud
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - clouds 
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Run until the user asks to quit
running = True

# Score 
scoreCounter = 0
maxLives = 3
livesCounter = 3
maxCollisionDelay = 30
collisionDelayCounter = maxCollisionDelay
scoreAdder = 0.2 # for debugging [0.2]

# # get highest score
with open('score.txt', 'r') as f:
    tmpHs = json.load(f)
    highScore = int(tmpHs['highscore'])  


# start the music
pygame.mixer.music.load("sounds/BackingTrack.mp3")
pygame.mixer.music.play(loops=-1)


# Main loop
while running:

    # increase score
    scoreCounter = scoreCounter + scoreAdder
    # if the high score is beaten reassign
    if scoreCounter > highScore:
        highScore = int(scoreCounter)

    # # # EVENT HANDLING
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
            
            # DEBUG key
            if event.key == K_0:
                # enter a debug point
                print('DEBUG')

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

        # Add a new enemy?
        elif event.type == ADDENEMY:
            # scale velocities with score
            ls = 0
            hs = 10 + scoreCounter//50
            pp = player.rect.centery;
            
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy(ls, hs, pp)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # Add a new cloud?
        elif event.type == ADDCLOUD:
            # Create the new cloud and add it to sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    # # # UPDATE PLAYER POSITION
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
  
    # # # UPDATE HARMLESS CLOUDS
    clouds.update()

    # # # UPDATE ENEMIES
    enemies.update()
    
    # Update the player sprite based on user keypresses  
    player.update(pressed_keys)

  
    # # # FILL SCREEN
    # Fill the background with white
    # screen.surf = pygame.image.load("images/spacebck.jpg").convert()
    screen.fill((0, 0, 0))
    screen.blit(screen_image, (0, 0))

    # # # Lives
    textLives = font.render('Lives: {:0>1d} / {:0>1d}'.format(int(livesCounter), maxLives), True, white)
    textLRect = textLives.get_rect()
    textLRect.center = (SCREEN_WIDTH - 116, 50)

    # # #  update text/score
    # create a text surface object on which text is drawn on it. 
    textScore = font.render('Score: {:0>8d}'.format(int(scoreCounter)), True, white) 
    # create a rectangular object for the text surface object 
    textRect = textScore.get_rect()  
    # set the center of the rectangular object. 
    textRect.center = (SCREEN_WIDTH - 90, 30) 

    # # # print high score
    textHighScore = font.render('High Score: {:0>8d}'.format(int(highScore)), True, white)
    textHSRect = textHighScore.get_rect()  
    textHSRect.center = (SCREEN_WIDTH - 115, 10) 
    
    screen.blit(textScore, textRect) 
    screen.blit(textHighScore, textHSRect)
    screen.blit(textLives, textLRect) 
    
    # # # DRAW EVERYTHING
    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # # # DETECT COLLISIONS
    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):

        if collisionDelayCounter >= 0:
            collisionDelayCounter -= 1
        else:
            collisionDelayCounter = maxCollisionDelay
            livesCounter -= 1

            # play collision sound
            collision_sound.play()

        if livesCounter <= 0:
            # If so, then remove the player and stop the loop
            player.kill()

            # Stop any moving sounds and play the collision sound
            move_up_sound.stop()
            move_down_sound.stop()

            pygame.time.delay(500)
            running = False

    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)
    


# write file
data = {'highscore':str(highScore)}
with open('score.txt', 'w') as f:
    f.write(json.dumps(data))

# # # print final score
font = pygame.font.Font('freesansbold.ttf', 50) 
textFinalScore = font.render('Final Score: {:0>8d}'.format(int(scoreCounter)), True, white)
textFRect = textFinalScore.get_rect()  
textFRect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2) 
screen.blit(textFinalScore, textFRect) 
# Update the display
pygame.display.flip()
pygame.time.delay(5 * 1000) # [ms]

# All done! Stop and quit the mixer.
pygame.mixer.music.stop()
pygame.mixer.quit()


# Done! Time to quit.
pygame.quit()
