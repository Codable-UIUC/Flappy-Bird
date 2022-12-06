import random
import sys 
import pygame
from pygame.locals import *

width = 289
height = 511
framepersecond = 32
screen = pygame.display.set_mode((width, height))
background = pygame.transform.scale(pygame.image.load("gallery/sprites/background.jpeg"), (width, height))
play_button = pygame.transform.scale(pygame.image.load("buttons/play.png"), (150, 70))
option_button = pygame.transform.scale(pygame.image.load("buttons/options.png"), (100, 60))
quit_button = pygame.transform.scale(pygame.image.load("buttons/icon_x.png"), (57, 57))
player = pygame.transform.scale(pygame.image.load("gallery/sprites/player.png"), (32, 32)) # <-- placeholder
sprites = {}
audio = {}
groundY = height * 0.9

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
                if mouse_pos[0] in range(70, 220) and mouse_pos[1] in range(300, 370):
                    # game start
                    return
                if mouse_pos[0] in range(40, 110) and mouse_pos[1] in range(400, 470):
                    # options
                    pass
                if mouse_pos[0] in range(160, 260) and mouse_pos[1] in range(403, 463):
                    # exit
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
    pipeVelX = -4
    playerVelY = -9
    playerMaxVel = 10  
    playerMinVelY = -8
    playerAccY = 1

    # generate pipes
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()
    
    # upper pipes
    upperPipes = [
        {'x': width+200, 'y':newPipe1[0]['y']},
        {'x': width+200+(width/2), 'y':newPipe2[0]['y']},
    ]
    
    #lower pipes
    lowerPipes = [
        {'x': width+200, 'y':newPipe1[1]['y']},
        {'x': width+200+(width/2), 'y':newPipe2[1]['y']},
    ]
    
    playerFlapVel = -8 
    playerFlapped = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                if playery > 0:
                    playerVelY = playerFlapVel
                    playerFlapped = True
                    # play flap audio

        # collision logic
        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes) 
        if crashTest:
            return
        # score logic

        if playerVelY < playerMaxVel and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False            
        playerHeight = 32
        playery += min(playerVelY, groundY - playery - playerHeight)

        # move pipes 
        for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX
            
        # add new pipe when first goes out of screen
        if 0<upperPipes[0]['x']<5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        # remove out of screen pipe
        if upperPipes[0]['x'] < - sprites['pipe'][0].get_width(): # here there negative sign is also there , so be carefull
            upperPipes.pop(0)
            lowerPipes.pop(0)
 
 
         # Lets blit our sprites now
        screen.blit(sprites['background'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            screen.blit(sprites['pipe'][0], (upperPipe['x'], upperPipe['y']))
            screen.blit(sprites['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

        screen.blit(sprites['base'], (basex, groundY))
        screen.blit(sprites['player'], (playerx, playery))
        pygame.display.update()
        framepersecond_clock.tick(framepersecond)

def isCollide(playerx, playery, upperPipes, lowerPipes):
    # collision logic
    if playery> groundY - 25  or playery<0:
        #audio['hit'].play()
        return True
    
    for pipe in upperPipes:
        pipeHeight = sprites['pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < sprites['pipe'][0].get_width()):
        #    audio['hit'].play()
            return True

    for pipe in lowerPipes:
        if (playery + sprites['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < sprites['pipe'][0].get_width():
        #    audio['hit'].play()
            return True

    return False

def getRandomPipe():
    pipeHeight = sprites['pipe'][0].get_height()
    offset = height/3
    y2 = offset + random.randrange(0, int(height - sprites['base'].get_height()  - 1.2 *offset))
    pipeX = width + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1}, #upper Pipe
        {'x': pipeX, 'y': y2} #lower Pipe
    ]
    return pipe


def gameOver():
    
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Flappy Bird')

    # load in ui sprites and add to list of sprites
    # load in game over ui sprites
    
    pygame.display.update()

    # game over logic (press button to retry / go back to home / etc)

if __name__ == "__main__":

    pygame.init() 
    framepersecond_clock = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird') 

    sprites['base'] =pygame.image.load('gallery/sprites/base.png').convert_alpha()
    sprites['pipe'] =(pygame.transform.rotate(pygame.image.load('gallery/sprites/pipe.png').convert_alpha(), 180), 
    pygame.image.load('gallery/sprites/pipe.png').convert_alpha()
    )

    # Game sounds
    audio['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    audio['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    audio['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    audio['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    audio['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

    sprites['background'] = pygame.image.load('gallery/sprites/background.jpeg').convert()
    sprites['player'] = pygame.image.load('gallery/sprites/player.png').convert_alpha()
    
    while True:
        homescreen() 
        gamescreen()
            
