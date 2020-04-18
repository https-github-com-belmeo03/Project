
import cv2
import numpy as np

img = cv2.imread("img230.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
(thresh, Img_First) = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
#cv2.imshow("imaB",Img_First)
#cv2.waitKey(0)
#กำหนดให้ widthคือความกล้าง และ heightคือความสูง  แล้วให้ rows คือหาค่าในแนวนอนของความสูง และ cols คือหาค่าในแนวตั้งของความกว้าง---------------------------
h,w = Img_First.shape
Rows=h
Cols=w


# print(SumPixel_HNo1)
# print(w,h)
fram = 0
fram2 = 0

for i in range(0,h+1,+1):
    if i<h:
        fram += 1
    else:
        fram2 = +fram
        break

test = Img_First[fram-40:fram2+40, 0:w] 
h2,w2 = test.shape

k = h-h2
print(k)

test2 = Img_First[fram-h:fram-42, 0:w] 
cv2.imshow("asd",test2)
cv2.waitKey(0)
    


    