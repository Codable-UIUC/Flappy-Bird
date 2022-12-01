import sys 
import pygame
from pygame.locals import *

width = 289
height = 511
screen = pygame.display.set_mode((width, height))
groundY = height * 0.9
sprites = {}
audio = {}

def homescreen():
    # home screen logic (play button)
    pass

def gamescreen():
    
    # load bgm file and play
    score = 0
    playerx = int(width/5)
    playery = int (height/2)
    basex = 0
    playerVelY = -9
    playerMaxVel = 10  
    playerMinVelY = -8
    playerAccY = 1
    # generate pipes

    playerFlapVel = -8 
    playerFlapped = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_SPACE):
                if playery > 0:
                    playerVelY = playerFlapVel
                    playerFlapped = True
                    audio['wing'].play()

        # collision logic

        # score logic

        if playerVelY < playerMaxVel and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False            
        playerHeight = sprites['player'].get_height()
        playery += min(playerVelY, groundY - playery - playerHeight)

        # move pipes 

        # add new pipe when first goes out of screen

        # remove out of screen pipe

        # render sprites
        pygame.display.update()

def isCollide(playerx, playery, upperPipes, lowerPipes):
    # collision logic
    pass


def getRandomPipe():
    # generate random pipe lengths
    pass

def gameOver():
    
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Flappy Bird')

    # load in ui sprites and add to list of sprites
    # load in game over ui sprites
    
    pygame.display.update()

    # game over logic (press button to retry / go back to home / etc)

if __name__ == "__main__":

    pygame.init() 
    pygame.display.set_caption('Flappy Bird') 

    # load sprites and add to list
    # load audio and add to list

    while True:
        homescreen() 
        gamescreen()