import numpy as np
import cv2
#image read

img = cv2.imread('Screenshot_2.png', cv2.IMREAD_COLOR)

#to draw line on the imgae

cv2.line(img,(0,0),(100,100),(255,0,0))

cv2.imshow('draw',img)                 #show imagev and drawn things on it

#wait for undefinite time for key stroke
cv2.waitKey(0)
cv2.destroyAllWindows()
