import sys 
import pygame
from pygame.locals import *

width = 289
height = 511
screen = pygame.display.set_mode((width, height))
background = pygame.transform.scale(pygame.image.load("background.jpeg"), (width, height))
play_button = pygame.transform.scale(pygame.image.load("buttons/play.png"), (150, 70))
option_button = pygame.transform.scale(pygame.image.load("buttons/options.png"), (100, 60))
quit_button = pygame.transform.scale(pygame.image.load("buttons/icon_x.png"), (57, 57))

groundY = height * 0.9
sprites = {}
audio = {}

def homescreen():
    while True:
        screen.blit(background, (0,0))
        mouse_pos = pygame.mouse.get_pos()

        title = pygame.font.Font('freesansbold.ttf', 45).render('Flappy Bird', True, (255, 255, 255))
        screen.blit(title, (15,100))

        # start button
        screen.blit(play_button, (70, 300))

        # option button
        screen.blit(option_button, (40, 400))

        # quit button
        screen.blit(quit_button, (190, 403))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos[0] in range(70, 220) and mouse_pos[1] in range(360, 430):
                    gamescreen()
                if mouse_pos[0] in range(40, 140) and mouse_pos[1] in range(400, 460):
                    optionscreen()
                if mouse_pos[0] in range(190, 247) and mouse_pos[1] in range(403, 460):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def optionscreen():
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
                    # play flap audio

        # collision logic

        # score logic

        if playerVelY < playerMaxVel and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False            
        playerHeight = 0 # <----- replace with height of player sprite
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

homescreen()