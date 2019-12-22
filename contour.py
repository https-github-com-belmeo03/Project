import cv2
import numpy as np

img = cv2.imread("9.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
(thresh, Img_First) = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
#cv2.imshow("imaB",Img_First)
#cv2.waitKey(0)
#กำหนดให้ widthคือความกล้าง และ heightคือความสูง  แล้วให้ rows คือหาค่าในแนวนอนของความสูง และ cols คือหาค่าในแนวตั้งของความกว้าง---------------------------
Height,Width = Img_First.shape
Rows=Height
Cols=Width
SumPixel_H = np.array([Cols-(y/255) for y in Img_First.sum(axis=1)])#หาผลรวมของpixelสีดำในแนวcols

#---------Procecsที่เอาไว้หาค่าpixelสีดำแล้วเก็บตำแหน่งทั้งข้างบนและข้างล่างครั้งแรก--------------------------------------------------
Spec_HolBegin = 0
Spec_HolEnd = 0

Hol = len(SumPixel_H)

for SpScore in range(0,Hol,+1):
   if SumPixel_H[SpScore]==0:
        SpScore = +1
   else:
      Spec_HolBegin=+SpScore
      break

for SpScore in range(Spec_HolBegin,Hol,+1):
   if SumPixel_H[SpScore] !=0:
        SpScore = +1
   else:
      Spec_HolEnd=+SpScore
      break



UpperAndLower_Cut = Img_First[Spec_HolBegin : Spec_HolEnd,0:Width] #ตัดพื้นที่ว่างทั้ง บน และ ล่าง ออก

#cv2.imshow("dectScore",UpperAndLower_Cut)
#cv2.waitKey(0)

#------------------------------------------------------ตัดแนวตั้งช่องคะแนน----------------------------------------------------------#

Height3,Width3 = UpperAndLower_Cut.shape
Rows3=Height3
Cols3=Width3
SumPixel_Ver = np.array([Rows3-(y/255) for y in UpperAndLower_Cut.sum(axis=0)])#หาผลรวมของpixelสีดำในแนวcols


Spec_VerBegin = 0
Spec_VerEnd = 0

Ver = len(SumPixel_Ver)

for SpScore1 in range(Spec_VerEnd,Ver,+1):
   if SumPixel_Ver[SpScore1]==0:
        SpScore1 = +1
   else:
      Spec_VerBegin=+SpScore1
      break

for SpScore1 in range(Spec_VerBegin,Ver,+1):
   if SumPixel_Ver[SpScore1]!=0:
        SpScore1 = +1
   else:
      Spec_VerEnd=+SpScore1
      break



LAndR_Cut = UpperAndLower_Cut[0:Height3,Spec_VerBegin:Spec_VerEnd] #ตัดพื้นที่ว่างทั้ง บน และ ล่าง ออก


#cv2.imshow("cut_Score",LAndR_Cut)
#cv2.waitKey(0)

#-------------------------------------------------คัดกรอบบนล่างช่องคะแนน-------------------------------------------------------#

Height5,Width5 = LAndR_Cut.shape
Rows5 = Height5
Cols5 = Width5
SumPixel_HNo = np.array([Cols5-(y/255) for y in LAndR_Cut.sum(axis=1) ])
#print(SumPixel_HNo)
HNo = len(SumPixel_HNo)


Egde_cut = LAndR_Cut[5:Height5-5,5:Width5-5]
#cv2.imshow("asd",Egde_cut)
#cv2.waitKey(0)

#----------------------------------------------ตัดเลขแนวนอนช่องคะแนน-----------------------#
Height7,Width7 = Egde_cut.shape
Rows7=Height7
Cols7=Width7
SumPixel_HNoScore = np.array([Cols7-(y/255) for y in Egde_cut.sum(axis=1)])



NoScore_Begin =0
NoScore_End =0
HNoScore = len(SumPixel_HNoScore)

for NoSc in range (0,HNoScore,+1):
    if SumPixel_HNoScore[NoSc]==0:
        NoSc = +1
    else:
        NoScore_Begin =+ NoSc
        break

for NoSc in range(NoScore_Begin,HNoScore,+1):
    if SumPixel_HNoScore[NoSc]!=0:
        NoSc=+1
    else:
        NoScore_End=+NoSc
        break

NoCut_H = Egde_cut[NoScore_Begin-3:NoScore_End+3,0:Width7]
#cv2.imshow("suhiukhbis",NoCut_H)
#cv2.waitKey(0)

#---------------------------------ตัดเลขแล้วตั้งช่องคะแนน------------------------------#
Height8,Width8= NoCut_H.shape

Rows8=Height8
Cols8=Width8
SumPixel_VerNoScore = np.array([Rows8-(y/255) for y in NoCut_H.sum(axis=0)])#หาผลรวมของpixelสีดำในแนวcols


NoScore_End1 = 0
NoScore_Begin1 = 0

VerNo = len(SumPixel_VerNoScore)

for NoSc1 in range(NoScore_End1,VerNo,+1):
   if SumPixel_VerNoScore[NoSc1]==0:
        NoSc1 = +1
   else:
       NoScore_Begin1=+NoSc1
       break

for NoSc1 in range(NoScore_Begin1,VerNo,+1):
   if SumPixel_VerNoScore[NoSc1]!=0:
       NoSc1 = +1
   else:
       NoScore_End1=+NoSc1
       break

NoCut_Ver = NoCut_H[0:Height8,NoScore_Begin1-3:NoScore_End1+3] #ตัดพื้นที่ว่างทั้ง บน และ ล่าง ออก
cv2.imshow("No",NoCut_Ver)

cv2.waitKey(0)


HeightBlack,WidthBlack = NoCut_Ver.shape

print("H : "+ str(HeightBlack)+"  W : "+str(WidthBlack))


for i in range (0,HeightBlack,+1):
    for j in range (0,WidthBlack,+1):
        if NoCut_Ver[i][j]==255:
            NoCut_Ver[i][j]=0
        else:
            NoCut_Ver[i][j]=255
       # print(Img_First[i][j])
cv2.imshow("sad",NoCut_Ver)
#cv2.imwrite("0000.png",Img_First)
cv2.waitKey(0)



