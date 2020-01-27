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
    image_box = image
    # gray = cv2.cvtColor(image_box,cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(image_box, 10, 250)
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    idx = 0
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        # print( x,y,w,h)
        if w>200 and h>200 and w<1000 and h<700:
            idx+=1
            new_img=image_box[y:y+h,x:x+w]
            imgbox=new_img
    return imgbox

def detect_number(image):
    arrayImage =[]
    img_number = image

    # gray = cv2.cvtColor(img_number,cv2.COLOR_BGR2GRAY)
    # cv2.imshow("asd",img_number)
    edged = cv2.Canny(img_number, 10, 250)
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sorted_ctrs = sorted(cnts, key=lambda cnts: cv2.boundingRect(cnts)[0])
    idx=0
    for i, ctr in enumerate(sorted_ctrs):
        x, y, w, h = cv2.boundingRect(ctr)
        if w>25 and h>25 and w<70 and h<70: 
            # print(x, y, w, h)
            idx=+1
            new_img=img_number[y:y+h,x:x+w]
            cv2.imwrite("number/img"+ str(i) + '.png', new_img)
            arrayImage.append(new_img)
            # img_number2=new_img 
            # cv2.imshow("asd"+str(i),img_number2)
    return arrayImage 


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
        backgroundImg = np.zeros((30, 30), dtype=np.uint8)
        for i in range(0,h,+1):
            for j in range(0,w,+1):
                backgroundImg[i][j]=Img_First[i][j]
        
        # cv2.imwrite("temp/img"+ str(k) + '.png', backgroundImg)
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
        
      

def Process_paper():
    image = cv2.imread("cap2.jpg")
    # image3 = cv2.imread("box/img1.png")
    # print(image3)

    grayscale = gray_scale(image)

    binary = binary_image(grayscale)
    rot = rotate_image(binary,-90)
    box = detect_box(rot)

    number = detect_number(box)
    cut_fram = frame_detail(number)
    image_black=reblack(cut_fram)
    temp_size = tem_size(image_black)
    erode = erosion(temp_size)
    

    # print(erode)
    # noise2 = add_gaussian_noise(binary)
    # detec = detection(grayscale)
    # cv2.imshow("asd",binary)
    # cv2.imwrite("bi2"+".png",binary)
    # cv2.imshow("hb",image_black[0])
    # cv2.waitKey(0)
    # plt.imshow(image_black)
    # plt.show()
    return erode


# Process_paper()
# print(Process_paper())












