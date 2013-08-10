import Leap, sys, pygame, math
from Leap import SwipeGesture


class SampleListener(Leap.Listener):
	curStroke = None
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
			if self.curStroke != None and self.curStroke.strokeID == swipe.id:
				self.curStroke.addPos(curPos)
			else:
				self.curStroke = Stroke(swipe.id,curPos)
			self.curStroke.draw()
			pygame.display.flip()

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

screen = pygame.display.set_mode([900,600])
def main():
	# Create a sample listener and controller
	listener = SampleListener()
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