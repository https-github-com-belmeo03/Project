import cv2
import numpy as np
import fuction_image

image = cv2.imread("code/img3.png")
gray  = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
(thresh, Img_First) = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
cv2.imshow("asd",Img_First)]
cv2.waitKey(0)
Height,Width = Img_First.shape
print(Height,Width)

Rows=Height
Cols=Width

SumPixel_H = np.array([Cols-(y/255) for y in Img_First.sum(axis=1)])

print(SumPixel_H)