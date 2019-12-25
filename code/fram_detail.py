import cv2
import numpy as np

img = cv2.imread("number/img60.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
Height6, Width6 = gray.shape
print(Height6, Width6)
Rows6 = Height6
Cols6 = Width6

SumPixel_HNo1 = np.array([Cols6 - (y / 255) for y in gray.sum(axis=1)])
Egde_cut1 = gray[6:Height6 - 6, 6:Width6 - 6] 

cv2.imshow("asd",Egde_cut1)
cv2.waitKey(0)

