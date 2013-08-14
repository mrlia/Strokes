import pygame

class Score(pygame.sprite.Sprite):
    """This class represents the player score"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.font = pygame.font.Font(None, 25)
        self.font.set_italic(1)
        self.score = 0
        self.name = ""
        self.update()
        self.rect = self.image.get_rect().move(20, 20)

    def addPoint(self,name):
        self.score = self.score + 1
        self.name = name
        print self.score

    def update(self):
        """Update the score"""
        if self.score == 0:
            msg = "Puntuacion: %d" % self.score
        else:
            msg = "Puntuacion: %d Last enemy defeated: %s " % (self.score,self.name)
        self.image = self.font.render(msg, 1, (0,0,0))
