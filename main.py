import random
import sys 
import pygame
from pygame.locals import *
from pygame import mixer

width = 289
height = 511
framepersecond = 32

pygame.init()

# Screen and buttons
screen = pygame.display.set_mode((width, height))
background = pygame.transform.scale(pygame.image.load("gallery/sprites/background.jpeg"), (width, height))
play_button = pygame.transform.scale(pygame.image.load("buttons/play.png"), (150, 60))
option_button = pygame.transform.scale(pygame.image.load("buttons/options.png"), (150, 60))
quit_button = pygame.transform.scale(pygame.image.load("buttons/exit.png"), (150, 60))
home_button = pygame.transform.scale(pygame.image.load("buttons/icon_home.png"), (45, 45))
info_buttom = pygame.transform.scale(pygame.image.load("buttons/icon_info.png"), (45, 45))
exit_button = pygame.transform.scale(pygame.image.load("buttons/icon_x.png"), (45, 45))
title = pygame.transform.scale(pygame.image.load("gallery/sprites/flappy-bird.png"), (270, 80))

# Options
play_bgm = True
play_sfx = True

# BGM
mixer.music.load('Sound/bgm.wav')
mixer.music.play(-1)

player = pygame.transform.scale(pygame.image.load("gallery/sprites/player.png"), (32, 32)) # <-- placeholder
groundY = height * 0.9
sprites = {}
audio = {}

def homescreen():
    while True:
        screen.blit(background, (0,0))
        mouse_pos = pygame.mouse.get_pos()

        screen.blit(title, (8,100))

        # start button
        screen.blit(play_button, (70, 240))

        # option button
        screen.blit(option_button, (70, 315))

        # quit button
        screen.blit(quit_button, (70, 390))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos[0] in range(70, 220) and mouse_pos[1] in range(240, 300):
                    # game start
                    return
                if mouse_pos[0] in range(70, 220) and mouse_pos[1] in range(315, 375):
                    # options
                    optionscreen()
                if mouse_pos[0] in range(70, 220) and mouse_pos[1] in range(390, 450):
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

        # Credits Button
        credits_text = pygame.font.Font('freesansbold.ttf', 30).render('Credits', True, (255, 255, 255))
        screen.blit(credits_text, (30, 460))
        screen.blit(info_buttom, (170, 453))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos[0] in range(5, 50) and mouse_pos[1] in range(5, 50):
                    return
                if mouse_pos[0] in range(130, 180) and mouse_pos[1] in range(210, 240):
                    play_bgm = True
                    mixer.music.play(-1)
                if mouse_pos[0] in range(200, 260) and mouse_pos[1] in range(210, 240):
                    play_bgm = False
                    mixer.music.stop()
                if mouse_pos[0] in range(130, 180) and mouse_pos[1] in range(270, 300):
                    play_sfx = True
                if mouse_pos[0] in range(200, 260) and mouse_pos[1] in range(270, 300):
                    play_sfx = False
                if mouse_pos[0] in range(170, 215) and mouse_pos[1] in range(453, 498):
                    creditscreen()


        pygame.display.update()


def creditscreen():
    y = 0
    credit_font = pygame.font.Font('freesansbold.ttf', 25)
    clock = pygame.time.Clock()
    name1 = credit_font.render("Minjae Rhee", True, (255, 255, 0))
    name2 = credit_font.render("Michael Bhang", True, (255, 255, 0))
    name3 = credit_font.render("Jehyeok Yeon", True, (255, 255, 0))
    name4 = credit_font.render("Sanghyuk Seo", True, (255, 255, 0))
    name5 = credit_font.render("Emily Shin", True, (255, 255, 0))
    name6 = credit_font.render("Hyerim Oh", True, (255, 255, 0))
    name7 = credit_font.render("Donghyeon Jeong", True, (255, 255, 0))
    while True:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(background, (0, 0))
        screen.blit(exit_button, (5,5))

        credit_rect1 = name1.get_rect()
        credit_rect1.center = (144, (-60+y))
        credit_rect2 = name2.get_rect()
        credit_rect2.center = (144, (-120+y))
        credit_rect3 = name3.get_rect()
        credit_rect3.center = (144, (-180+y))
        credit_rect4 = name4.get_rect()
        credit_rect4.center = (144, (-240+y))
        credit_rect5 = name5.get_rect()
        credit_rect5.center = (144, (-300+y))
        credit_rect6 = name6.get_rect()
        credit_rect6.center = (144, (-360+y))
        credit_rect7 = name7.get_rect()
        credit_rect7.center = (144, -420+y)

        screen.blit(name1, credit_rect1)
        screen.blit(name2, credit_rect2)
        screen.blit(name3, credit_rect3)
        screen.blit(name4, credit_rect4)
        screen.blit(name5, credit_rect5)
        screen.blit(name6, credit_rect6)
        screen.blit(name7, credit_rect7)

        
        # credits_text = pygame.font.Font('freesansbold.ttf', 15).render("Donghyeon Jeong, Jehyeok Yeon, ", True, (255, 255, 255))
        # screen.blit(credits_text, (20, 55+y))
        # credits_text_2 = pygame.font.Font('freesansbold.ttf', 15).render("Minjae Rhee, Michael Bhang", True, (255, 255, 255))
        # screen.blit(credits_text_2, (20, 85+y))
        # credits_text_3 = pygame.font.Font('freesansbold.ttf', 15).render("Hyerim Oh, Sanghyuk Seo", True, (255, 255, 255))
        # screen.blit(credits_text_3, (20, 115+y))
        # credits_text_4 = pygame.font.Font('freesansbold.ttf', 15).render("Emily Shin", True, (255, 255, 255))
        # screen.blit(credits_text_4, (20, 145+y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos[0] in range(5, 50) and mouse_pos[1] in range(5, 50):
                    return


        pygame.display.update()
        y += 1
        pygame.time.wait(10)

        if y == 1000: y = 0

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
    font_gameover = pygame.font.Font('freesansbold.ttf', 30)

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

    myFont = pygame.font.SysFont("arial", 20, True, True)
    score_title = myFont.render("Score:", True, (255, 255, 255))
    score_rect = score_title.get_rect()
    score_rect.x, score_rect.y = 100, 10

    playerFlapVel = -8 
    playerFlapped = False
    score_up = True

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP or (event.type == KEYDOWN and event.key == K_SPACE):
                if playery > 0:
                    playerVelY = playerFlapVel
                    playerFlapped = True
                    # play flap audio
                    audio['wing'].play()

        # collision logic
        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes)

        # game over
        while crashTest:
            gameover_text1 = font_gameover.render("GAME OVER :(", False, (255, 255, 255))
            gameover_rect1 = gameover_text1.get_rect()
            gameover_rect1.center = (144, 120) 

            gameover_text2 = font_gameover.render("Your Score: "+str((score))+"", False, (255, 255, 255))
            gameover_rect2 = gameover_text2.get_rect()
            gameover_rect2.center = (144, 170)

            gameover_text3 = font_gameover.render("Press ESC to Quit", False, (255, 255, 255))
            gameover_rect3 = gameover_text3.get_rect()
            gameover_rect3.center = (144, 220)

            screen.blit(gameover_text1, gameover_rect1)
            screen.blit(gameover_text2, gameover_rect2)
            screen.blit(gameover_text3, gameover_rect3)
            pygame.display.update()
            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            return
            

        # score logic
        player_x = playerx + sprites['player'].get_width()
        pipe_x = lowerPipes[0]['x'] + sprites['pipe'][0].get_width()
        
        if pipe_x > player_x:
            score_up = True
        elif pipe_x < player_x and score_up:
            score += 1
            audio['point'].play()
            score_up = False
        
        # score rendering
        score_title2 = myFont.render(str((score)), True, (255, 255, 255))
        score_rect2 = score_title2.get_rect()
        score_rect2.x, score_rect2.y  = 170, 10

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

        screen.blit(score_title, score_rect)
        screen.blit(score_title2, score_rect2)

        pygame.display.update()
        framepersecond_clock.tick(framepersecond)

        

def isCollide(playerx, playery, upperPipes, lowerPipes):
    # collision logic
    if playery> groundY - 25  or playery<0:
        audio['hit'].play()
        return True
    
    for pipe in upperPipes:
        pipeHeight = sprites['pipe'][0].get_height()
        if (playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x'])+20 < sprites['pipe'][0].get_width()):
            audio['hit'].play()
            return True

    for pipe in lowerPipes:
        if (playery + sprites['player'].get_height() > pipe['y']) and abs(playerx - pipe['x'])+20 < sprites['pipe'][0].get_width():
            audio['hit'].play()
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
    bird_img = pygame.image.load('gallery/sprites/birdy.png')
    sprites['player'] = pygame.transform.scale(bird_img, (30, 21)).convert_alpha()
    # sprites['main'] = pygame.image.load('gallery/sprites/flappy-bird.png')
    
    while True:
        homescreen() 
        gamescreen()
            
