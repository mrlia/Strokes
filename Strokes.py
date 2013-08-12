import Leap, sys, pygame, math, json
from Leap import SwipeGesture
from random import randrange


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

	def draw(self):
		prevPos = self.positions[0]
		for pos in self.positions:
			pygame.draw.line(screen, (0,0,0), prevPos, pos, 3)
			prevPos = pos

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

def isSimilar(firstStroke,secondStroke):
	return True

def getEnemy():
	"""Get a random enemy from the list of kanji file."""
	f = open('Enemies.json','r')
	fileContent = f.read()
	kanjiList = json.loads(fileContent)['kanjis']
	nKanjis = len(kanjiList)
	newEnemy = kanjiList[randrange(nKanjis)]
	strokes = [Stroke(newEnemy['id'],newEnemy['strokes'])]
	return Enemy(strokes,newEnemy['name'])

class GameState:
	"""Manage the state of the game and its enemies."""
	enemy = getEnemy()

	def attack(self,stroke):
		"""Attack the enemy with a stroke and check if it's defeated."""
		self.enemy.attack(stroke)
		if self.enemy.isDefeated():
			print "Enemy %s defeated!!!!" % self.enemy.name
			self.enemy = getEnemy()

class GameListener(Leap.Listener):
	"""Listener for the Leap gestures."""
	curStroke = None
	gameState = GameState()
	def on_init(self, controller):
		print "Initialized"

	def on_disconnect(self, controller):
		# Note: not dispatched when running in a debugger.
		print "Disconnected"

	def on_exit(self, controller):
		print "Exited"

	def on_connect(self, controller):
		print "Connected"
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
		
	def on_frame(self, controller):
		"""Manage the swipe gestures that will be the strokes."""
		frame = controller.frame()
		for gesture in frame.gestures():
			#Get the swipe
			swipe = SwipeGesture(gesture)
			print swipe.position
			#Get the x and y positions of the swipe
			positionList = swipe.position.to_tuple()
			curPos = [int(positionList[0]+500),int(math.fabs(positionList[1]-500))]
			#If it's the beginning of the swipe, create a new Stroke
			if swipe.state == Leap.Gesture.STATE_START:
				self.curStroke = Stroke(swipe.id,curPos)
			#If it's the same swipe, add the new position to the current stroke
			elif swipe.state == Leap.Gesture.STATE_UPDATE:
				self.curStroke.addPos(curPos)
			#If it's the end of the swipe, check if the swipe was correct
			elif swipe.state == Leap.Gesture.STATE_STOP:
				self.gameState.attack(self.curStroke)

			self.curStroke.draw()
			pygame.display.flip()


screen = pygame.display.set_mode([900,600])
def main():
	# Create a game listener, controller and init pygame
	listener = GameListener()
	controller = Leap.Controller()
	pygame.init()
	screen.fill((0,255,255))
	pygame.display.flip()
	
	# Have the game listener receive events from the controller
	controller.add_listener(listener)
	
	# Keep this process running until Enter is pressed
	print "Press Enter to quit..."
	sys.stdin.readline()
	
	# Remove the game listener when done
	controller.remove_listener(listener)

	
if __name__ == "__main__":
	main()