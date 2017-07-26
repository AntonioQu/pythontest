##0. CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
##1. CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
##3. CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file
##4. CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
##5. CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
##6. CV_CAP_PROP_FPS Frame rate.
##7. CV_CAP_PROP_FOURCC 4-character code of codec.
##8. CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
##9. CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
##10. CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
##11. CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
##12. CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
##13. CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
##14. CV_CAP_PROP_HUE Hue of the image (only for cameras).
##15. CV_CAP_PROP_GAIN Gain of the image (only for cameras).
##16. CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
##17. CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
##18. CV_CAP_PROP_WHITE_BALANCE Currently unsupported
##19. CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)


import numpy as np
import cv2
from tkinter import *

root = Tk()
root.title("video")

cap = cv2.VideoCapture(0)

#cap.set(3,720)
#cap.set(4,720)
#cap.set(6, 24)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
