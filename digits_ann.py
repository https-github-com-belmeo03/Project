from PIL import Image
import numpy as np
import cv2
"""""""""
#from matplotlib import pyplot as plt

w, h = 20, 20

img = cv2.imread('digit.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
##img = Image.fromarray(gray)
##img.show()

# Now we split the image to 5000 cells, each 20x20 size
cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]

# Make it into a Numpy array. It size will be (50,100,20,20)
x = np.array(cells)

#อ่านตัวเลขตัวแรก ของ 5000 ตัวอักษร
y = x[0,0,1:20,1:20]
img = Image.fromarray(y)
#img.show()

# Now we prepare train_data and test_data.
train = x[:,:50].reshape(-1,400).astype(np.float32) # Size = (2500,400)
test = x[:,50:100].reshape(-1,400).astype(np.float32) # Size = (2500,400)

# Create labels for train and test data
k = np.arange(10)
train_labels = np.repeat(k,250)[:,np.newaxis]
test_labels = train_labels.copy()

# Initiate kNN, train the data, then test it with test data for k=1
knn = cv2.ml.KNearest_create()
knn.train(train,cv2.ml.ROW_SAMPLE,train_labels)
ret,result,neighbours,dist = knn.findNearest(test,k=1)

# Now we check the accuracy of classification
# For that, compare the result with test_labels and check which are wrong
matches = result == test_labels
correct = np.count_nonzero(matches)
accuracy = correct*100.0/result.size
print (accuracy)

# save the data
#np.savez('knn_data.npz',train=train, train_labels=train_labels)
"""


# Now load the data
with np.load('knn_data.npz') as data:
    #print (data.files)
    train = data['train']
    train_labels = data['train_labels']

arrayList = []
count = 1
count_num = 0

#while count == 1:
for i in range(0,1,+1):
    knn = cv2.ml.KNearest_create()
    knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)

    test_img = cv2.imread("code"+str(i)+".png")

    count_num = count_num+1
    #cv2.imshow("asd",test_img)

    test_img2 = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
    print(test_img2)
    test_img3 = cv2.resize(test_img2, (20, 20))
    cv2.imshow("asd",test_img3)
    x = np.array(test_img3)
    test_img4 = x.reshape(-1, 400).astype(np.float32)
    ret, result, neighbours, dist = knn.findNearest(test_img4, k=3)
    #print(neighbours)
    #print(ret)
    #print(dist)
    # Print the predicted number
    #print (int(result))

    arrayList.append(int(result) )
    cv2.waitKey(0)

    for i in range (0,arrayList.__len__(),+1):
        arrayList[i]
    #print(arrayList[i])
    file = open("code.txt","w")
    file.write(str(arrayList[i])+",",)


