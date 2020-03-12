import cv2 
import numpy as np



def sumPixel(image,h,w):
    total_img = []
    score = 0
    for i in range (0,w,+1):
        for j in range (0,h,+1):
            if i == 0:  
                image[j][i] = 0 
            if i == w-1:
                image[j][i] = 0  
    # print(total_img)
    # cv2.imshow("dfydfg",image)
    # cv2.waitKey(0)
    return image


image = cv2.imread("box/img2.png")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
(thresh, binary) = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
dst = cv2.fastNlMeansDenoising(binary, None, 10, 10, 100) 
edged = cv2.Canny(image, 10, 250)
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
idx = 0
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    if w>100 and h>150 :
        # print( x,y,w,h)
        if w<150 and h<200 :
            idx+=1
            new_img=dst[y:y+h,x:x+w]
            cv2.imwrite("score/img"+ str(idx) + '.png', new_img)
