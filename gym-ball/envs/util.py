from rect import *

def convert_to_rect(str_coords):
	list_coords = str_coords.split(':')
	list_coords = [int(x) for x in list_coords]
	
	box = Rect(list_coords[0], list_coords[1], list_coords[2], list_coords[3])
	return box

def intersection_over_union(boxA, boxB):
		boxA = [boxA.top, boxA.left, boxA.bottom, boxA.right]
		boxB = [boxB.top, boxB.left, boxB.bottom, boxB.right]

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