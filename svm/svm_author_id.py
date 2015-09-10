#!/usr/bin/python

"""
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors

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
from sklearn import svm
from sklearn.metrics import accuracy_score
import time

clf = svm.SVC(C=10000, kernel="rbf")
print clf.C
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
start_train = time.time()
clf.fit(features_train, labels_train)
print "Train time: %fs" %(time.time()-start_train)
start_predict = time.time()
pred = clf.predict(features_test)
print "Predict time: %fs" %(time.time()-start_predict)
acc = accuracy_score(pred, labels_test)
print acc

i = 0
for x in pred:
	if x == 1:
		i += 1

print "Of %d emails, Chris wrote %d" %(len(pred), i)





#########################################################


