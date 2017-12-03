import cv2

class Video:

	def __init__(self, path="./vid1.mp4"):
		self.cap = cv2.VideoCapture(path)
		while not self.cap.isOpened():
			self.cap = cv2.VideoCapture(path)
			cv2.waitKey(1000)
			print "Wait for the header"

		self.pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)

	def get_fps(self):
		return self.cap.get(cv2.cv.CV_CAP_PROP_FPS)

	def reset_playing(self):
		self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
		self.pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)

	def start_playing_from(self, index):
		self.cap.set(cv2.CAP_PROP_POS_FRAMES, index)
		self.pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)


	def grab_frame(self, enclosing_window):
		left_coord = (enclosing_window.top, enclosing_window.left)
		right_coord = (enclosing_window.bottom, enclosing_window.right)

		while  True:
			flag, frame = self.cap.read()

			if flag:
				# The frame is ready and already captured, so let's draw enclosing window
				cv2.rectangle(frame,left_coord,right_coord,(0,255,0),3)
				# cv2.imshow('video', frame)
				#cv2.imwrite('video.png', frame)

				#update the index of next frame to be read
				self.pos_frame = self.cap.get(cv2.CAP_PROP_POS_FRAMES)
				#print str(pos_frame)+" frames"
				return frame
				
			else:
				# The next frame is not ready, so we try to read it again
				self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.pos_frame-1)

				print "frame is not ready"
				# It is better to wait for a while for the next frame to be ready
				cv2.waitKey(1000)

			if cv2.waitKey(10) == 27:
				break
			if self.cap.get(cv2.CAP_PROP_POS_FRAMES) == self.cap.get(cv2.CAP_PROP_FRAME_COUNT):
				# If the number of captured frames is equal to the total number of frames,
				# we stop
				raise Exception("Video is finished.")
				break
