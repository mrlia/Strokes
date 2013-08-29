import Leap, sys, pygame, math
from Leap import SwipeGesture
from Enemies import *
from Stroke import *
from image import *
from sound import *
from resources import *
from score import *

class GameState:
	"""Manage the state of the game and its enemies."""
	enemy = None
	def __init__(self):
		self.enemy = getEnemy()

	def attacking(self):
		if not(self.enemy.isDefeated()):
			self.enemy.attacking()

	def attack(self,stroke):
		"""Attack the enemy with a stroke and check if it's defeated."""
		self.enemy.attack(stroke)
		print "%s Attacked!!!!" % self.enemy.name
		if self.enemy.isDefeated():
			pygame.time.wait(1000)
			self.enemy.kill()
			score.addPoint(self.enemy.name)
			print "Enemy %s defeated!!!!" % self.enemy.name
			self.enemy = getEnemy()

class GameListener(Leap.Listener):
	"""Listener for the Leap gestures."""
	curStroke = None
	gameState = None
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
			#Get the x and y positions of the swipe
			positionList = swipe.position.to_tuple()
			curPos = [int(positionList[0]+500),int(math.fabs(positionList[1]-500))]
			#If it's the beginning of the swipe, create a new Stroke
			if swipe.state == Leap.Gesture.STATE_START:
				self.curStroke = Stroke(curPos)
			#If it's the same swipe, add the new position to the current stroke
			elif swipe.state == Leap.Gesture.STATE_UPDATE:
				self.curStroke.addPos(curPos)
				self.gameState.attacking()
			#If it's the end of the swipe, check if the swipe was correct
			elif swipe.state == Leap.Gesture.STATE_STOP:
				self.gameState.attack(self.curStroke)

			self.curStroke.draw(screen)
			pygame.display.flip()


def main():
	pygame.init()
	init_window()
	init_background()
	
	all = pygame.sprite.Group()
	Score.containers = all
	Enemy.containers = all
	
	# Load the images of the sprites
	load_game_images()

	# Create the game state manager
	gameState = GameState()

	# Create a game listener, controller and init pygame
	listener = GameListener()
	listener.gameState = gameState
	controller = Leap.Controller()
	# Have the game listener receive events from the controller
	controller.add_listener(listener)

	global score
	score = Score()
	all.add(score)
	global QUIT
	QUIT = 0

	clock = pygame.time.Clock()
	while not QUIT:
		# Set the fps.
		timePassed = clock.tick(50)
		
		# Check if the player wants to quit
		for event in pygame.event.get():
			if event.type == QUIT or \
				(event.type == KEYDOWN and event.key == K_ESCAPE):
					controller.remove_listener(listener)
					return

		# Delete all the Sprites from the screen and update them
		all.clear(get_screen(), get_background())
		all.update()
	
		update_screen()
		dirty = all.draw(get_screen())
		pygame.display.flip()
	
	# Remove the game listener when done
	controller.remove_listener(listener)


if __name__ == "__main__":
	main()
