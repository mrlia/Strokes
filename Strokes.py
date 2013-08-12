import Leap, sys, pygame, math
from Leap import SwipeGesture


class Stroke:
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
	strokes = [Stroke(1,(300,400))]
	
	return Enemy(strokes,"boca")

class GameState:
	enemy = getEnemy()

	def attack(self,stroke):
		self.enemy.attack(stroke)
		if self.enemy.isDefeated():
			print "Enemy {} defeated!!!!".format(self.enemy.name)
			self.enemy = getEnemy()

class GameListener(Leap.Listener):
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
		frame = controller.frame()
		# Gestures
		for gesture in frame.gestures():
			swipe = SwipeGesture(gesture)
			print swipe.position
			positionList = swipe.position.to_tuple()
			curPos = [int(positionList[0]+500),int(math.fabs(positionList[1]-500))]
			if swipe.state == Leap.Gesture.STATE_START:
				self.curStroke = Stroke(swipe.id,curPos)
			elif swipe.state == Leap.Gesture.STATE_UPDATE:
				self.curStroke.addPos(curPos)
			elif swipe.state == Leap.Gesture.STATE_STOP:
				self.gameState.attack(self.curStroke)

			self.curStroke.draw()
			pygame.display.flip()


screen = pygame.display.set_mode([900,600])
def main():
	# Create a sample listener and controller
	listener = GameListener()
	controller = Leap.Controller()
	pygame.init()
	screen.fill((0,255,255))
	pygame.display.flip()
	
	# Have the sample listener receive events from the controller
	controller.add_listener(listener)
	
	# Keep this process running until Enter is pressed
	print "Press Enter to quit..."
	sys.stdin.readline()
	
	# Remove the sample listener when done
	controller.remove_listener(listener)

	
if __name__ == "__main__":
	main()