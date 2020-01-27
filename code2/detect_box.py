import cv2 
import numpy as np
image = cv2.imread("rotation/rot.png")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(image, 10, 250)
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
idx = 0
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    print( x,y,w,h)
    if w>200 and h>200 and w<1000 and h<700:
        idx+=1
        new_img=gray[y:y+h,x:x+w]
        cv2.imwrite("box/img"+ str(idx) + '.png', new_img)
# cv2.imshow("fghjk",image)
cv2.waitKey(0)