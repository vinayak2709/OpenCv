import numpy as np
import cv2


i=cv2.imread('Screenshot_2.png')

rows,columns,channels=i.shape
matrix=cv2.getRotationMatrix2D((rows/2,columns/2),27,0.7)
print(matrix)
out1= cv2.warpAffine(i,matrix,(columns,rows))

rows,columns,channels=i.shape
matrix=cv2.getRotationMatrix2D((rows/2,columns/2),90,0.7)
print(matrix)
out2= cv2.warpAffine(i,matrix,(columns,rows))
array = i[0:rows]



if px

cv2.imshow('original',i)
cv2.imshow('UnknownRotaion',out1)
cv2.imshow('90Rotaion',out2)



cv2.waitKey(0)
cv2.destroyAllWindows()