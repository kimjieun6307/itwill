# -*- coding: utf-8 -*-
"""
NB vs SVM : 희소행렬(고차원)
 - 가중치 적용 : Tfidf
"""

from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np # np file load # chap07/data -> spam_data.npy


# file load : allow_pickle=True
# lecture04_SparseMatrix 참고
x_train, x_test, y_train, y_test = np.load('C:/ITWILL/4_Python-II/workspace/chap07_TextMining/data/spam_data.npy', 
                                           allow_pickle=True)
x_train.shape # (3901, 4000)
x_test.shape

# list-> numpy
y_train.shape # AttributeError: 'list' object has no attribute 'shape'
y_train = np.array(y_train)
y_test = np.array(y_test)
y_train.shape # (3901,)
y_test.shape # (1673,)


# 2. NB model
nb = MultinomialNB()
model = nb.fit(X=x_train, y=y_train)

y_pred = model.predict(x_test)
y_true = y_test

acc=accuracy_score(y_true, y_pred)
acc # 0.9748953974895398

con_mat = confusion_matrix(y_true, y_pred)
con_mat
'''
array([[1446,    1],
       [  41,  185]], dtype=int64)
'''
# spam에 대한 오분류
185/(41+185) #  0.8185840707964602


# 3. SVM model
svc = SVC(gamma='auto')
model_svc = svc.fit(X=x_train, y=y_train)

y_pred2 = model_svc.predict(x_test)
y_true2 = y_test

acc=accuracy_score(y_true2, y_pred2)
acc # 0.8649133293484758

con_mat = confusion_matrix(y_true2, y_pred2)
con_mat
'''
array([[1447,    0],
       [ 226,    0]], dtype=int64)
'''

# 선형svm
svc2 = SVC(kernel='linear',)
model_svc2 = svc2.fit(X=x_train, y=y_train)

y_pred3 = model_svc.predict(x_test)
y_true3 = y_test

acc=accuracy_score(y_true3, y_pred3)
acc # 0.8649133293484758

con_mat = confusion_matrix(y_true3, y_pred3)
con_mat
'''
array([[1447,    0],
       [ 226,    0]], dtype=int64)
'''

# Hyper parameter(kernel, C, gamma)

params = [0.001, 0.01, 0.1, 1, 10, 100] # e-3 ~ e+2 
kernel = ['linear', 'rbf']
best_score = 0
best_params={} # dict : {'kernel':'liner', 'C':0.001 } 
for k in kernel:
    for g in params :
        for c in params:
            svc = SVC(kernel=k, gamma=g, C=c)
            model = svc.fit(x_train, y_train)
            score = model.score(x_test, y_test)  
            if score > best_score :
                best_score = score
                best_params = {'kernel': k, 'gamma' : g, 'C' : c}    

print('best score : ', best_score)
# best score :  0.9814704124327556
print('best parameter : ', best_params)
# best parameter :  {'kernel': 'rbf', 'gamma': 0.1, 'C': 10}














