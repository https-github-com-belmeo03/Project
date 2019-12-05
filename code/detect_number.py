import cv2 
import numpy as np
image = cv2.imread("box/img2.png")

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(image, 10, 250)
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
idx = 0
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    print( x,y,w,h)
    if w>25 and h>25 and w<70 and h<70:
        idx+=1
        new_img=gray[y:y+h,x:x+w]
        cv2.imwrite("number/img"+ str(idx) + '.png', new_img)
# cv2.imshow("fghjk",image)
cv2.waitKey(0)