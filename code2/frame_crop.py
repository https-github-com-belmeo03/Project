import cv2
import numpy as np

img = cv2.imread("number/img34.png",0)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# winname = "Test"
# cv2.namedWindow(winname)        # Create a named window
# cv2.moveWindow(winname, 40,30)  # Move it to (40,30)
# cv2.imshow(winname, img)
# cv2.waitKey()
# cv2.destroyAllWindows()

(thresh, Img_First) = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY)
Height,Width = Img_First.shape

rows = Width
cols = Height

SumPixel_H = np.array([cols-(y/255) for y in Img_First.sum(axis=1)])

print(SumPixel_H)


Spec_HolBegin = 0
Spec_HolEnd = 0

Hol = len(SumPixel_H)

for SpScore in range(0,Hol,+1):
   if SumPixel_H[SpScore]<50 and SumPixel_H[SpScore]>30:
        SpScore = +1
   else:
      Spec_HolBegin=+SpScore
      break

for SpScore in range(Spec_HolBegin,Hol,+1):
   if SumPixel_H[SpScore] <30:
        SpScore = +1
   else:
      Spec_HolEnd=+SpScore
      break
UpperAndLower_Cut = Img_First[Spec_HolBegin : Spec_HolEnd,0:Width]
# cv2.imwrite("frame/frame_ver"+'.png',UpperAndLower_Cut)
winname = "Test"
cv2.namedWindow(winname)        # Create a named window
cv2.moveWindow(winname, 40,30)  # Move it to (40,30)
cv2.imshow(winname, UpperAndLower_Cut)
cv2.waitKey()
cv2.destroyAllWindows()
print(Spec_HolEnd)

# Height3,Width3 = UpperAndLower_Cut.shape
# rows3=Height3
# cols3=Width3
# SumPixel_Ver = np.array([rows3-(y/255) for y in UpperAndLower_Cut.sum(axis=0)])#หาผลรวมของpixelสีดำในแนวcol
# print(SumPixel_Ver)