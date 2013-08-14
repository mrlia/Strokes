import pygame
from image import *
from sound import *
from pygame.locals import *

SCREENRECT = Rect(0, 0, 900, 600)
screen = pygame.display.set_mode(SCREENRECT.size)
background = pygame.Surface(screen.get_size())
background = background.convert()
bgdImage  = load_image('data','background.jpg')
background.blit(bgdImage, (0, 0))

def init_window():
    # screen mode
    winstyle = RESIZABLE # or 0 | FULLSCREEN | NOFRAME
    bestColorDepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestColorDepth)

    # Create the visualitation window
    pygame.display.set_icon(load_image('data','icon.gif'))
    pygame.display.set_caption('Kanji Strokes')

def init_background():
    # Create the background
    screen.blit(background, (0,0))
    pygame.display.flip()

def get_screen():
    return screen

def get_background():
    return background

def update_screen():
    screen.blit(background, (0,0))
