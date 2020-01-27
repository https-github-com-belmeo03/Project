import cv2 
import numpy as np

image = cv2.imread("0000.png")
# arr = []
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
backgroundImg = np.zeros((30, 30), dtype=np.uint8)

h,w = gray.shape


for i in range(0,h,+1):
    for j in range(0,w,+1):

     backgroundImg[i][j]=gray[i][j]

cv2.imshow("sad",backgroundImg)
cv2.imwrite("111"+'.png',backgroundImg)
cv2.waitKey(0)
# print(h,w)