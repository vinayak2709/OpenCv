import numpy as np
import cv2
#image read

img = cv2.imread('Screenshot_2.png', cv2.IMREAD_COLOR)

#to draw circle on the imgae
cv2.circle(img,(200,200),70,(0,0,255),3)
#         (img,centre ,radius ,color,thickness=None,lineType=None)  if thickness=-1 then circle get filled otherwise empty

cv2.imshow('draw',img)                 #show imagev and drawn things on it

#wait for undefinite time for key stroke
cv2.waitKey(0)
cv2.destroyAllWindows()
