# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time


vs = VideoStream(src=0).start()

# allow the camera to warm up
time.sleep(2.0)

# keep looping
while True:
    
    # grab the current frame
    frame = vs.read()

    # resize the frame, blur it, and convert it to the HSV
    # color space
    frame = imutils.resize(frame, width=200)

    
    # draw the circle and centroid on the frame,
    # then update the list of tracked points
    """cv2.circle(frame, (int(x), int(y)), int(radius),
        (0, 255, 255), 2)
    cv2.circle(frame, center, 5, (0, 0, 255), -1)"""

    # show the frame to our screen
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

vs.stop()

# close all windows
cv2.destroyAllWindows()
