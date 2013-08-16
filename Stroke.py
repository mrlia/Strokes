import pygame, math

class Stroke:
	"""This class represents a player stroke."""
	positions = []
	strokeID = None
	def __init__(self,id,pos):
		self.strokeID = id
		self.positions = []
		if pos != None :
			self.positions.append(pos)

	def addPos(self, pos):
		self.positions.append(pos)

	def draw(self,surface):
		prevPos = self.positions[0]
		for pos in self.positions:
			pygame.draw.line(surface, (0,0,0), prevPos, pos, 3)
			prevPos = pos

def getAngle(stroke):
	return math.atan2(stroke.positions[-1][1] - stroke.positions[0][1], stroke.positions[-1][0] - stroke.positions[0][0])

def isSimilar(firstStroke,secondStroke):
	x = getAngle(firstStroke)
	y = getAngle(secondStroke)
	result = abs(x-y)
	print "result:"
	print result
	return result < 0.3

