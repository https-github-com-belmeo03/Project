from cv2 import cv2
import numpy as np

def scan_cut(image):
    
    # arr = []
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    (thresh, Img_First) = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

    re_img =cv2.resize(Img_First,(2468,3500))
    w,h = re_img.shape
    
    UpperAndLower_Cut = re_img[0 : 1234,0:w]
    
    # cv2.imshow("sad",UpperAndLower_Cut)
    UpperAndLower_Cut2 = re_img[0 : 680,0:w]
    img = cv2.resize(UpperAndLower_Cut2,(1234,340))
    cv2.imwrite("box/img1.png",img)
    return img

def scan_boxnumber(image):
    edged = cv2.Canny(image, 10, 250)

    dst = cv2.fastNlMeansDenoising(image, None, 10, 10, 100) 
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    idx = 0
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        
    
        # print( x,y,w,h)
        if w>550 and h>60 :
            if w<610 and h<90 :
                # print("1")
                idx+=1
                new_img=image[y:y+h,x:x+w]
                # cv2.imwrite("number/img" + '.png', new_img)
    return new_img

def scan_number(image):
    arrayImage_num =[]
    edged = cv2.Canny(image, 10, 250)
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sorted_ctrs = sorted(cnts, key=lambda cnts: cv2.boundingRect(cnts)[0])
    idx=0
    for i, ctr in enumerate(sorted_ctrs):
        x, y, w, h = cv2.boundingRect(ctr)
        if w>35 and h>45 : 
            if w<50 and h<60 : 
                idx+=1
                new_img=image[y:y+h,x:x+w]
                arrayImage_num.append(new_img)
    return arrayImage_num

def cut_underNum(image):
    (thresh, Img_First) = cv2.threshold(image, 140, 255, cv2.THRESH_BINARY)


    w,h = Img_First.shape
    # print(w,h) 
    UpperAndLower_Cut2 = Img_First[0 : 63,0:h]
    return UpperAndLower_Cut2

def scan_detail(image):
    array_cut=[]
    for i in range (0,image.__len__(),+1):
        w,h = image[i].shape
        Rows6 = h
        Cols6 = w
        SumPixel_HNo1 = np.array([Cols6 - (y / 255) for y in image[i].sum(axis=1)])
        Egde_cut1 = image[i][5:w - 5,5:h - 5] 
        array_cut.append(Egde_cut1)
    return array_cut

def reblack(Img_black):
   
    array_black=[]
    for k in range (0,Img_black.__len__(),+1):
        Img_First = Img_black[k]
        
        Height,Width = Img_First.shape
       
        for i in range (0,Height,+1):
            for j in range (0,Width,+1):
                if Img_First[i][j]==255:
                    Img_First[i][j]=0
                else:
                    Img_First[i][j]=255
        array_black.append(Img_First)
               
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





def clear_scans(img):
    # gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    (thresh, Img_First) = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY)


    w,h = Img_First.shape
    UpperAndLower_Cut2 = Img_First[0 : w,900:h]
    # cv2.imwrite("cut/img" + '.png', UpperAndLower_Cut2)
    return UpperAndLower_Cut2


def scan_boxscore(img):
    # print(img)
    
    edged = cv2.Canny(img, 10, 250)
    dst = cv2.fastNlMeansDenoising(img, None, 10, 10, 100) 
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    idx = 0
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        if w>150 and h>120 :
            if w<165 and h<135 :
        # print(x,y,w,h)
        # idx+=1
                new_img2=img[y:y+h,x:x+w]
                # cv2.imwrite("score/img"+  '.png', new_img2)
        # imgbox=new_img
    return new_img2


def clear_scan(img):
    # gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    (thresh, Img_First) = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY)


    w,h = Img_First.shape
    UpperAndLower_Cut = Img_First[50 : h,0:h]
    # cv2.imwrite("cut/img2" + '.png', UpperAndLower_Cut)
    return UpperAndLower_Cut

def scan_numberscore(img):
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
        if w>40 and h>60 :
            if w<55 and h<70 : 
        
                idx+=1
                new_img=img[y:y+h,x:x+w]
                # cv2.imwrite("num_score/img"+ str(idx) + '.png', new_img)
                arrayImage_score.append(new_img)
    return arrayImage_score

def scan_detailScore(img):
    array_cut=[]
    for i in range (0,img.__len__(),+1):
        w,h = img[i].shape
        # print(w,h)
        Rows6 = h
        Cols6 = w
        # print(Cols6)
        SumPixel_HNo1 = np.array([Cols6 - (y / 255) for y in img[i].sum(axis=1)])
        # print(SumPixel_HNo1)
        Egde_cut1 = img[i][5:w - 5,5:h - 5] 
        array_cut.append(Egde_cut1)
    return array_cut

def scan_sizeScore(gray):
    array_size=[]
    
    for k in range (0,gray.__len__(),+1):
        Img_First = gray[k]
        
        h,w = Img_First.shape
        # print("test")
        backgroundImg = np.zeros((80, 80), dtype=np.uint8)
        start_W_position = int(40-(w/2))
        start_H_position = int(40-(h/2))
        
        for i in range(0,h,+1):
            for j in range(0,w,+1):
                backgroundImg[i+start_H_position][j+start_W_position]=Img_First[i][j]
        
                cv2.imwrite("temp_score/img"+ str(k) + '.png', backgroundImg)
        array_size.append(backgroundImg)
 

    return array_size

def reblack_scan(Img_black):
  
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
        # cv2.imwrite("clear_score/img"+ str(k) + '.png', Img_First)
        array_black.append(Img_First)
        # print(array_black)
        # cv2.imshow("asd",array_black)              
    return array_black

def check_scan(point):
    # array_point=[]
    # print(point[12])
    Img_point = point[0]
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
        point.pop(0)
    # print(point[0])
    return point

img_score=[]
def setScore(img):
    img_score.clear()
    img_score.append(img)


def scan_function2(image):
    clear_img=clear_scans(image)
    score_Sbox= scan_boxscore(clear_img)

    clear= clear_scan(score_Sbox)
    score_Snumber=scan_numberscore(clear)
    frame=scan_detailScore(score_Snumber)
    black = reblack_scan(frame)
    temp=scan_sizeScore(black)
    check2 = check_scan(temp)
    setScore(check2)

def getScore():
    return img_score[0]   

def getscan_function2():
    temp = temp=scan_sizeScore(getScore())
    
    return temp




img2 = []   

def setimgNumberscan(img):
    img2.clear()
    img2.append(img)

def scan_function(file_name):
    image = cv2.imread(file_name)
    # image = cv2.imread("scan/f4.jpg")
    cut = scan_cut(image)
    scan_function2(cut)
    scanbox=scan_boxnumber(cut)
    number = scan_number(scanbox)
    
    if number == []:
      
        scanbox2 = cut_underNum(scanbox)
        number = scan_number(scanbox2)
    frame = scan_detail(number)
    black = reblack(frame)
    temp = tem_size(black)
    check = check_point(temp)
    setimgNumberscan(check)
    return check

def getimgNumberscan():
    return img2[0]

def getscan_function():
    temp_size = tem_size(getimgNumberscan())
    
    return temp_size

# scan_function()