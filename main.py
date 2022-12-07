import sys 
import pygame
from pygame.locals import *
from pygame import mixer

width = 289
height = 511
framepersecond = 32

# Screen and buttons
screen = pygame.display.set_mode((width, height))
background = pygame.transform.scale(pygame.image.load("background.jpeg"), (width, height))
play_button = pygame.transform.scale(pygame.image.load("buttons/play.png"), (150, 70))
option_button = pygame.transform.scale(pygame.image.load("buttons/options.png"), (120, 60))
quit_button = pygame.transform.scale(pygame.image.load("buttons/exit.png"), (120, 60))
home_button = pygame.transform.scale(pygame.image.load("buttons/icon_home.png"), (45, 45))

# Options
play_bgm = True
play_sfx = True

player = pygame.transform.scale(pygame.image.load("player.png"), (32, 32)) # <-- placeholder



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
        screen.blit(option_button, (15, 400))

        # quit button
        screen.blit(quit_button, (155, 400))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos[0] in range(70, 220) and mouse_pos[1] in range(300, 370):
                    # game start
                    return
                if mouse_pos[0] in range(15, 135) and mouse_pos[1] in range(400, 460):
                    # options
                    optionscreen()
                if mouse_pos[0] in range(155, 275) and mouse_pos[1] in range(400, 460):
                    # exit
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def optionscreen():
    while True:
        global play_bgm
        global play_sfx
        screen.blit(background, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        # Title
        title = pygame.font.Font('freesansbold.ttf', 45).render('Options', True, (255, 255, 255))
        screen.blit(title, (55, 75))

        # BGM
        bgm_text = pygame.font.Font('freesansbold.ttf', 30).render('BGM', True, (255, 255, 255))
        screen.blit(bgm_text, (30, 210))

        # SFX
        sfx_text = pygame.font.Font('freesansbold.ttf', 30).render('SFX', True, (255, 255, 255))
        screen.blit(sfx_text, (30, 270))

        on_text_on = pygame.font.Font('freesansbold.ttf', 30).render('ON', True, (0, 255, 0))
        off_text_on = pygame.font.Font('freesansbold.ttf', 30).render('OFF', True, (255, 0, 0))
        on_text_off = pygame.font.Font('freesansbold.ttf', 30).render('ON', True, (0, 75, 0))
        off_text_off = pygame.font.Font('freesansbold.ttf', 30).render('OFF', True, (75, 0, 0))

        if play_bgm:
            screen.blit(on_text_on, (130, 210))
            screen.blit(off_text_off, (200, 210))

        elif not play_bgm:
            screen.blit(on_text_off, (130, 210))
            screen.blit(off_text_on, (200, 210))

        if play_sfx:
            screen.blit(on_text_on, (130, 270))
            screen.blit(off_text_off, (200, 270))

        elif not play_sfx:
            screen.blit(on_text_off, (130, 270))
            screen.blit(off_text_on, (200, 270))


        # Back Button
        screen.blit(home_button, (5, 5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos[0] in range(5, 50) and mouse_pos[1] in range(5, 50):
                    return
                if mouse_pos[0] in range(130, 180) and mouse_pos[1] in range(210, 240):
                    play_bgm = True
                if mouse_pos[0] in range(200, 260) and mouse_pos[1] in range(210, 240):
                    play_bgm = False
                if mouse_pos[0] in range(130, 180) and mouse_pos[1] in range(270, 300):
                    play_sfx = True
                if mouse_pos[0] in range(200, 260) and mouse_pos[1] in range(270, 300):
                    play_sfx = False


        pygame.display.update()



def gamescreen():
    
    # load bgm file and play
    score = 0
    playerx = int(width/5)
    playery = int (height/2)
    playerVelY = -9
    playerMaxVel = 10  
    playerAccY = 1

    # generate pipes

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

        # score logic

        if playerVelY < playerMaxVel and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False            
        playerHeight = 32
        playery += min(playerVelY, groundY - playery - playerHeight)

        # move pipes 

        # add new pipe when first goes out of screen

        # remove out of screen pipe

        # render sprites
        screen.blit(background, (0,0))
        screen.blit(player, (playerx,playery))
        pygame.display.update()
        framepersecond_clock.tick(framepersecond)

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
    framepersecond_clock = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird') 

    while True:
        homescreen() 
        gamescreen()

