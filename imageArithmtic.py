#add images

import cv2

import numpy as np

im1= cv2.imread('Screenshot_2.png',0)
im2= cv2.imread('p3.png',0)

#there are 3methods adding images but 3rd one is best one of them
#add = im1 + im2

#add = cv2.add(im1 ,im2)

add = cv2.addWeighted(im1, 0.6, im2, 0.4, 0)

cv2.imshow('add',add)
cv2.imwrite('add3rdMethod.png',add)


cv2.waitKey(0)
cv2.destroyAllWindows()