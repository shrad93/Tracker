import gym

from gym import error, spaces, utils
from gym.utils import seeding
import os
from rect import *
from video_sk import *  #or from video import * (if opencv works on your system)
import configparser
config = configparser.ConfigParser()

config.read('config.ini')
#import cv2
import matplotlib.pyplot as plt
import scipy.misc
import pdb

class BallEnv(gym.Env):
	metadata = {'render.modes': ['human']}

	action_set = {'up', 'down', 'left', 'right'}
	episode_length = 25   #TODO: set length of one episode
	reward_step = 5

	def __init__(self):
		self.video_path = str(config['video']['path'])
		self.video = Video(self.video_path)
		self.fps = self.video.get_fps()
		height = self.video.get_height()
		width = self.video.get_width()


		self.action_space = spaces.Discrete(len(self.action_set))  
	
		self.observation_space = spaces.Box(low=0, high=255, shape=(height, width, 3))

		
		
		self.velocity = 300  		#TODO: set value of velocity


		self.state = None #represents previous frame
		self.window_coordinates = None
		self.count = 0
		

		f = open(str(config['video']['coordinate']),"r")
		self.coordinate_logs = f.readlines()
		

	def _step(self, action):
		done = False
		#since we are taking an action, we will grab the next frame from moving ball video
		try:
			next_frame = self.video.grab_frame()

			#In one unit of action in a frame, the shift would be velocity/fps
			if action == 0: #up
				self.window_coordinates.move_up(self.velocity/self.fps)
			elif action == 1: #down
				self.window_coordinates.move_down(self.velocity/self.fps)
			elif action == 2: #left
				self.window_coordinates.move_left(self.velocity/self.fps)
			elif action == 3: #right
				self.window_coordinates.move_right(self.velocity/self.fps)
				

			#draw this enclosing window on the frame grabbed above
			observation = self.video.draw_rect_frame(next_frame, self.window_coordinates)
			self.state = observation

			reward = self._reward(next_frame, self.window_coordinates)

			self.count += 1
			if self.count %25 == 0:
				done = True

			return observation, reward, done, {}

		except Exception, e:
			done = True

	def _reset(self):
		#grab the very first frame the set enclosing window correctly
		# self.count = 0
		self.video.reset_playing()
		frame = self.video.grab_frame()

		self.window_coordinates = Rect(300, 0, 500, 100) #TODO: find correct ground truth coordinate and update it
		frame = self.video.draw_rect_frame(frame, self.window_coordinates)

		self.state = frame

		return frame

	def _reward(self, frame, window_coordinates):
		#TODO: IOU

		reward = 0
		if self.count%reward_step ==0:
			ground_truth = self.coordinate_logs[self.count]
			ground_truth = ground_truth.split(':')
			ground_truth = [int(x) for x in ground_truth]
			object_coord = [window_coordinates.top,window_coordinates.left,window_coordinates.bottom,window_coordinates.right]
			reward = intersection_over_union(ground-truth,object_coord)


		return reward

	def _render(self, mode='human', close=False):
		frame = self.state

		if frame is None:
			return 

		#cv2.imshow('video', frame), if cv2 works on your system
		plt.imshow(frame)

		filepath = self.video_path+str(self.count)+'.jpg'
		scipy.misc.imsave(filepath, frame)


		return frame


	def intersection_over_union(boxA, boxB):
		# determine the (x, y)-coordinates of the intersection rectangle
		xA = max(boxA[0], boxB[0])
		yA = max(boxA[1], boxB[1])
		xB = min(boxA[2], boxB[2])
		yB = min(boxA[3], boxB[3])
	 
		# compute the area of intersection rectangle
		interArea = (xB - xA + 1) * (yB - yA + 1)
	 
		# compute the area of both the prediction and ground-truth
		# rectangles
		boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
		boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
	 
		# compute the intersection over union by taking the intersection
		# area and dividing it by the sum of prediction + ground-truth
		# areas - the interesection area
		iou = interArea / float(boxAArea + boxBArea - interArea)
	 
		# return the intersection over union value
		return iou









