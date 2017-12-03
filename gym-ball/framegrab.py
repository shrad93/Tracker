import cv2


cap = cv2.VideoCapture("./vid1.mp4")
    while not cap.isOpened():
        cap = cv2.VideoCapture("./vid1.mp4")
        cv2.waitKey(1000)
        print "Wait for the header"

pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)

def framegrab(fps,left_coord,right_coord):
    
    
    while  True:

        flag, frame = cap.read()
        
        if flag:
            # The frame is ready and already captured
            cv2.rectangle(frame,left_coord,right_coord,(0,255,0),3)
            # cv2.imshow('video', frame)
            cv2.imwrite('video.png', frame)
            return np.array()
            pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
            print str(pos_frame)+" frames"
        else:
            # The next frame is not ready, so we try to read it again
            cap.set(cv2.CAP_PROP_POS_FRAMES, pos_frame-1)
            print "frame is not ready"
            # It is better to wait for a while for the next frame to be ready
            cv2.waitKey(1000)

        if cv2.waitKey(10) == 27:
            break
        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            # If the number of captured frames is equal to the total number of frames,
            # we stop
            break
