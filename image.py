import pygame, os.path
from pygame.locals import *

#Create the relative path to the data
main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(directory,file):
    """Load an image and returns a Surface."""
    file = os.path.join(main_dir, directory, file)
    print(file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        print ('No se puede cargar la imagen %s' % file)
    return surface.convert()

def load_images(directory,*files):
    """Load several images and returns a list."""
    images = []
    for file in files:
        images.append(load_image(directory,file))
    return images

def assembleSprite(directory, filename, size):
    """Returns a list with the images of the file.
    The size is the size of each image in pixels inside the file."""
    width = size[0]
    height = size[1]
    file = os.path.join(main_dir, directory, filename)
    spritesheet = pygame.image.load(file)
    sizeTotal = spritesheet.get_size()
    widthTotal = sizeTotal[0]
    heightTotal = sizeTotal[1]
    row = heightTotal / height
    col = widthTotal / width
    sprites = []
    for y in range(row):
        for x in range(col):
            image = pygame.Surface((width,height))
            w = x*width
            w2 = (x+1)*width
            h = y*height
            h2 = (y+1)*height
            rect = (w, h, w2, h2)
            image.blit(spritesheet, (0,0), rect)
            image = image.convert()
            #colorkey = image.get_at((0,0))
            #image.set_colorkey(colorkey, RLEACCEL)
            sprites.append(image)
    return sprites

def assembleSprites(size, directory, *files):
    """Returns a list with the images of several files
    The size is the size of each image in pixels inside the files.
    The matrix indicates how the images are positionate (nCol,nRow)"""
    sprites = []
    for file in files:
        sprites.append(assembleSprite(directory, file, size))
    return sprites
