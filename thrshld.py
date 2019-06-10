
#here in this program thresholding ,bitwise and,bitwise not ,bitwise or explored

import cv2
import numpy as np

i1= cv2.imread('Screenshot_2.png')
i2= cv2.imread('p3.png')

rows,columns,channels = i2.shape     #it gives rows ,columns,channels
roi = i1[0:rows ,0:columns]

im2gry = cv2.cvtColor(i2, cv2.COLOR_BGRA2GRAY)           #bgr 2 gray conversion

ret, mask=cv2.threshold(im2gry ,120,255 ,cv2.THRESH_BINARY_INV)
#                   source ,thresholdValue,MaxValue,...)


mask_inv = cv2.bitwise_not(mask)
i1_backGround = cv2.bitwise_and(roi,i2,mask=mask_inv )   #for backGround mask inv imp parameter in AND (roi or i1 doesnt matter since they are same)

i2_ForeGround = cv2.bitwise_and(i1,i2,mask=mask)        ##for foreGround mask imp parameter in AND
ore = cv2.bitwise_or(i1,i2,mask=mask)
dst = cv2.add(i1_backGround , i2_ForeGround)
#i1[0:rows, 0:columns] = dst

add = cv2.add(i1, i2)

cv2.imshow('orig',i1)
cv2.imshow('origAdd',add)
cv2.imshow('maskImage',mask)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('i1Bg',i1_backGround)
cv2.imshow('i1_fg',i2_ForeGround)
cv2.imshow('dst',dst)

cv2.imshow('or',ore)
cv2.imwrite('origAdd.jpg',add)
cv2.imwrite('maskImage.jpg',mask)
cv2.imwrite('mask_inv.jpg',mask_inv)
cv2.imwrite('i1B=roi&i2&mask_inv.jpg',i1_backGround)
cv2.imwrite('i1_fg=i1&i2&mask.jpg',i2_ForeGround)
cv2.imwrite('fgbg.jpg',dst)
cv2.imwrite('maskImage1.jpg',mask)

cv2.waitKey(0);
cv2.destroyAllWindows()