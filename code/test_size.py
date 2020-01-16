import cv2
import numpy as np

def frame_detail(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    Height6, Width6 = gray.shape
    # print(Height6, Width6)
    Rows6 = Height6
    Cols6 = Width6

    SumPixel_HNo1 = np.array([Cols6 - (y / 255) for y in gray.sum(axis=1)])
    Egde_cut1 = gray[6:Height6 - 6, 6:Width6 - 6] 
    return Egde_cut1


def reblack(gray):
    # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
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
    return Img_First

def tem_size(gray):
    # cv2.imshow("da",gray)
    # gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    grays=gray
    h,w = grays.shape
    # print(grays)
    backgroundImg = np.zeros((30, 30), dtype=np.uint8)
    
    for i in range(0,h,+1):
        for j in range(0,w,+1):
            backgroundImg[i][j]=grays[i][j]
    
    # tem_img = backgroundImg

    return backgroundImg


img = cv2.imread("number/img60.png")

frame= frame_detail(img)
frame2= reblack(frame)
frame3= tem_size(frame2)


# cv2.imshow("da",frame3)
cv2.imwrite("temp/222"+'.png',frame3)
# cv2.waitKey(0)