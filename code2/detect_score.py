from cv2 import cv2
import numpy as np

image = cv2.imread("testscane/img.png")
# arr = []
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
(thresh, Img_First) = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)


w,h = Img_First.shape
print(w,h) 
UpperAndLower_Cut = Img_First[0 : w,900:h]
print(UpperAndLower_Cut)
# cv2.imshow("sad",UpperAndLower_Cut)
# UpperAndLower_Cut2 = Img_First[0 : 680,0:w]
# img = cv2.resize(UpperAndLower_Cut2,(1234,340))
cv2.imwrite("testscane/img3.png",UpperAndLower_Cut)

cv2.waitKey(0)
