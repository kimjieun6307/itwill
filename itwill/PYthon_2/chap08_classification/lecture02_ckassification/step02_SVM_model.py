# -*- coding: utf-8 -*-
"""
SVM model
    - 선형SVM, 비선형SVM
    - Hyper parameter(kernel, C, gamma) : 데이터 특성에 따라 최적의 파라미터 값을 구해야 함.
"""

import pandas as pd # csv file read
from sklearn.svm import SVC # model class
from sklearn.model_selection import train_test_split # split
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score # model 평가


# 1. dataset load
iris = pd.read_csv("C:/ITWILL/4_Python-II/data/iris.csv")
iris.info()


# 2. x, y 변수 선택
cols=list(iris.columns)
cols # ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']

x_col = cols[:4]
y_col = cols[-1]


# 3. train(0.6)/test(0.4) split
train, test = train_test_split(iris, test_size=0.4, random_state=123)


# 4. SVM model 생성
'''
비선형 svm 모형
 - default : C =1.0,  kernel ='rbf'
 - 커널 함수 종류 : Polynomial, Sigmoid, 가우시안 RBF
'''
svc = SVC( C =1.0, gamma='auto', kernel ='rbf') # 비선형 SVM model
model = svc.fit(X=train[x_col], y=train[y_col])

y_pred = model.predict(test[x_col])
y_true = test[y_col]

acc = accuracy_score(y_true, y_pred)
acc #  0.9666666666666667


'''
선형 svm 모형 :  kernel ='linear'
'''
svc2 = SVC( C =1.0, kernel ='linear') # 선형 SVM model
model2 = svc2.fit(X=train[x_col], y=train[y_col])

y_pred2 = model2.predict(test[x_col])
y_true2 = test[y_col]

acc2 = accuracy_score(y_true2, y_pred2)
acc2 # 0.9666666666666667


#######################
## Grid Search
#######################
# Hyper parameter(kernel, C, gamma)

# Cost, gamma, kernel
params = [0.001, 0.01, 0.1, 1, 10, 100] # e-3 ~ e+2 
kernel = ['linear', 'rbf']
best_score = 0
best_params={} # dict : {'kernel':'liner', 'C':0.001 } 

for k in kernel:
    for g in params :
        for c in params:
            svc = SVC(kernel=k, gamma=g, C=c)
            model = svc.fit(train[x_col], train[y_col])
            score = model.score(test[x_col], test[y_col])
            
            if score > best_score :
                best_score = score
                best_params = {'kernel': k, 'gamma' : g, 'C' : c}
        

print('best score : ', best_score)
# best score :  1.0

print('best parameter : ', best_params)
# best parameter :  {'kernel': 'rbf', 'gamma': 0.01, 'C': 100}



svc3 = SVC( C = 100, gamma=0.01, kernel ='rbf') # 비선형 SVM model
model3 = svc3.fit(X=train[x_col], y=train[y_col])

y_pred3 = model3.predict(test[x_col])
y_true3 = test[y_col]

acc3 = accuracy_score(y_true3, y_pred3)
acc3 # 1.0












