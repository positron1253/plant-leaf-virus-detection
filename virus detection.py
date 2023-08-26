import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers import Conv2D,Dense,Dropout,Flatten,MaxPooling2D,Input,BatchNormalization
from tensorflow.keras.models import Sequential
from tensorflow.keras.models import Model
from tensorflow.python.framework import ops
from tensorflow.keras.utils import to_categorical
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import os
import cv2


dir = "PLD_3_Classes_256\Training"
x=[]
y=[]
for direct in os.listdir(dir):
    print("Loading dataset training {}".format(direct))
    for filename in os.listdir(os.path.join(dir,direct)):
        img_path = os.path.join(dir,direct,filename)
        image = cv2.imread(img_path)
        image = cv2.resize(image,(32,32))
        image = np.array(image)
        image = image/255
        x.append(image)
        y.append(direct)


dir_val = "PLD_3_Classes_256/Validation"
x_val=[]
y_val=[]
for direct in os.listdir(dir_val):
    print("Loading dataset validation {}".format(direct))
    for filename in os.listdir(os.path.join(dir_val,direct)):
        img_path = os.path.join(dir_val,direct,filename)
        image = cv2.imread(img_path)
        image = cv2.resize(image,(32,32))
        image = np.array(image)
        image = image/255
        x_val.append(image)
        y_val.append(direct)

from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
le = LabelEncoder()
int_labels = le.fit_transform(y)
encode_label = np_utils.to_categorical(int_labels)

print(int_labels)

print(encode_label)

from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
le = LabelEncoder()
int_labels = le.fit_transform(y_val)
encode_label_val = np_utils.to_categorical(int_labels)

x = np.array(x)

x_val = np.array(x_val)

from sklearn.utils import shuffle
x,encode_label = shuffle(x,encode_label)
x_val,encode_label_val = shuffle(x_val,encode_label_val)


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(x,encode_label,test_size=0.2)

Y_train = np.array([np.array(i) for i in Y_train])
Y_test = np.array([np.array(i) for i in Y_test])
encode_label_val = np.array([np.array(i) for i in encode_label_val])

print(Y_train)


model = Sequential()

model.add(Conv2D(32, (3, 3), padding='same', input_shape=(32, 32, 3), activation='relu'))
model.add(Conv2D(64,(3,3),padding='same',activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())

model.add(Flatten())
model.add(Dropout(0.2))
model.add(Dense(64, activation='relu'))
model.add(Dense(3, activation='softmax'))


model.summary()

model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])

from keras.callbacks import ModelCheckpoint
filepath = 'my_best_model.hdf5'
checkpoint = ModelCheckpoint(filepath=filepath,
                             monitor='val_loss',
                             verbose=1,
                             save_best_only=True,
                             mode='min')
callbacks = [checkpoint]


model.save("my_model")




test_img_path = "PLD_3_Classes_256/Testing/Healthy/Healthy_3.jpg"

test_arr = []
test_image = cv2.imread(test_img_path)
test_image = cv2.resize(test_image,(32,32))
test_image = np.array(test_image)
test_image = test_image/255
test_image = test_image.reshape(1,32,32,3)
test_arr.append(test_image)
print(test_arr)
print("hi")

model.predict(test_arr) 

