import numpy as np
import cv2
import random

def move_left(c,amt):
	(x,y) = c
	return (x-amt,y)

def move_right(c,amt):
	(x,y) = c
	return (x+amt,y)


def move_up(c,amt):
	(x,y) = c
	return (x,y-amt)

def move_down(c,amt):
	(x,y) = c
	return (x,y+amt)

def check_bounds(c):
	(x,y) = c
	return (x>=100 and y>=100 and x<=1000 and y<=1000)

def perform_action(action,c,amt):
	if (action==0):
		return move_left(c,amt)

	elif (action==1):
		return move_right(c,amt)

	elif (action==2):
		return move_up(c,amt)

	elif (action==3):
		return move_down(c,amt)





def create(start, number_images, amt, radius, num_steps,file_name):
	count = 1
	(u,l) = num_steps
	f = open(file_name, 'w')
	while (True):
		number_steps = random.randint(u,l)
		action = random.randint(0,3)
		for i in range(number_steps):
			temp = perform_action(action,start,amt)
			print temp
			if not check_bounds(temp):
				break

			start = temp
			img = np.zeros((1024,1024,3), np.uint8)
			cv2.circle(img,start, radius, (0,0,255), -1)
			cv2.imwrite("./images2/img"+str('%03d' % count)+".png",img)
			(x,y) = start
			f.write(str(x-radius)+":"+str(y-radius)+":"+str(x+radius)+":"+str(y+radius)+"\n")
			count+=1
			if(count==number_images):
				f.close()
				return

if __name__ == "__main__":
	start = (100,100)
	number_images = 500
	amt = 35
	radius = 20
	num_step = (5, 10)
	file_name = "../data/coordinate-log.txt"
	create(start, number_images, amt, radius, num_step, file_name)
		