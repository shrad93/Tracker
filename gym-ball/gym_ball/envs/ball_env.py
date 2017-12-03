import gym

from gym import error, spaces, utils
from gym.utils import seeding

from rect import *

class BallEnv(gym.Env):
  	metadata = {'render.modes': ['human']}
  	ACTION_LOOKUP = {
		0 : move_up,
		1 : move_down,
		2 : move_left,
		3 : move_right
	}

  	action_set = {'up', 'down', 'left', 'right'}
  	

	def __init__(self, fps, velocity):
		self.action_space = spaces.Discrete(len(self.action_set))  
	
		self.observation_space = spaces.Box(low=-1, high=1)

		self.fps = fps
		self.velocity = velocity
		self.state = None
		self.window_coordinates = None
		self.count = 0

		self.viewer = None
		

	def _step(self, action):
		#since we are taking an action, we will grab the next frame from moving ball video
		#TODO: screengrab from charu

		#In one unit of action in a frame, the shift would be velocity/fps
		self.window_coordinates(ACTION_LOOKUP[action](self.velocity/self.fps))

		#draw this enclosing window on the frame grabbed above
		#TODO: from charu

	def _reset(self):
		#grab the very first frame the set enclosing window correctly
		...

	def _reward(self):
		#IOU
		...

	def _render(self, mode='human', close=False):
		...