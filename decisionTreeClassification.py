# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:40:39 2020

@author: arya
"""

#import packages
import pandas as pd
from sklearn import tree

#title
print('THIS IS A DECISION TREE CLASSIFICATION ALGORITM TO PREDICT IF X CAN WIN A TIC-TAC-TOE MATCH OR NOT BASED ON THE X-O-X TABLE')

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
 
#using decision tree classification algorithm
dtclf = tree.DecisionTreeClassifier()
dtclf.fit(trainSet, classLabel)

#taking testing set
a = eval(input('ENTER THE tic-tac-toe TABLE VALUES AS A LIST: \n1 for X\n0 for O\n-1 for blank space\n'))
if(len(a) != 9):
    print('WRONG TABLE FORMAT')
else:
    print('\n')
    prediction = dtclf.predict([a])
    
    #print the result
    if(prediction == [1]):
        print('X can win')
    else:
        print('X cannot win')
