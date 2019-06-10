
import numpy as np
import cv2

d=20
i=cv2.imread('Screenshot_2.png')
while (d!=2):
    print("in while",d)

    d-=1
rows,columns,channels=i.shape
array=[0,0]
c=rows


'''''
for num in range(0,rows) :

    for j in range(columns) :
        #print("found")
        c-=1
        #if c==-20 :
           # break
'''
print(c)




