import cv2
import os
import numpy as np
from sklearn.model_selection import train_test_split
from keras.layers import Activation, Dense, Dropout, Flatten, MaxPooling2D, Convolution2D
from keras.models import Sequential

path = './image/'

i = 0
inputData = []
category = []
for location, top, files in os.walk(path):
    for f in files:
        Y = [0, 0, 0]  # [0] apple [1] banana [2] peach
        img = cv2.imread(location + '/' + f)
        img = cv2.resize(img, None, fx=64 / img.shape[1], fy=64 / img.shape[0])
        inputData.append(img)
        Y[i] = 1
        category.append(Y)
    if files:
        i += 1

inputData = np.array(inputData)
inputData = inputData/256
category = np.array(category)

trainData, testData, trainLabel, testLabel = train_test_split(inputData, category)
print(trainData.shape)
model = Sequential()

model.add(Convolution2D(32, 3, 3, border_mode='same', input_shape=trainData.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Convolution2D(64, 3, 3, border_mode='same', input_shape=(64, 3, 3) ))
model.add(Activation('relu'))
model.add(Convolution2D(64, 3, 3))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(3))
model.add(Activation('softmax'))

model.compile(loss='binary_crossentropy',
              optimizer='Adam',
              metrics=['accuracy'])
model.fit(trainData, trainLabel, batch_size=32, epochs=50, validation_data=(testData, testLabel))
score = model.evaluate(testData, testLabel)

print('loss=', score[0])
print('accuracy=', score[1])
