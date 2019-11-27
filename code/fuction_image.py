import cv2
import numpy as np

class fuction_image:

    def gray_scale(image):
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        grayscale = gray
        return grayscale

    def binary_image(image):
        (thresh, binary) = cv2.threshold(image, 140, 255, cv2.THRESH_BINARY)
        return binary

    def add_mean_noise(image):
        dst = cv2.fastNlMeansDenoising(image, None, 10, 10, 100) 
        reduc_noise = dst
     
        return reduc_noise  

    def detection(gray):
        idx = gray
        edged = cv2.Canny(gray, 10, 250)
        # cv2.imshow("Edges", edged)
        # cv2.waitKey(0)
        
        #applying closing function 
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
        closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
        # cv2.imshow("Closed", closed)
        # cv2.waitKey(0)
        
        #finding_contours 
        (cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            cv2.drawContours(image, [approx], -1, (0, 255, 0), 


        return idx


    # def detection(gray):
        
    #     retval, thresh_gray = cv2.threshold(gray, thresh=160, maxval=255,type=cv2.THRESH_BINARY_INV)
        
    #     contours, hierarchy = cv2.findContours(thresh_gray,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    #     print(contours)



    #     # mx = (0,0,0,0)      # biggest bounding box so far
    #     # mx_area = 0
    #     # for cont in contours:
    #     #     x,y,w,h = cv2.boundingRect(cont)
    #     #     x, y, w, h = x-40, y-40, w+80,h+80 # make the bounding box a bit bigger
    #     #     area = w*h
    #     #     if area > mx_area:
    #     #         mx = x,y,w,h
    #     #         mx_area = area
    #     # x,y,w,h = mx

    #     # # Output to files
    #     # roi=img[y:y+h,x:x+w]

    #     # dec = roi

    #     return dec
        



    image = cv2.imread("im2.jpg")

    grayscale = gray_scale(image)

    # binary = binary_image(grayscale)

    # noise2 = add_gaussian_noise(binary)
    detec = detection(grayscale)
    # cv2.imshow("asd",binary)
    # cv2.imshow("hb",noise2)
    # cv2.waitKey(0)



fuction_image()










