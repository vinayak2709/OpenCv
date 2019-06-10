import numpy as np
import cv2
#image read

img = cv2.imread('Screenshot_2.png', cv2.IMREAD_COLOR)

#to draw line on the imgae

cv2.line(img,(0,0),(100,100),(255,0,0))

#to draw rectangle on the imgae
cv2.rectangle(img,(100,100),(500,500),(0,255,0),(8))

#to draw circle on the imgae
cv2.circle(img,(200,200),70,(0,0,255),3)

#producing array of points to give arguments to draw polyygon

pts = np.array([[1000,500],[100,100],[1000,200],[500,100],[700,40]],np.int32)

#to draw polygon on the imgae

cv2.polylines(img,[pts],True , (0,0,0),(5))

# to write fonts ,sentences on image
font =cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,' HEY I am Vinayak ,I have done this !',(5,300), font,2,(100,250,150),2,cv2.LINE_AA)
#            img          - msg to write            start pt,fontData,fontType,color ,thicknes ,.)

cv2.imshow('draw',img)                 #show imagev and drawn things on it

#wait for undefinite time for key stroke
cv2.waitKey(0)
cv2.destroyAllWindows()
