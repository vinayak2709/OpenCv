import numpy as np
import cv2
#image read

img = cv2.imread('Screenshot_2.png', cv2.IMREAD_COLOR)

#to draw rectangle on the imgae
cv2.rectangle(img,(100,100),(500,500),(0,255,0),(8))
#         ( img  ,point1,   point2,     color,thikness,lineType=none,Shift=None)
#if thickness=-1 then Rectangle get filled otherwise empty

cv2.imshow('draw',img)                 #show imagev and drawn things on it

#wait for undefinite time for key stroke
cv2.waitKey(0)
cv2.destroyAllWindows()
