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

# to change roi

img[10: 150 , 10 : 150] = [0, 0, 0]

cv2.imshow('operatedImage', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
