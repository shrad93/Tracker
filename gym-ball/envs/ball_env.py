import gym

from gym import error, spaces, utils
from gym.utils import seeding

import os
from util import *
from rect import *
from video_sk import *  #or from video import * (if opencv works on your system)
import configparser

#import cv2
import matplotlib.pyplot as plt
import scipy.misc
import pdb

config = configparser.ConfigParser()
config.read('/mnt/c/Users/Shradha/Documents/SicunGao/gym/gym/envs/ball/config.ini')


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

		
		
		self.velocity = 35*5  		#TODO: set value of velocity = amt*fps


		self.state = None #represents previous frame
		self.window_coordinates = None
		self.count = 0
		

		coord_f = open(str(config['video']['coordinate']),"r")
		self.coordinate_logs = coord_f.readlines()

		self.render_path = str(config['render']['path'])
		

	def _step(self, action):
		done = False
		#since we are taking an action, we will grab the next frame from moving ball video
		try:
			next_frame = self.video.grab_frame()

			#In one unit of action in a frame, the shift would be velocity/fps
			shift = self.velocity/self.fps
			if action == 0: #up
				self.window_coordinates.move_up(shift)
			elif action == 1: #down
				self.window_coordinates.move_down(shift)
			elif action == 2: #left
				self.window_coordinates.move_left(shift)
			elif action == 3: #right
				self.window_coordinates.move_right(shift)
				

			#draw this enclosing window on the frame grabbed above
			observation = self.video.draw_rect_frame(next_frame, self.window_coordinates)
			self.state = observation
			
			self.count += 1
			
			reward = self._reward(next_frame, self.window_coordinates)
			
			if self.count % self.episode_length == 0:
				done = True

			return observation, reward, done, {}

		except Exception, e:
			print "in catch block"
			done = True

	def _reset(self):
		#grab the very first frame the set enclosing window correctly
		# self.count = 0
		self.video.reset_playing()
		self.count = 0

		frame = self.video.grab_frame()

		self.window_coordinates = convert_to_rect(self.coordinate_logs[self.count]) #initiallize with ground truth 
		frame = self.video.draw_rect_frame(frame, self.window_coordinates)

		self.state = frame

		return frame

	def _reward(self, frame, window_coordinates):
	
		reward = 0
		if self.count % self.reward_step == 0:
			ground_truth = convert_to_rect(self.coordinate_logs[self.count])
			reward = intersection_over_union(ground_truth,window_coordinates)

		return reward

	def _render(self, mode='human', close=False):
		frame = self.state

		if frame is None:
			return 

		#cv2.imshow('video', frame), if cv2 works on your system
		plt.imshow(frame)

		filepath = self.render_path+str(self.count)+'.jpg'
		scipy.misc.imsave(filepath, frame)


		return frame


	









