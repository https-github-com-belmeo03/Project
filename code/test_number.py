from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import matplotlib.pyplot as plt
import fuction_image as fmate
import cv2
# load and prepare the image
plt.rcParams['image.cmap'] = 'gray'
def load_image(filename):
	# load the image
	array_test=[]
	for i in range (0,filename.__len__()-1,+1):
			
			# cv2.imshow("asf",filename[i])
			# cv2.waitKey(0)
		# print(filename[1])
			plt.imshow(filename[i]);
			plt.show()
			# gray3 = cv2.cvtColor(filename[i],cv2.COLOR_BGR2GRAY)
			(thresh, Img_First) = cv2.threshold(filename[i], 140, 255, cv2.THRESH_BINARY)
			img = cv2.resize(Img_First,(28,28))
			# print(img)
		# 	h,w = filename[i].shape
		# print(h,w)
			# img = cv2.resize(filename[i],(28,28))
			# h,w = img.shape
			# print(img[1])
			img2 = img.reshape(1, 28, 28, 1)
			# print(img2)
			# img2 = img2.astype('float32')
			# img2 = img2 / 255.0
			array_test.append(img2)
	return array_test
	
 
# load an image and predict the class
def run_example():
	# load the image
	# model = load_model('final_model2.h5py')
	img = load_image(fmate.Process_paper())
	model = load_model('final_model2.h5py')
	# for k in range (0,img.__len__(),+1):
		# img2 = img[k].reshape(1, 28, 28, -1)
		# print(img2)

	# img2 = img.reshape(1, 28, 28, 1)
    # plt.imshow(img);
    # w,h=img.shape
	# print(img2)
	# load model
	
	# # # predict the class
	
	for i in range (0,img.__len__(),+1):
		digit = model.predict_classes(img[i])
		print(digit)
		# plt.imshow(img[i]);
 
# entry point, run the example

run_example()