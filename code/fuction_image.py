import cv2
import numpy as np
import matplotlib.pyplot as plt

def readImage ():
    image3 = cv2.imread("box/img1.png")
    # print(image3)
    cv2.imshow("sd",image3)
    cv2.waitKey(0)
    # ia = image3
    # return ia

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

    
def detect_box(image):
    # image_box = image
    # gray = cv2.cvtColor(image_box,cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(image, 10, 250)
    dst = cv2.fastNlMeansDenoising(image, None, 10, 10, 100) 
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    idx = 0
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
       
        if w>700 and h>200  :
            if w<1000 and h<300  :
                # print( x,y,w,h)
            # if w>0 and h>0 :
                idx+=1
                new_img=image[y:y+h,x:x+w]
                cv2.imwrite("box/img"+ str(idx) + '.png', new_img)
                # imgbox=new_img
    return new_img

def detect_boxNumber(image):
    # arrayImage =[]
    edged = cv2.Canny(image, 10, 250)
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sorted_ctrs = sorted(cnts, key=lambda cnts: cv2.boundingRect(cnts)[0])
    idx=0
    for i, ctr in enumerate(sorted_ctrs):
        x, y, w, h = cv2.boundingRect(ctr)
        if w>500 and h>40 : 
            if w<600 and h<80 : 
        # if w>0 and h>0 : 
                # print(x, y, w, h)
                idx=+1
                new_img=image[y:y+h,x:x+w]
                # cv2.imwrite("number/img"+ str(i) + '.png', new_img)
                cv2.imwrite("number/img2" + '.png', new_img)
                # arrayImage.append(new_img)
    return new_img


def detect_number(image):
    arrayImage_num =[]
    # img_number = image

    # gray = cv2.cvtColor(img_number,cv2.COLOR_BGR2GRAY)
    # cv2.imshow("asd",img_number)
    edged = cv2.Canny(image, 10, 250)
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sorted_ctrs = sorted(cnts, key=lambda cnts: cv2.boundingRect(cnts)[0])
    idx=0
    for i, ctr in enumerate(sorted_ctrs):
        x, y, w, h = cv2.boundingRect(ctr)
        if w>35 and h>40 : 
            if w<50 and h<55 : 
        # if w>0 and h>0 : 
                # print(x, y, w, h)
                idx=+1
                new_img=image[y:y+h,x:x+w]
                cv2.imwrite("code2/num/img"+ str(i) + '.png', new_img)
                arrayImage_num.append(new_img)
    return arrayImage_num


def frame_detail(img):
    array_cut=[]
    for i in range (0,img.__len__(),+1):
        w,h = img[i].shape
        # print(w,h)
        Rows6 = h
        Cols6 = w
        # print(Cols6)
        SumPixel_HNo1 = np.array([Cols6 - (y / 255) for y in img[i].sum(axis=1)])
        # print(SumPixel_HNo1)
        Egde_cut1 = img[i][6:w - 6,6:h - 6] 
        array_cut.append(Egde_cut1)
    return array_cut


def reblack(Img_black):
    # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # (thresh, Img_First) = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
    #cv2.imshow("imaB",Img_First)

    #cv2.waitKey(0)
    #กำหนดให้ widthคือความกล้าง และ heightคือความสูง  แล้วให้ rows คือหาค่าในแนวนอนของความสูง และ cols คือหาค่าในแนวตั้งของความกว้าง---------------------------
    array_black=[]
    for k in range (0,Img_black.__len__(),+1):
        Img_First = Img_black[k]
        
        Height,Width = Img_First.shape
        # print(Height,Width)
        # print("H : "+ str(Height)+"  W : "+str(Width))


        for i in range (0,Height,+1):
            for j in range (0,Width,+1):
                if Img_First[i][j]==255:
                    Img_First[i][j]=0
                else:
                    Img_First[i][j]=255
        cv2.imwrite("clear_image/img"+ str(k) + '.png', Img_First)
        array_black.append(Img_First)
        # print(array_black)
        # cv2.imshow("asd",array_black)              
    return array_black

def tem_size(gray):
    array_size=[]
    
    for k in range (0,gray.__len__(),+1):
        Img_First = gray[k]
        
        h,w = Img_First.shape
        # print(w,h)
        backgroundImg = np.zeros((50, 50), dtype=np.uint8)
        start_W_position = int(25-(w/2))
        start_H_position = int(25-(h/2))
        
        for i in range(0,h,+1):
            for j in range(0,w,+1):
                backgroundImg[i+start_H_position][j+start_W_position]=Img_First[i][j]
        
                cv2.imwrite("temp/img"+ str(k) + '.png', backgroundImg)
        array_size.append(backgroundImg)
 

    return array_size

def erosion(image):
    array_erode=[]
    for i in range (0,image.__len__(),+1):
        Img_First = image[i]
        kernel = np.ones((2,2),np.uint8)
        img_erosion = cv2.erode(Img_First, kernel, iterations=1) 
        array_erode.append(img_erosion)
    return array_erode
        
img2 = []   

def setimgNumber(img):
    img2.append(img)

def Process_paper():
    try:
        image = cv2.imread("bi8.png")
        # image3 = cv2.imread("box/img1.png")
        # print(image3)

        grayscale = gray_scale(image)

        binary = binary_image(grayscale)
        # rot = rotate_image(binary,0)
        box = detect_box(binary)
        boxNumber=detect_boxNumber(box)
        number = detect_number(boxNumber)
        cut_fram = frame_detail(number)
        image_black=reblack(cut_fram)
        temp_size = tem_size(image_black)
        setimgNumber(temp_size)
    except:
   
        image = cv2.imread("bi8.png")
        # image3 = cv2.imread("box/img1.png")
        # print(image3)

        grayscale = gray_scale(image)

        binary = binary_image(grayscale)
        # rot = rotate_image(binary,0)
        
        boxNumber=detect_boxNumber(binary)
        # print(boxNumber)
        number = detect_number(boxNumber)
        cut_fram = frame_detail(number)
        image_black=reblack(cut_fram)
        temp_size = tem_size(image_black)
        setimgNumber(temp_size)
    # erode = erosion(temp_size)
    return temp_size



def getimgNumber():
    return img2[0]
    


def Process_paper2():
    temp_size = tem_size(getimgNumber())
    return temp_size


Process_paper()
# print(Process_paper())












