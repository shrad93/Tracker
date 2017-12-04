import cv2
import argparse
import os

# Construct the argument parser and parse the arguments

# Arguments
dir_path = 'images/'
ext = 'png'
output = 'out.m4v'

images = []
for f in os.listdir(dir_path):
    if f.endswith(ext):
        images.append(f)
        print f

image_path = os.path.join(dir_path, images[0])
frame = cv2.imread(image_path)
height, width, layers = frame.shape


video = cv2.VideoWriter('video.m4v',-1,1,(width,height))

for i in range(len(images)):
	image_path = os.path.join(dir_path, images[i])
	temp = cv2.imread(image_path)
	video.write(temp)

cv2.destroyAllWindows()
video.release()