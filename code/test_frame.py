import cv2 
import numpy as np

image = cv2.imread("number/img39.png")
# arr = []
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(image, 10, 250)
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# sorted_ctrs = sorted(cnts, key=lambda cnts: cv2.boundingRect(cnts)[0])
idx = 0
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    print( x,y,w,h)
    if w>20 and h>20 and w<30 and h<30:
        idx+=1
        new_img=gray[y:y+h,x:x+w]
        cv2.imwrite("code/frame/img"+ str(idx) + '.png', new_img)
        