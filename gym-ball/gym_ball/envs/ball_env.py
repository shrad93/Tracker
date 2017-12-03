import gym

from gym import error, spaces, utils
from gym.utils import seeding

from rect import *
from video import *

class BallEnv(gym.Env):
  	metadata = {'render.modes': ['human']}
  	ACTION_LOOKUP = {
		0 : move_up,
		1 : move_down,
		2 : move_left,
		3 : move_right
	}

  	action_set = {'up', 'down', 'left', 'right'}
  	

	def __init__(self):
		self.action_space = spaces.Discrete(len(self.action_set))  
	
		self.observation_space = spaces.Box(low=-1, high=1)

		video_path = "./vid1.mp4";
		self.video = Video(video_path)
		self.fps = self.video.get_fps()
		self.velocity = 1  		#TODO: set value of velocity


		self.state = None
		self.window_coordinates = None
		self.count = 0

		self.viewer = None
		

	def _step(self, action):
		#since we are taking an action, we will grab the next frame from moving ball video
		try:
			next_frame = self.video.grab_frame()
			#In one unit of action in a frame, the shift would be velocity/fps
			self.window_coordinates(ACTION_LOOKUP[action](self.velocity/self.fps))

			#draw this enclosing window on the frame grabbed above
			observation = self.video.draw_rect_frame(next_frame, self.window_coordinates)

			self.count += 1

		except:
			done = True

	def _reset(self):
		#grab the very first frame the set enclosing window correctly
		self.video.reset_playing()
		frame = self.video.grab_frame()

		self.window_coordinates = Rect(0, 0, 0, 0) #TODO: find correct coordinate and update it
		frame = self.video.draw_rect_frame(frame, self.window_coordinates)

		return frame

	def _reward(self):
		#IOU
		return 0

	def _render(self, mode='human', close=False):
		...