from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import matplotlib.pyplot as plt
import fuction_image as fmate
import scan as sc
import cv2
import csv
# import input_image as ing
# load and prepare the image
plt.rcParams['image.cmap'] = 'gray'
# def input_image():
# 	image_array=[]
# 	for i in range(0,13,+1):
# 			image = cv2.imread("temp/img"+str(i)+'.png') 
# 			image_array.append(image)
# 	return image_array



def load_image(filename):
	# load the image
	
	
	
	array_test=[]
	# array_testBi=[]
	for i in range (0,filename.__len__(),+1):
		
		
		(thresh, Img_First) = cv2.threshold(filename[i], 140, 255, cv2.THRESH_BINARY)
		img = cv2.resize(Img_First,(28,28))
		
	
		# print(i)

				
		img4 = img.reshape(1, 28, 28, 1)
		
		array_test.append(img4)
	return array_test


	

# load an image and predict the class
def run_example():
	
	count_number=[]
	try:
		img = load_image(sc.getscan_function())
	except:
		img = load_image(fmate.Process_paper2())
	
	
	model = load_model('final_model3.h5py')

	# # # predict the class
	
	for i in range (0,img.__len__(),+1):
		digit = model.predict_classes(img[i])
		# print(digit)
	
		count_number.append(int(digit))
	
	# saveCSV(count_number)
	
	return count_number

def load_score(filename):
	# load the image
	
	
	
	array_testScore=[]
	# array_testBi=[]
	
	for i in range (0,filename.__len__(),+1):
		
		
		(thresh, Img_First) = cv2.threshold(filename[i], 140, 255, cv2.THRESH_BINARY)
		img = cv2.resize(Img_First,(28,28))
		
		
		
		# print(i)

				
		img4 = img.reshape(1, 28, 28, 1)
		
		array_testScore.append(img4)
	return array_testScore

def run_score():
	count_score=[]
	# load the image
	# model = load_model('final_model2.h5py')
	try:
		img2 = load_image(sc.getscan_function2())
	except:
		img2 = load_score(fmate.Process_score2())
	# print(img2)
	
	
	model2 = load_model('final_model4.h5py')

	# # # predict the class
	
	for j in range (0,img2.__len__(),+1):
		digit2 = model2.predict_classes(img2[j])
		# print(digit2)
		# print(j)
	
		count_score.append(int(digit2))
	
	# saveCSV(count_score)
	return count_score
def csv_file(score,number):
	# array_number = []
	with open("code3.csv", "a") as f:
		# fieldnames = ['score','number']
		# writer = csv.DictWriter(f, lineterminator='\n')
		writer = csv.writer(f,lineterminator='\n')
		# writer.writeheader()
		# for row in writer
		writer.writerow([score,number])


	# print(array_number)


def saveCSV(data):
	file = open("code2.csv", "w")
	for i_r in range(0,data.__len__(),+1):
 		file.write(str(data[i_r])+',')



# run_example()
