class Enemy:
	"""This class represents the kanji enemies, with the name and stroke list."""
	strokes = []
	name = ""
	curStroke = 0
	def __init__(self,strokeList,name):
		self.strokes = strokeList
		self.name = name

	def attack(self,stroke):
		if isSimilar(self.strokes[self.curStroke],stroke):
			self.curStroke = self.curStroke + 1

	def isDefeated(self):
		return self.curStroke == len(self.strokes)

    def draw(self):
        print "I´m drawing " + self.name

def loadEnemies():
	f = open('Enemies.json','r')
	fileContent = f.read()
	kanjiList = json.loads(fileContent)['kanjis']

def getEnemy():
	"""Get a random enemy from the list of kanji."""
	nKanjis = len(kanjiList)
	newEnemy = kanjiList[randrange(nKanjis)]
	strokes = [Stroke(newEnemy['id'],newEnemy['strokes'])]
	return Enemy(strokes,newEnemy['name'])

