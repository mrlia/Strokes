import pygame

class Stroke:
	"""This class represents a player stroke."""
	positions = []
	strokeID = None
	def __init__(self,id,pos):
		self.strokeID = id
		self.positions = []
		self.positions.append(pos)

	def addPos(self, pos):
		self.positions.append(pos)

	def draw(self,surface):
		prevPos = self.positions[0]
		for pos in self.positions:
			pygame.draw.line(surface, (0,0,0), prevPos, pos, 3)
			prevPos = pos

def isSimilar(firstStroke,secondStroke):
	return True

