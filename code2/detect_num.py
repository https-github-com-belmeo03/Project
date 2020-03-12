import cv2 
import numpy as np

image = cv2.imread("number/img2.png")
# arr = []
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(image, 10, 250)
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
sorted_ctrs = sorted(cnts, key=lambda cnts: cv2.boundingRect(cnts)[0])
idx=0
for i, ctr in enumerate(sorted_ctrs):
    x, y, w, h = cv2.boundingRect(ctr)
    if w>35 and h>40 : 
        if w<50 and h<55 : 
    # if w>0 and h>0 : 
            print(x, y, w, h)
            idx=+1
            new_img=gray[y:y+h,x:x+w]
            cv2.imwrite("code2/num/img"+ str(i) + '.png', new_img)