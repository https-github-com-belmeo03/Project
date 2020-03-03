
import cv2
import numpy as np

img = cv2.imread("box/img1.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
(thresh, Img_First) = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
#cv2.imshow("imaB",Img_First)
#cv2.waitKey(0)
#กำหนดให้ widthคือความกล้าง และ heightคือความสูง  แล้วให้ rows คือหาค่าในแนวนอนของความสูง และ cols คือหาค่าในแนวตั้งของความกว้าง---------------------------
Height,Width = Img_First.shape

# print("H : "+ str(Height)+"  W : "+str(Width))


for i in range (0,Height,+1):
    for j in range (0,Width,+1):
        if Img_First[i][j]==255:
            Img_First[i][j]=0
        else:
            Img_First[i][j]=255
        # print(Img_First[i][j])
cv2.imshow("sad",Img_First)
cv2.imwrite("222.png",Img_First)
cv2.waitKey(0)
