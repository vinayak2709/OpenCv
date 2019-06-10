import numpy as np
import cv2
import matplotlib as plt
#from PILasOPENCV import Image


i2 = cv2.imread('p3.png')
i = cv2.imread('p3.png')
#img = Image.open('p3.png')
#croppedImage = img.crop((100,100,240,200))

cv2.imshow('original image',i)

crop = i[100:500 ,250:400]           # array pixels to be cropped
i2[100:500 ,250:400] = [0,0,0]        #same time throgh i2 same array size is made 0 i.e black

croppedImage = cv2.cvtColor(crop,cv2.COLOR_BGR2RGB)   # cropping

cv2.imshow('cropped image',croppedImage)
cv2.imshow('orginalImageRemain',i2)


cv2.imwrite('cropped_image.jpg',croppedImage)
cv2.imwrite('orginalImageRemain.jpg',i2)


cv2.waitKey(0)
cv2.destroyAllWindows()