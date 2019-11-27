import cv2 
image = cv2.imread("im2.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(image, 10, 250)
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
idx = 0
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    print( x,y,w,h)
    if w>40 and h>40:
        idx+=1
        new_img=image[y:y+h,x:x+w]
        cv2.imwrite("code/img"+ str(idx) + '.png', new_img)
cv2.imshow("im",new_img)
cv2.waitKey(0)