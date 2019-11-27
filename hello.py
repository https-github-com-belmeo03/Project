import cv2
import numpy as np

img = cv2.imread("9.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
(thresh, Img_First) = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
# cv2.imshow("imaB",Img_First)
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

# cv2.imshow("dectScore",UpperAndLower_Cut)
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
print(SumPixel_HNo)
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

NoCut_H = Egde_cut[NoScore_Begin:NoScore_End,0:Width7]
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

NoCut_Ver = NoCut_H[0:Height8,NoScore_Begin1:NoScore_End1] #ตัดพื้นที่ว่างทั้ง บน และ ล่าง ออก
#cv2.imshow("No",NoCut_Ver)

#cv2.waitKey(0)



#-------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------บนล่างช่องรหัสนักศักษา-------------------------------------------------#
Height1,Width1 = Img_First.shape
Rows1=Height1
Cols1=Width1
SumPixel_H1 = np.array([Cols1-(y/255) for y in Img_First.sum(axis=1)])#หาผลรวมของpixelสีดำในแนวcols

#---------Procecsที่เอาไว้หาค่าpixelสีดำแล้วเก็บตำแหน่งทั้งข้างบนและข้างล่างช่องรหัสนักศึกษา--------------------------------------------------
Spec_HolBegin1 = 0
Spec_HolEnd1 = 0

Hol1 = len(SumPixel_H1)

for SpCode in range(Spec_HolEnd,Hol1,+1):
   if SumPixel_H1[SpCode]==0:
        SpCode = +1
   else:
      Spec_HolBegin1=+SpCode
      break

for SpCode in range(Spec_HolBegin1,Hol1,+1):
   if SumPixel_H1[SpCode]!=0: #กำหนดพิกเซล 150 หรือ 4
        SpCode = +1
   else:
      Spec_HolEnd1=+SpCode
      break



UpperAndLower_Cut1 = Img_First[Spec_HolBegin1:Spec_HolEnd1,0:Width1] #ตัดพื้นที่ว่างทั้ง บน และ ล่าง ออก


#cv2.imshow("dectCode",UpperAndLower_Cut1)
#cv2.waitKey(0)

#-----------------------------------------------ตัดแนวตั้งช้องรหัส-------------------------------------------------------#

Height4,Width4 = UpperAndLower_Cut1.shape
Rows4=Height4
Cols4=Width4
SumPixel_Ver = np.array([Rows4-(y/255) for y in UpperAndLower_Cut1.sum(axis=0)])
Spec_VerBegin1 = 0
Spec_VerEnd1 = 0

Ver = (len(SumPixel_Ver))
count = 1
Count_NumWrite = 0


while count == 1:
 for SpCode1 in range (Spec_VerEnd1,Ver,+1):
    if SumPixel_Ver[SpCode1] == 0:
        SpCode1 = +1
    else:
        Spec_VerBegin1=+SpCode1
        break
 for SpCode1 in range (Spec_VerBegin1,Ver,+1):
    if SumPixel_Ver[SpCode1]!=0:
        SpCode1 = +1
    else:
        Spec_VerEnd1 = +SpCode1
        break

 LAndR_Cut1 = UpperAndLower_Cut1[0:Height4,Spec_VerBegin1:Spec_VerEnd1]


 Height6, Width6 = LAndR_Cut1.shape
 Rows6 = Height6
 Cols6 = Width6
 SumPixel_HNo1 = np.array([Cols6 - (y / 255) for y in LAndR_Cut1.sum(axis=1)])


 HNo1 = len(SumPixel_HNo1)

 Egde_cut1 = LAndR_Cut1[6:Height6 - 6, 6:Width6 - 6] #------------------ตัดกรอบช่องรหัส------------#

 # ---------------------------------------คัดเเนวตั้งช่องรหัส------------------------------#
 Height9, Width9 = Egde_cut1.shape

 Rows9 = Height9
 Cols9 = Width9
 SumPixel_VerNoCode = np.array([Rows9 - (y / 255) for y in Egde_cut1.sum(axis=0)])  # หาผลรวมของpixelสีดำในแนวcols

 NoCode_End1 = 0
 NoCode_Begin1 = 0

 VerNo1 = len(SumPixel_VerNoCode)

 for NoCode1 in range(NoCode_End1, VerNo1, +1):
     if SumPixel_VerNoCode[NoCode1] == 0:
         NoCode1 = +1
     else:
         NoCode_Begin1 = +NoCode1
         break

 for NoCode1 in range(NoCode_Begin1, VerNo1, +1):
     if SumPixel_VerNoCode[NoCode1] != 0:
         NoCode1 = +1
     else:
         NoCode_End1 = +NoCode1
         break

 NoCut_Ver1 = Egde_cut1[0:Height9, NoCode_Begin1:NoCode_End1]  # ตัดพื้นที่ว่างทั้ง บน และ ล่าง ออก

 #cv2.imshow("cut_Code", Egde_cut1)
 # cv2.waitKey(0)


 #cv2.waitKey(0)
 Height10, Width10 = NoCut_Ver1.shape

 Rows10 = Height10
 Cols10 = Width10
 SumPixel_HNoCode = np.array([Cols10 - (y / 255) for y in NoCut_Ver1.sum(axis=1)])  # หาผลรวมของpixelสีดำในแนวcols

 NoCode_End = 0
 NoCode_Begin = 0

 VerNo = len(SumPixel_HNoCode)

 for NoCode in range(NoCode_End, VerNo, +1):
     if SumPixel_HNoCode[NoCode] == 0:
         NoCode = +1
     else:
         NoCode_Begin = +NoCode
         break

 for NoCode in range(NoCode_Begin, VerNo, +1):
     if SumPixel_HNoCode[NoCode] != 0:
         NoCode = +1
     else:
         NoCode_End = +NoCode
         break

 NoCut_Ver = NoCut_Ver1[NoCode_Begin:NoCode_End, 0:Width10]  # ตัดพื้นที่ว่างทั้ง บน และ ล่าง ออก

 #cv2.imshow("cut_Code", NoCut_Ver)
 #cv2.waitKey(0)
 CheckArea = 0
 for i in range(Spec_VerEnd1, Ver, +1):
     if SumPixel_Ver[i] != 0:  # เช็คดูว่า ตำแหน่ง สุดท้ายของตัวอักษร ไปจนถึง ความกว้างนั้น มีตัวอักษรอีกหรือไหม
         CheckArea = 1
     else:
         i = +1

 if CheckArea==0:   #ถ้าไม่มีตัวอักษรอีก ให้ทำการเปลี่ยน Count เป็น 0
    count=0


