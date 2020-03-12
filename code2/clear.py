import cv2
import numpy as np

import cv2
import numpy as np

img = cv2.imread('222.png')
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)
cv2.imshow("asfd",dilation)
cv2.waitKey(0)