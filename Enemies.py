import json, pygame
from random import randrange
from image import *
from Stroke import *

class Enemy(pygame.sprite.Sprite):
	"""This class represents the kanji enemies, with the name and stroke list."""
	strokes = []
	name = ""
	curStroke = 0
	def __init__(self,id,strokeList,name):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.id = id
		self.curImages = self.images[self.id]
		self.image = self.curImages[self.curStroke]
		self.rect = self.image.get_rect(center=(200,200))
		self.strokes = strokeList
		self.name = name
		self.attackingStatus = 0
		self.strokeImage = 0

	def attacking(self):
		if not self.isDefeated():
			if self.attackingStatus == 0:
				self.strokeImage = self.strokeImage + 1
				self.attackingStatus = 1

	def attack(self,stroke):
		if isSimilar(self.strokes[self.curStroke],stroke):
			self.strokeImage = self.strokeImage + 1
			self.curStroke = self.curStroke + 1
			self.attackingStatus = 0

	def isDefeated(self):
		return self.curStroke == len(self.strokes)

	def update(self):
		self.image = self.curImages[self.strokeImage]

	def kill(self):
		if self.isDefeated():
			pygame.sprite.Sprite.kill(self)

def loadEnemies():
	f = open('Enemies.json','r')
	fileContent = f.read()
	return json.loads(fileContent)['kanjis']

def getEnemy():
	"""Get a random enemy from the list of kanji."""
	kanjiList = loadEnemies()
	nKanjis = len(kanjiList)
	newEnemy = kanjiList[randrange(nKanjis)]
	strokes = []
	for posList in newEnemy['strokes']:
		stroke = Stroke(None)
		for pos in posList:
			stroke.addPos(pos)
		strokes.append(stroke)
	return Enemy(newEnemy['id'],strokes,newEnemy['name'])

