import cv2 
import numpy as np

image = cv2.imread("clear_image/img0.png")
# arr = []
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
backgroundImg = np.zeros((50, 50), dtype=np.uint8)

h,w = gray.shape
start_W_position = int(25-(w/2))
start_H_position = int(25-(h/2))
print(h,w)
print("------")
for i in range(0,h,+1):
    for j in range(0,w,+1):
     print(i+start_H_position,j+start_W_position)
     backgroundImg[i+start_H_position][j+start_W_position]=gray[i][j]
imgResize = cv2.resize(backgroundImg,(28,28))

cv2.imshow("sad",imgResize)
# cv2.imwrite("111"+'.png',backgroundImg)
cv2.waitKey(0)
# print(h,w)