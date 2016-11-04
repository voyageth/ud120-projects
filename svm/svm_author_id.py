#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#########################################################
print('start')
from sklearn import svm
clf = svm.SVC(kernel='rbf', C=10000.0)
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

clf.fit(features_train, labels_train)
print('fit end')

pred = clf.predict(features_test)
print('predict end')

cnt = 0
for i in range(0, len(pred)) :
    if pred[i] == 1 :
        cnt+=1

print ('count', cnt)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test, pred)
print("accuracy : {}".format(accuracy))

