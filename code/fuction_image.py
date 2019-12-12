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
         
    def rotate_image(mat, angle):
        """
        Rotates an image (angle in degrees) and expands image to avoid cropping
        """

        height, width = mat.shape[:2] # image shape has 3 dimensions
        image_center = (width/2, height/2) # getRotationMatrix2D needs coordinates in reverse order (width, height) compared to shape

        rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1.)

        # rotation calculates the cos and sin, taking absolutes of those.
        abs_cos = abs(rotation_mat[0,0]) 
        abs_sin = abs(rotation_mat[0,1])

        # find the new width and height bounds
        bound_w = int(height * abs_sin + width * abs_cos)
        bound_h = int(height * abs_cos + width * abs_sin)

        # subtract old image center (bringing image back to origo) and adding the new image center coordinates
        rotation_mat[0, 2] += bound_w/2 - image_center[0]
        rotation_mat[1, 2] += bound_h/2 - image_center[1]

        # rotate image with the new bounds and translated rotation matrix
        rotated_mat = cv2.warpAffine(mat, rotation_mat, (bound_w, bound_h))
        return rotated_mat
  
        



    image = cv2.imread("cap2.jpg")

    grayscale = gray_scale(image)

    binary = binary_image(grayscale)

    # noise2 = add_gaussian_noise(binary)
    # detec = detection(grayscale)
    # cv2.imshow("asd",binary)
    cv2.imwrite("bi2"+".png",binary)
    # cv2.imshow("hb",noise2)
    cv2.waitKey(0)



fuction_image()










