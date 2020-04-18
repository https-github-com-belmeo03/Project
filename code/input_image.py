import cv2
import numpy as np


def input_image():
    image2=[]
    for i in range(0,13,+1):
        image = cv2.imread("temp/img"+str(i)+'.png')
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        (thresh, binary) = cv2.threshold(image, 140, 255, cv2.THRESH_BINARY)
        # cv2.imshow("saD",binary)
        # cv2.waitKey(0)
        image2.append(binary)
        print(binary)
    return image2
input_image()


    