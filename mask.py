import cv2
import numpy as np

i1= cv2.imread('p3.png')
i2= cv2.imread('Screenshot_2.png')

rows,columns,channels = i2.shape     #it gives rows ,columns,channels

roi = i1[0:rows-200,0:columns-500]    #region of interest according to user requirement

im2gry = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)           #bgr 2 gray conversion

ret, mask=cv2.threshold(im2gry , 210,255 ,cv2.THRESH_BINARY_INV)
#                   source ,thresholdValue,MaxValue,...)

cv2.imshow('maskImage',mask)
cv2.imwrite('maskImage210Mask.jpg',mask)

cv2.waitKey(0)
cv2.destroyAllWindows()