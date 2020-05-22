import cv2
import numpy as np
import matplotlib.pyplot as plt




#แปลงภาพเป็นขาวดำ
def binary_image(image):
    (thresh, binary) = cv2.threshold(image, 140, 255, cv2.THRESH_BINARY)
    return binary



#detect หัวกระดาษ
def detect_box(image):

    edged = cv2.Canny(image, 10, 250)
    dst = cv2.fastNlMeansDenoising(image, None, 10, 10, 100) 
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    idx = 0
    for c in cnts:
        #หาความกว้างและความสูงของสิ่งที่จะตัด
        x,y,w,h = cv2.boundingRect(c)

        #กำหนดความกว้างและความสูงของสิ่งที่จะตัด
        if w>700 and h>200  :
            if w<1000 and h<300  :
              
                idx+=1
                new_img=image[y:y+h,x:x+w]
                cv2.imwrite("box/img"+ str(idx) + '.png', new_img)
               
    return new_img

#ตัดส่วนล่างของหัวกระดาษเพื่อป้องกันความผิดพลาด
def box_under(image):
    h,w = image.shape
    Rows=h
    Cols=w

    fram = 0
    fram2 = 0

    for i in range(0,h+1,+1):
        if i<h:
            fram += 1
            
        else:
            fram2 = +fram
            break

    test = image[fram-h:fram-42, 0:w] 
  
    return test 

#detect ช่องคะแนน
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
        
                idx=+1
                new_img=image[y:y+h,x:x+w]
              
    return new_img

#detect ช่องคะแนนของแต่ละช่อง
def detect_number(image):
    arrayImage_num =[]
   
    edged = cv2.Canny(image, 10, 250)
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sorted_ctrs = sorted(cnts, key=lambda cnts: cv2.boundingRect(cnts)[0])
    idx=0
    for i, ctr in enumerate(sorted_ctrs):
        x, y, w, h = cv2.boundingRect(ctr)
        if w>30 and h>40 : 
            if w<50 and h<55 : 
     
                idx+=1
                new_img=image[y:y+h,x:x+w]
             
                arrayImage_num.append(new_img)
    return arrayImage_num

#ทำการตัดกรอบของช่องรหัส
def frame_detail(img):
    array_cut=[]
    for i in range (0,img.__len__(),+1):
        w,h = img[i].shape
        Rows6 = h
        Cols6 = w
        SumPixel_HNo1 = np.array([Cols6 - (y / 255) for y in img[i].sum(axis=1)])
       
        Egde_cut1 = img[i][6:w - 6,6:h - 6] 
        array_cut.append(Egde_cut1)
    return array_cut

#เปลี่ยนสีภาพจากขาวเป็นดำ ดำเป็นขาว
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


#ปรับขนาดรูปภาพให้ตรงกัน
def tem_size(gray):
    array_size=[]
    
    for k in range (0,gray.__len__(),+1):
        Img_First = gray[k]
        h,w = Img_First.shape
        #สร้างพื้นหลังมาหนึ่งภาพแล้วทำการเอาภาพที่จะปรับไปวางทับกัน
        backgroundImg = np.zeros((50, 50), dtype=np.uint8)
        start_W_position = int(25-(w/2))
        start_H_position = int(25-(h/2))
        
        for i in range(0,h,+1):
            for j in range(0,w,+1):
                backgroundImg[i+start_H_position][j+start_W_position]=Img_First[i][j]
        
                cv2.imwrite("temp/img"+ str(k) + '.png', backgroundImg)
        array_size.append(backgroundImg)
 

    return array_size


#เช็คตำแหน่งสุดท้ายของช่องคะแนน 
def check_point(point):
  
    Img_point = point[12]
   
    h,w = Img_point.shape
    
    Rows=h
    Cols=w
    SumPixel_H = np.array([(y/255) for y in Img_point.sum(axis=1)])
    
    Hol = len(SumPixel_H)
    count_p = 0
    #ถ้าไม่ม่พิกเซลก็จะไม่แสดงค่าของช่อง 13
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





#detect ช่องคะแนน
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
               
                new_img2=img[y:y+h,x:x+w]
               
    return new_img2

#detect ช่องคะแนนของแต่ละช่อง
def detect_score(img):
    arrayImage_score =[]
    
    edged = cv2.Canny(img, 10, 250)
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sorted_ctrs = sorted(cnts, key=lambda cnts: cv2.boundingRect(cnts)[0])
    idx=0
    for i, ctr in enumerate(sorted_ctrs):
        x, y, w, h = cv2.boundingRect(ctr)
        if w>30 and h>40 : 
            if w<50 and h<60 :  
      
                idx+=1
                new_img=img[y:y+h,x:x+w]
               
                arrayImage_score.append(new_img)
    return arrayImage_score

#ตัดกรอบของช่องคะแนน
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

#ปรับขนาดช่องตะแนน
def tem_sizeScore(gray):
    array_size=[]
    
    for k in range (0,gray.__len__(),+1):
        Img_First = gray[k]
        
        h,w = Img_First.shape
        # print("test")
        backgroundImg = np.zeros((60, 60), dtype=np.uint8)
        start_W_position = int(30-(w/2))
        start_H_position = int(30-(h/2))
        
        for i in range(0,h,+1):
            for j in range(0,w,+1):
                backgroundImg[i+start_H_position][j+start_W_position]=Img_First[i][j]
        
                cv2.imwrite("temp_score/img"+ str(k) + '.png', backgroundImg)
        array_size.append(backgroundImg)
 

    return array_size

#เปลี่ยนสีภาพจากขาวเป็นดำ ดำเป็นขาว
def reblack_score(Img_black):
    
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

#เช๋คตำแหน่งของช่องที่หนึ่ง
def check_score(point):
 
    Img_point = point[0]
    
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

# เก็บค่าช่องคะแนน
def setScore(img):
    img_score.clear()
    img_score.append(img)

#เรียกใช้ฟังชั่นก์การทำงานต่างๆในส่วนของช่องคะแนน
def Process_score(img):
    score=detect_score(img)
    num =frame_detailScore(score)
    reblack=reblack_score(num)
    temp=tem_sizeScore(reblack)
    check=check_score(temp)
    setScore(check)
    # print(temp)

# getค่าช่องคะแนน
def getScore():
    return img_score[0]   
# getค่าช่องคะแนน
def Process_score2():
    temp = temp=tem_sizeScore(getScore())
    
    return temp


img2 = []   
# เก็บค่าช่องรหัส
def setimgNumber(img):
    img2.clear()
    img2.append(img)


#เรียกใช้ฟังชั่นก์การทำงานต่างๆ
def Process_paper(open_file):

        
    binary = binary_image(open_file)
    
    box = detect_box(binary)

    under=box_under(box)
    
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




# getค่าช่องรหัส
def getimgNumber():
    return img2[0]
    

# getค่าช่องรหัส

def Process_paper2():
    temp_size = tem_size(getimgNumber())
    
    return temp_size






# Process_paper()













