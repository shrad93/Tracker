class Rect:

	def __init__(self, top, left, bottom, right):
		self.top = top
		self.left = left
		self.bottom = bottom
		self.right = right
	
	def move_up(self, amount):
		self.top -= amount
		self.bottom -= amount

	def move_down(self, amount):
		self.top += amount
		self.bottom += amount

	def move_left(self, amount):
		self.left -= amount
		self.right -= amount

	def move_right(self, amount):
		self.left += amount
		self.right += amount
