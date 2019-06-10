import cv2
import numpy as np


i1= cv2.imread('p4.png')
i2= cv2.imread('p3.png')

height,width =i2.shape[:2]                                #returns height & width of original image
print(height)                                             #shows height value
print(width)                                              #shows width value
quarter_height ,quarter_width = height/4 ,width/4         #translation of image by height & width by 1/4th

print(quarter_height)                                     #shows height value

print(quarter_width)                                      #shows width value

#           |1  0  tx|
#       T=  |0  1  ty|
# T is translation matrix

T = np.float32([[1,0,quarter_width],[0,1,quarter_height]])

print(T)

i2_trans = cv2.warpAffine(i2,T,(width,height))             #warpAffine transformation to translate (shift) image linearly
cv2.imshow('original image',i2)
cv2.imshow('Translaton image',i2_trans)
cv2.imwrite('original_image.jpg',i2)
cv2.imwrite('Translaton_image.jpg',i2_trans)

cv2.waitKey(0)
cv2.destroyAllwindows()