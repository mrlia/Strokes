import pygame, os.path

#Create the relative path to the data
main_dir = os.path.split(os.path.abspath(__file__))[0]

def init_sound():
    # Try to init the sound
    if pygame.mixer and not pygame.mixer.get_init():
        print ('Error, no hay sonido')
        pygame.mixer = None

class noSound:
    """This class is in case the sound fails."""
    def play(self): pass

def load_sound(directory,file):
    """Load a sound file"""
    if not pygame.mixer: return noSound()
    file = os.path.join(main_dir, directory, file)
    try:
        sound = pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        print ('No se puede cargar el sonido %s' % file)
    return noSound()

def load_sounds(directory,*files):
    """Load several sounds and returns a list."""
    sounds = []
    for file in files:
        sounds.append(load_sound(directory,file))
    return sounds
