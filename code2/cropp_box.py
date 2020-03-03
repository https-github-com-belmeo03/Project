import cv2
import numpy as np
# import fuction_image

image = cv2.imread("bi5.png")
gray  = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
(thresh, Img_First) = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)


Height5,Width5 = Img_First.shape
Rows5 = Height5
Cols5 = Width5
SumPixel_HNo = np.array([Cols5-(y/255) for y in Img_First.sum(axis=1) ])
# print(SumPixel_HNo)
HNo = len(SumPixel_HNo)


Egde_cut = Img_First[5:Height5-5,10:Width5-5]
cv2.imshow("sad",Egde_cut)
cv2.imwrite("testbi"+'.png',Egde_cut)
cv2.waitKey(0)