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
		self.images = assembleSprites((160,120), (3,1),'data','uno.png')
		self.image = self.images[self.id]
		self.rect = self.image.get_rect(center=(200,200))
		self.strokes = strokeList
		self.name = name

	def attack(self,stroke):
		if isSimilar(self.strokes[self.curStroke],stroke):
			self.curStroke = self.curStroke + 1

	def isDefeated(self):
		return self.curStroke == len(self.strokes)

	def update(self):
		if self.isDefeated():
			self.image = self.images[self.id+2]
		else:
			self.image = self.images[self.id+1]

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

