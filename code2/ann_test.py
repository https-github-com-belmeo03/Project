

# If we initialize the random number generator before loading Keras, we'll get the same
# result each time we run the notebook.
import numpy as np
import cv2
np.random.seed(0)

import keras
from keras.datasets import mnist
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.models import Sequential

import matplotlib.pyplot as plt

# To set the color used to display monochrome images.
plt.rcParams['image.cmap'] = 'gray'

(x_train, y_train), (x_test, y_test) = mnist.load_data()

img_width, img_height = x_train[0].shape

print(img_width, img_height)


x_train = x_train.reshape(x_train.shape[0], img_width, img_height, 1)
x_test = x_test.reshape(x_test.shape[0], img_width, img_height, 1)
# print(x_test[0])

#Normalization image 
x_train = x_train / 255
x_test = x_test / 255
# print(x_train)
# plt.imshow(x_train[12,:,:,0]);


y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)

# # For instance, here is how the first instance in the training set is encodes.
# print(y_train[1])


# Training the CNN

num_classes = 10

model = Sequential()
model.add(Conv2D(32, kernel_size=(5, 5), strides=(1, 1),
                 activation='relu',
                 input_shape=(img_width, img_height, 1)))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Conv2D(64, (5, 5), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=256,
          epochs=5,
          verbose=1,
          validation_data=(x_test, y_test));
model.save('final_model2.h5py')



score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# plt.imshow(x_test[500,:,:,0]);


img= cv2.imread("temp/img0.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
(thresh, Img_First) = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
ima = cv2.resize(Img_First,(28,28))
w ,h= ima.shape
ima2 = ima.reshape(1, w, h, 1)
plt.imshow(ima);
print(ima)


print(h, w)
# ตรวจภาพ

guesses = model.predict_classes(ima2)

print(guesses)


probabilities = model.predict(x_test)
# print(probabilities)
def print_probs(ps):
    for p, i in sorted([(p, i) for i, p in enumerate(ps)], reverse=True):
        print(f'{i}: {p:.4f}')

# print(probabilities[500])



errors = []

for x, y, g, p in zip(x_test, y_test, guesses, probabilities):    
    if not y[g]:        
        errors.append( (p[g], p, y.argmax(), x[:,:,0]) )

errors.sort(reverse=True)

len(errors)



# def show_error(err):
#     _, p, label, img = err    
#     print('Correct label:', label)
#     print_probs(p)
#     plt.imshow(img)
        
# show_error(errors[0])

plt.show()




