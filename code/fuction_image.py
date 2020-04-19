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

def box_under(image):
    h,w = image.shape
    Rows=h
    Cols=w


    # print(SumPixel_HNo1)
    # print(w,h)
    fram = 0
    fram2 = 0

    for i in range(0,h+1,+1):
        if i<h:
            fram += 1
            
        else:
            fram2 = +fram
            break

    test = image[fram-h:fram-42, 0:w] 
    # cv2.imwrite("testbug/img"+'.png',test)
    return test 

def detect_boxNumber(image):
    # arrayImage =[]
    edged = cv2.Canny(image, 10, 250)
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sorted_ctrs = sorted(cnts, key=lambda cnts: cv2.boundingRect(cnts)[0])
    idx=0
    for i, ctr in enumerate(sorted_ctrs):
        x, y, w, h = cv2.boundingRect(ctr)
        if w>490 and h>40 : 
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
        if w>30 and h>40 : 
            if w<50 and h<55 : 
        # if w>0 and h>0 : 
                # print(x, y, w, h)
                idx+=1
                new_img=image[y:y+h,x:x+w]
                cv2.imwrite("num/img"+ str(idx) + '.png', new_img)
                # cv2.imwrite("num/img"+ str(idx) + '.png', image)
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
        # print("test")
        backgroundImg = np.zeros((50, 50), dtype=np.uint8)
        start_W_position = int(25-(w/2))
        start_H_position = int(25-(h/2))
        
        for i in range(0,h,+1):
            for j in range(0,w,+1):
                backgroundImg[i+start_H_position][j+start_W_position]=Img_First[i][j]
        
                cv2.imwrite("temp/img"+ str(k) + '.png', backgroundImg)
        array_size.append(backgroundImg)
 

    return array_size

def check_point(point):
    # array_point=[]
    # print(point[12])
    Img_point = point[12]
    # plt.imshow(Img_point)
    # plt.show()
    h,w = Img_point.shape
    
    Rows=h
    Cols=w
    SumPixel_H = np.array([(y/255) for y in Img_point.sum(axis=1)])
    
    Hol = len(SumPixel_H)
    count_p = 0
    for i in range(0,Hol,+1):
        if SumPixel_H[i] == 0:
            i =+1
        else:
            count_p =+i
            # i =+1
    # print(i)
    # print(count_p)
    if count_p < 5:
        point.pop(12)
    # print(point[12])
    return point




def erosion(image):
    array_erode=[]
    for i in range (0,image.__len__(),+1):
        Img_First = image[i]
        kernel = np.ones((2,2),np.uint8)
        img_erosion = cv2.erode(Img_First, kernel, iterations=1) 
        array_erode.append(img_erosion)
    return array_erode
        


def detect_boxscore(img):
    # 
    edged = cv2.Canny(img, 10, 250)
    dst = cv2.fastNlMeansDenoising(img, None, 10, 10, 100) 
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    idx = 0
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        if w>130 and h>100 : 
            if w<155 and h<120 :
                # print(img)
                # idx+=1
                new_img2=img[y:y+h,x:x+w]
                cv2.imwrite("score/img"+  '.png', new_img2)
        # imgbox=new_img
    return new_img2

def detect_score(img):
    arrayImage_score =[]
    # img_number = image

    # gray = cv2.cvtColor(img_number,cv2.COLOR_BGR2GRAY)
    # cv2.imshow("asd",img_number)
    edged = cv2.Canny(img, 10, 250)
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sorted_ctrs = sorted(cnts, key=lambda cnts: cv2.boundingRect(cnts)[0])
    idx=0
    for i, ctr in enumerate(sorted_ctrs):
        x, y, w, h = cv2.boundingRect(ctr)
        if w>30 and h>40 : 
            if w<50 and h<60 :  
        # if w>0 and h>0 : 
                # print(x, y, w, h)
                idx+=1
                new_img=img[y:y+h,x:x+w]
                cv2.imwrite("num_score/img"+ str(idx) + '.png', new_img)
                arrayImage_score.append(new_img)
    return arrayImage_score

def frame_detailScore(img):
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

def tem_sizeScore(gray):
    array_size=[]
    
    for k in range (0,gray.__len__(),+1):
        Img_First = gray[k]
        
        h,w = Img_First.shape
        # print("test")
        backgroundImg = np.zeros((130, 130), dtype=np.uint8)
        start_W_position = int(65-(w/2))
        start_H_position = int(65-(h/2))
        
        for i in range(0,h,+1):
            for j in range(0,w,+1):
                backgroundImg[i+start_H_position][j+start_W_position]=Img_First[i][j]
        
                cv2.imwrite("temp_score/img"+ str(k) + '.png', backgroundImg)
        array_size.append(backgroundImg)
 

    return array_size

def reblack_score(Img_black):
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
        cv2.imwrite("clear_score/img"+ str(k) + '.png', Img_First)
        array_black.append(Img_First)
        # print(array_black)
        # cv2.imshow("asd",array_black)              
    return array_black
img_score=[]
def setScore(img):
    img_score.clear()
    img_score.append(img)

def Process_score(img):
    score=detect_score(img)
    num =frame_detailScore(score)
    reblack=reblack_score(num)
    temp=tem_sizeScore(reblack)
    # check=check_point(temp)
    setScore(temp)
    # print(temp)
def getScore():
    return img_score[0]   

def Process_score2():
    temp = temp=tem_sizeScore(getScore())
    
    return temp


img2 = []   

def setimgNumber(img):
    img2.clear()
    img2.append(img)

def Process_paper(open_file):


    try:
        image = cv2.imread(open_file)
        # print(image)
        

        grayscale = gray_scale(image)

        binary = binary_image(grayscale)
        
        


        box = detect_box(binary)

        under=box_under(box)
        # print("2")
        boxscore= detect_boxscore(under)
        Process_score(boxscore)

        boxNumber=detect_boxNumber(under)
        number = detect_number(boxNumber)
        cut_fram = frame_detail(number)
        image_black=reblack(cut_fram)
        temp_size = tem_size(image_black)
        check=check_point(temp_size)
        setimgNumber(check)
    except:
        print(open_file)

    #     image = cv2.imread(open_file)
        # grayscale = gray_scale(open_file)
        binary = binary_image(open_file)
        print("1")
        box = detect_box(binary)

        under=box_under(box)
        # print("2")
        boxscore= detect_boxscore(under)
        Process_score(boxscore)

        boxNumber=detect_boxNumber(under)
        number = detect_number(boxNumber)
        cut_fram = frame_detail(number)
        image_black=reblack(cut_fram)
        temp_size = tem_size(image_black)
        check=check_point(temp_size)
        setimgNumber(check)
        
  
    return check





def getimgNumber():
    return img2[0]
    


def Process_paper2():
    temp_size = tem_size(getimgNumber())
    
    return temp_size






# Process_paper()













