import math

class Rect:

	def __init__(self, top, left, bottom, right):
		self.top = top
		self.left = left
		self.bottom = bottom
		self.right = right
	
	def move_up(self, amount):
		self.top = math.floor(self.top - amount)
		self.bottom = math.floor(self.bottom - amount)

	def move_down(self, amount):
		self.top = math.ceil(self.top + amount)
		self.bottom = math.ceil(self.bottom + amount)

	def move_left(self, amount):
		self.left = math.ceil(self.left - amount)
		self.right = math.ceil(self.right - amount)
	
	def move_right(self, amount):
		self.left = math.floor(self.left + amount)
		self.right = math.floor(self.right + amount)
		