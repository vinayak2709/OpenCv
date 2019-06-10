import numpy as np
import cv2

img = cv2.imread('Screenshot_2.png', cv2.IMREAD_COLOR)

# FOR COLOR VALUE OF PERTICULAR PIXEL

px = img[55, 55]
print(px)

# to change color of that Pixel

img[55, 55] = [255, 255, 255]
print(px)

# Region of imgage

roi = img[100:150, 100:150]
print(roi)

# to change roi to black

#img[300: 800 , 100 : 500] = [0, 0, 0]
img[300,300] =[0,0,0]
img[300,301] =[0,0,0]
img[300,302] =[0,0,0]
img[300,303] =[0,0,0]
img[300,304] =[0,0,0]
img[300,305] =[0,0,0]
img[300,306] =[0,0,0]
img[300,307] =[0,0,0]
img[300,308] =[0,0,0]
img[300,309] =[0,0,0]
img[300,310] =[0,0,0]
img[300,311] =[0,0,0]
img[300,312] =[0,0,0]
img[301,300] =[0,0,0]
img[302,300] =[0,0,0]
img[303,300] =[0,0,0]
img[304,300] =[0,0,0]
img[305,300] =[0,0,0]
img[306,300] =[0,0,0]
img[307,300] =[0,0,0]
img[308,300] =[0,0,0]





#to change region of image by patch of same image

#watch_face = img[50:500, 150:700]
# 500 -50=450 ,700-150=550
#img[0:450,0:550]= watch_face
#for i in range(0,rows) :
    #for j in range(0,columns) :
       # if img [i,j]==[0,0,0]
cv2.imshow('operatedImage', img)
           # break
cv2.waitKey(0)
cv2.destroyAllWindows()
