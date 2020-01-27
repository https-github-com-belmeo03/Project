import cv2 
import numpy as np

image = cv2.imread("box/img1.png")
# arr = []
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(image, 10, 250)
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
sorted_ctrs = sorted(cnts, key=lambda cnts: cv2.boundingRect(cnts)[0])
idx=0
for i, ctr in enumerate(sorted_ctrs):
    x, y, w, h = cv2.boundingRect(ctr)
    if w>25 and h>25 and w<70 and h<70: 
        print(x, y, w, h)
        idx=+1
        new_img=gray[y:y+h,x:x+w]
        cv2.imwrite("number/img"+ str(i) + '.png', new_img)