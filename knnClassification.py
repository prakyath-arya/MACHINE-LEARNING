# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:52:13 2020

@author: arya
"""

#import packages
import pandas as pd
from sklearn import neighbors

#title
print('THIS IS A KNN CLASSIFICATION ALGORITM TO PREDICT IF X CAN WIN A TIC-TAC-TOE MATCH OR NOT BASED ON THE X-O-X TABLE')

#import dataset
data = pd.read_csv('C:\\Users\\aryap\\Downloads\\ENGINEERING\\Semester 6\\MNL\\Asssignment\\tictactoe.csv')

#load the training set
trainSet = []
for index, rows in data.iterrows():
    x = [rows.topleft, rows.topmiddle, rows.topright, rows.middleleft, rows.middlemiddle, rows.middleright, rows.bottomleft, rows.bottommiddle, rows.bottomright]
    trainSet.append(x)
    
#load the class label
classLabel = []
for index, rows in data.iterrows():
    y = rows.canXwin
    classLabel.append(y)
    
#using knn classification algorithm
knnclf = neighbors.KNeighborsClassifier()
knnclf.fit(trainSet, classLabel)

#taking testing set
table = eval(input('ENTER THE tic-tac-toe TABLE VALUES AS A LIST: \n1 for X\n0 for O\n-1 for blank space\n'))
if(len(table) != 9):
    print('WRONG TABLE FORMAT')
else:
    print('\n')
    prediction = knnclf.predict([table])
    
    #print the result
    if(prediction == [1]):
        print('X can win')
    else:
        print('X cannot win')
