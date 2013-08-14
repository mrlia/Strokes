import pygame
from image import *
from sound import *
from pygame.locals import *

SCREENRECT = Rect(0, 0, 900, 600)
screen = pygame.display.set_mode(SCREENRECT.size)

def init_window():
    # screen mode
    winstyle = RESIZABLE # or 0 | FULLSCREEN | NOFRAME
    bestColorDepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestColorDepth)

    # Create the visualitation window
    screen.fill((0,255,255))
    pygame.display.flip()
    pygame.display.set_icon(load_image('data','icon.gif'))
    pygame.display.set_caption('Lost Sound')

def init_background():    
    # Create the background
    bgdImage  = load_image('background.bmp')
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.blit(bgdImage, (0, 0))

    screen.blit(background, (0,0))
    pygame.display.flip()