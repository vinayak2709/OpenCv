import numpy as np

import cv2

cap = cv2.VideoCapture(0)
while True :
    ret,frame = cap.read()

    #to convert video into grayscale video
    gr = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    cv2.imshow('frm',frame)
    cv2.imshow('grayyy', gr)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
