# 2-Playing a video file through camera making it gray write at same time

import numpy as np
import cv2
import os

# capture video
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

cap = cv2.VideoCapture('rtsp://admin:admin123@192.168.0.10:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif')

# to write video in pycharm folder

fou = cv2.VideoWriter_fourcc(*'XVID')
ou = cv2.VideoWriter('MyOutput.avi',fou,20.0 ,(640,480))
while True :
    ret,fram = cap.read()                           #reading video
    ou.write(fram)                                  # continuosly writing
    #gr = cv2.cvtColor(fram , cv2.COLOR_BGR2GRAY)    # converting video into gray
    cv2.imshow('frm',fram)


    if cv2.waitKey(50) & 0xFF == ord('q'):          #it will get terminate after 50ms or q press

        break
cap.release()
ou.release()
cv2.destroyAllWindows()                            #it will close all windows running
