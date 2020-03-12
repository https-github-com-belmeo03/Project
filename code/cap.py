import cv2
import numpy as np

# def frame_cap():

cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
img_counter = 0
cam.set(3,1080)
cam.set(4,800)
cam.set(15,0.1)

while True:
		ret, frame = cam.read()
		ret, fr = cam.read()

		cv2.line(fr , (0, 220), (800, 220), (255, 0, 0), 2)
		cv2.line(fr, (0, 260), (800, 260), (0, 255, 0), 2)

		cv2.line(fr, (290, 0), (290, 800), (255, 0, 0), 2)
		cv2.line(fr, (335, 0), (335, 800), (0, 255, 0), 2)
		cv2.imshow("test", fr)

		gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		th1 = cv2.adaptiveThreshold(gray1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 40)
		cv2.imshow("test1", th1) #เอาไว้ดูวิดิโอที่เป็น binary

		if not ret:
				break

		k = cv2.waitKey(1)

		if k%256 == 27:
				# ESC pressed
				print("Escape hit, closing...")
				break


		elif k%256 == ord('z'):
				img_name = "opencv_frame_{}.png"
				cv2.imwrite(img_name, frame)
				img = cv2.imread(img_name)
				gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
				th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 40)
				#Imgcut = th[220:260, 290:335]
				cv2.imwrite("BinaryS21.png", th)
				cv2.imshow('Adaptive threshold', th)
				#print("{} written!".format(img_name))
				img_counter += 1



cam.release()

cv2.destroyAllWindows()

# fuction_cap()

