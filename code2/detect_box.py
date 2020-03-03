import cv2 
import numpy as np
image = cv2.imread("testbi.png")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
(thresh, binary) = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
dst = cv2.fastNlMeansDenoising(binary, None, 10, 10, 100) 
edged = cv2.Canny(image, 10, 250)
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
idx = 0
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    print( x,y,w,h)
    # if w>700 and h>200  :
    #     print( x,y,w,h)
    #     if w<1000 and h<300  :
        # if w>0 and h>0 :
    idx+=1
    new_img=dst[y:y+h,x:x+w]
    cv2.imwrite("box/img"+ str(idx) + '.png', new_img)
    # else:
    #     new_img2=dst[y:y+0,x:x+5]
    #     cv2.imwrite("box/img2" + '.png', new_img2)
# cv2.imshow("fghjk",new_img2)
# cv2.waitKey(0)


