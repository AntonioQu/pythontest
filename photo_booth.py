from __future__ import print_function
from photoboothapp import PhotoBoothApp
from imutils.video import VideoStream
import argparse
import time


ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True, help="path to output directory to store snapshots")
ap.add_argument("-p", "--picamera", type=int, default=-1, help="path to output directory to store snapshots")
args = vars(ap.parse_args())

print("[INFO] warming up camera...")
vs = VideoStream(usePiCamera=args["picamera"]>0).start()
time.sleep(2.0)

pba = PhotoBoothApp(vs,args["output"])
pba.root.mainloop()