
from __future__ import print_function
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from skimage import exposure
import numpy as np
import imutils
import cv2


mnist = datasets.load_digits()

(trainData, testData, trainLabels, testLabels) = train_test_split(np.array(mnist.data), mnist.target, test_size=0.25, random_state=42) #ข้อมูลไฟล์ test

(trainData, valData, trainLabels, valLabels) = train_test_split(trainData, trainLabels, test_size=0.1, random_state=84) #ข้อมูลไฟล์ train แต่ดึงรูปมาจาก test อีกที
cc = testData.astype("uint8")
# cv2.imshow("cc", cc)
model = KNeighborsClassifier(n_neighbors=1) #คำนวณ KNN
model.fit(trainData, trainLabels) #set ข้อมูล train
# print("step1 testData : ", testData)

#เตรียมภาพ 2 มิติ ที่ เมื่อแปลกเป็น 1 มิติแล้วให้เท่ากับ print("image : ", image)  อันนี้กูก็ไม่แน่ใจว่ามันต้องมีขนาดเท่าไหร่ มึงลองหารูปมา แล้วนำจำนวน 1 มิติดูแล้วลอง

# for i in np.random.randint(0, high=len(testLabels), size=(1,)): # loop เพื่อ วนหารูปที่จะมา test เฉยๆ

img= cv2.imread("0000.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
(thresh, Img_First) = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
ima = cv2.resize(Img_First,(8,8))
image = ima.reshape(1,-1)   #บรรนี้ นำภาพเข้า ในรูปแบบ 1 มิติ เช่น image = 1 มิติ
print(image)
# print("image : ", image)
prediction = model.predict(image) # นำรูปภาพ 1 มิติที่รับเข้ามา จากนั้นเรียกใช้ model เพื่อเรียกการคำนวณ KNN
print("step2 image1 : ",prediction)

image = image.reshape((8, 8)).astype("uint8") #แปลกภาพกลับเป็น 2 มิติ
print("step3 image1 : ", image)
image = exposure.rescale_intensity(image, out_range=(0, 255))
print("step4 image1 : ", image)
image = imutils.resize(image, width=32, inter=cv2.INTER_CUBIC)

print("I think that digit is: {}".format(prediction))
# print("image5 : ",image)
print("-------------------------------------------------------------------")
cv2.imshow("Image", image)
cv2.waitKey(0)