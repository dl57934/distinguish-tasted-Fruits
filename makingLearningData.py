import cv2
import os
import numpy as np
from sklearn.model_selection import train_test_split
import pickle
path = './image/'

i = 0
inputData = []
category=[]
for location, top, files in os.walk(path):
    for f in files:
        Y = [0, 0, 0]  # [0] apple [1] banana [2] peach
        img = cv2.imread(location+'/'+f)
        cv2.resize(img, None, fx=32/img.shape[1], fy=32/img.shape[0])
        X = img
        inputData.append(X)
        Y[i] = 1
        category.append(Y)
    if files:
        i += 1

inputData = np.array(inputData)
category = np.array(category)
inputData = inputData/256


trainData, testData, trainLabel, testLabel = train_test_split(inputData, category)
xy = (trainData, testData, trainLabel, testLabel)

f = open('fruit.txt', 'w')
pickle.dump(xy, f)
