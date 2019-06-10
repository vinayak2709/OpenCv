import cv2
import numpy as np
import matplotlib as plt


i= cv2.imread('p3.png')

fx =cv2.flip(i,0)                #flip along x axis
fy =cv2.flip(i,1)                #flip along y axis
fxy =cv2.flip(i,-1)              #flip along both x &y axis

#plt.subplot(231)
cv2.imshow('fx',fx)
#plt.title(("fliped along x"))
#plt.subplot(232)
cv2.imshow('fy',fy)
#plt.title(("fliped along y"))
#plt.subplot(233)
cv2.imshow('fxy',fxy)
#plt.title(("fliped along xy"))
#plt.show()
cv2.imwrite('flippedAlong_X.jpg',fx)
cv2.imwrite('flippedAlong_Y.jpg',fy)
cv2.imwrite('flippedAlong_X_&_Y.jpg',fxy)
cv2.waitKey(0)
cv2.destroyAllWindows()