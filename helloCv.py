
import cv2

#image read
mg = cv2.imread('Screenshot_2.png',0)

#image display
cv2.imshow('frame',mg)

#to wait by specfied miliseconds as argument of waitKey ,0 mean indefinite time till key strke , ord('s') wait tills spresssed
k = cv2.waitKey(5000)
if k == 27 :          # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('e'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()