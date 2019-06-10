import numpy as np
import cv2
import matplotlib as plt

i = cv2.imread('p3.png')

h,w,d =i.shape
wSc=500
imgScale = wSc/w

newX ,newY = i.shape[1]*imgScale,i.shape[0]*imgScale
newImage = cv2.resize(i,(int(newX),int(newY)))

cv2.imshow("orgnal image",i)
cv2.imshow("Resized image",newImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

