# 2-Playing a video file through camera making it gray write at same time

import numpy as np
import cv2
import os

# capture video

cap = cv2.VideoCapture(0)

# to write video in pycharm folder

fou = cv2.VideoWriter_fourcc(*'XVID')
ou = cv2.VideoWriter('Output.avi',fou,20.0 ,(640,480))
while True :
    ret,fram = cap.read()                           #reading video
    ou.write(fram)                                  # continuosly writing
    gr = cv2.cvtColor(fram , cv2.COLOR_BGR2GRAY)    # converting video into gray
    cv2.imshow('frm',fram)
    cv2.imshow('grayyy', gr)                        #showing output video
    if cv2.waitKey(50) & 0xFF == ord('q'):          #it will get terminate after 50ms or q press

        break
cap.release()
ou.release()
cv2.destroyAllWqindows()                            #it will close all windows running
