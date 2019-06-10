import cv2
import numpy as np

i1= cv2.imread('p4.png')
i2= cv2.imread('p3.png')

rows,columns,channels=i2.shape
matrix=cv2.getRotationMatrix2D((rows/2,columns/2),0,0.7)
print(matrix)
out1= cv2.warpAffine(i2,matrix,(columns,rows))

R2=cv2.getRotationMatrix2D((columns/2,rows/2),45,0.70)
print(R2)
out2= cv2.warpAffine(i2,R2,(columns,rows))

cv2.imshow('zeroRotaion',out1)
cv2.imshow('45degree Rotation',out2)

cv2.imwrite('zeroRotaion.jpg',out1)
cv2.imwrite('45Rotaion.jpg',out2)

cv2.waitKey(0)
cv2.destroyAllWindows()