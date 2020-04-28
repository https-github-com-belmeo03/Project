import cv2 
import numpy as np

# image = cv2.imread("testbug/re/img231.png")
image = cv2.imread("testscane/img1.png") 
# arr = []
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(image, 10, 250)

dst = cv2.fastNlMeansDenoising(image, None, 10, 10, 100) 
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
idx = 0
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    
   
    print( x,y,w,h)
    if w>40 and h>60 :
        if w<55 and h<70 : 

            idx+=1
            new_img=image[y:y+h,x:x+w]
            cv2.imwrite("testscane/img"+ str(idx) + '.png', new_img)