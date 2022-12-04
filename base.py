import math
import os
from random import randint
from collections import deque

import pygame
from pygame.locals import *

# global variables

FPS = 60

ANIMATION_SPEED = 0.18
WIN_WIDTH = 284 * 2
WIN_HEIGHT = 512

# Bird Class

class Bird(pygame.sprite.Sprite):
    WIDTH = HEIGHT = 32
    SINK_SPEED = 0.18
    CLIMB_SPEED = 0.3
    CLIMB_DURATION = 333.3

    def __int__(self, x, y, msec_to_climb, images):
        super(Bird, self).__init__()
        self.x, self.y = x, y

        self.msec_to_climb = msec_to_climb
        self._img_wingup, self._img_wingdown = images
        self._mask_wingup = pygame.mask.from_surface(self._img_wingup)
        self._mask_wingdown = pygame.mask.from_surface(self._img_wingdown)

    def update(self, delta_frame = 1):
        if self.msec_to_climb > 0 :
            frac_climb_done = 1 - self.msec_to_climb / Bird.CLIMB_DURATION

            self.y -= (Bird.CLIMB_SPEED) * frames_to_msec(delta_frame) * (1-math.cos(frac_climb_done * math.pi))
            self.msec_to_climb -= frames_to_msec(delta_frame)

        else:
            self.y += Bird.SINK_SPEED*frames_to_msec(delta_frame)

    def image(self):
        if pygame.time.get_ticks() % 500 >= 250:
            return self._mask_wingup
        else:
            return self._mask_wingdown

    def rect(self):
        return Rect(self.x, self.y, Bird.WIDTH, Bird.HEIGHT)

    def mask(self):
        if pygame.time.get_ticks() % 500 >= 250:
            return self._mask_wingup
        else:
            return self._mask_wingdown




# image load
def load_images():

    def load_image(img_file_name):
        file_name = os.path.join('.', 'images', img_file_name)
        img = pygame.image.load(file_name)

        img.convert()
        return img

    return {
        'background': load_image('background.png'),
        'pipe_end': load_image('pipe_end.png'),
        'pipe_body': load_image('pipe_body.png'),
        'bird_wingup': load_image('bird_wing_up.png')
        'bird_wingdown': load_image('bird_wing_down.png')
    }

def frames_to_msec(frame, fps = FPS):
    return 1000.0 * frame / fps

def msec_to_frames(milliseconds, fps = FPS):
    return fps * milliseconds / 1000

# Window display
def main():

    pygame.init()
    display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    pygame.display.set_caption('Flappy Bird')
    clock = pygame.time.Clock()

    score_font = pygame.font.SysFont(None, 32, bold= True)

    images = load_images()


class PipePair(pygame.sprite.Sprite):
    '''
    장애물 생성

    Attribute:
    1. x-axis: X position
    2. no y-axis: 0
    3. image needed
    4. top-pieces
    5. botton-pieces
    6. constants: 1) width 2) piece_height 3) add_interval
    '''
    WIDTH = 80
    PIECE_HEIGHT = 32
    ADD_INTERVAL = 3000

    def __init__(self, pipe_end_img, pipe_body_img):
        # initialize a random pipe pair
        self.x = float(WIN_WIDTH - 1)
        self.score_counted = False
        self.image = pygame((PipePair.WIDTH, WIN_HEIGHT), SRCALPHA)
        self.image.convert()
        self.image.fill((0, 0, 0, 0))

        total_pipe_body_pieces = int((WIN_HEIGHT - 3 * WIN_HEIGHT - 3 * PipePair.PIECE_HEIGHT)/PipePair.PIECE_HEIGHT)

        self.bottom_pieces = randint(1, total_pipe_body_pieces)
        self.top_pieces = randint(1, total_pipe_body_pieces)

        # bottom pipe

        for i in range(1, self.bottom_pieces + 1):
            piece_pos = (0, WIN_HEIGHT - i*PipePair.PIECE_HEIGHT)

            self.image.blit(pipe_body_img, piece_pos)
        bottom_pipe_end_y = WIN_HEIGHT - self.bottom_height_px
        bottom_end_pipe_pos = (0, bottom_pipe_end_y - PipePair.PIECE_HEIGHT)

        self.image.blit(pipe_end_img, bottom_end_pipe_pos)

        # top pipe

        for i in range(self.top_pieces):
            self.image.blit(pipe_body_img, (0, i * PipePair.PIECE_HEIGHT))

        total_pipe_end_x = self.top_height_px
        self.image.blit(pipe_end_img, (0, total_pipe_end_x))

        # compensate for added end pipes
        self.top_pieces += 1
        self.bottom_pieces += 1

        self.mask = pygame.mask.from_surface(self.image)  # detect collision

    def top_height_px(self):
        return self.top_pieces * PipePair.PIECE_HEIGHT

    def bottom_height_px(self):
        return self.bottom_pieces * PipePair.PIECE_HEIGHT

    def visible(self):
        return -PipePair.WIDTH < self.x < WIN_WIDTH
        # boolean type return based on whether pipepair on screen is visible to user
    def rect(self):
        return Rect(self.x, 0, PipePair.WIDTH, PipePair.PIECE_HEIGHT)

    def update(self, delta_frames = 1):
        self.x -= ANIMATION_SPEED * frames_to_msec(delta_frames)

    def collides_with(self, bird):
        return pygame.sprite.collide_mask(self, bird)

bird = Bird()

# main screen

# button 1

# button 2 -> option

while not gameOver:
    # 3 sec generate
    if 3:
        pip = PipePair()

    # 제혁
    if click == True:
        bird.update(up)
    else:
        bird.update(down)

    # 충돌
    if pip1.collides_with(bird):
        gameOver = True
        break

    # score up
    game_score += 1

# esc input -> main screen


def optionScreen():
    bgm, credits



