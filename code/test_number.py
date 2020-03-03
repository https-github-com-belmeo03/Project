from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import matplotlib.pyplot as plt
import fuction_image as fmate
import cv2
# load and prepare the image
plt.rcParams['image.cmap'] = 'gray'
def binary_image(img):
	
	array_binary=[]
	for k in range (0,img.__len__()-1,+1):
		
		Img_First = img[k]
		
		Height,Width = Img_First.shape
		# print(Height,Width)


		for i in range (0,Height,+1):
			for j in range (0,Width,+1):
				if Img_First[i][j]!=0:
					
					Img_First[i][j]=255
		cv2.imwrite("resize/img"+ str(k) + '.png', Img_First)
		array_binary.append(Img_First)
	return array_binary
               

def load_image(filename):
	# load the image
	array_test=[]
	array_testBi=[]
	for i in range (0,filename.__len__()-1,+1):
			
		
		(thresh, Img_First) = cv2.threshold(filename[i], 140, 255, cv2.THRESH_BINARY)
		img = cv2.resize(Img_First,(28,28))
		# array_testBi.append(img)
		# img2 = binary_image(array_testBi)
		# (thresh, binary) = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY)
		# print(img2)
	# for j in range (0,img2.__len__()-1,+1):
	# 	im3 = img2[j]
		# cv2.imwrite("resize/img"+ str(i) + '.png', img)
				
		img4 = img.reshape(1, 28, 28, 1)
		
		array_test.append(img4)
	return array_test
	
 
# load an image and predict the class
def run_example():
	count_number=[]
	# load the image
	# model = load_model('final_model2.h5py')
	img = load_image(fmate.Process_paper())
	model = load_model('final_model3.h5py')

	# # # predict the class
	
	for i in range (0,img.__len__(),+1):
		digit = model.predict_classes(img[i])
		print(digit)
	# 	# plt.imshow(img[i]);
		count_number.append(int(digit))
	return count_number



# plt.show()
# entry point, run the example
# print(run_example())
# file = open("code.txt", "w")
# for i_r in range(0,getNumberRasp.__len__(),+1):
#  print("get "+str(i_r)+"1", getNumberRasp[i_r])
#  file.write(str(getNumberRasp[i_r])+",")
run_example()

# print(csv[0])