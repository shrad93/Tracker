import skvideo.io
import numpy as np
from PIL import Image, ImageDraw
import pdb

class Video:

	def __init__(self, path="./vid1.mp4"):
		self.path = path
		self.cap = skvideo.io.vreader(path)
		self.metadata =  skvideo.io.ffprobe(path)['video']

	def get_fps(self):
		rate = self.metadata['@r_frame_rate']
		rate = rate.split('/')
		#pdb.set_trace()
		return float(rate[0])*1.0/float(rate[1])

	def get_height(self):
		return int(self.metadata['@height'])

	def get_width(self):
		return int(self.metadata['@width'])

	def reset_playing(self):
		self.cap = skvideo.io.vreader(self.path)

	def draw_rect_frame(self, frame, enclosing_window):
		left_coord = (enclosing_window.top, enclosing_window.left)
		right_coord = (enclosing_window.bottom, enclosing_window.right)

		img = Image.fromarray(frame)
		draw = ImageDraw.Draw(img)
		draw.rectangle([left_coord, right_coord], outline = (0,255,0))
		frame = np.asarray(img)

		return frame

	def grab_frame(self):
		frame = next(self.cap, None)
		if frame is not None:
			return frame
		else:
			# if frame is None we stop
			raise Exception("Video is finished.")
		
