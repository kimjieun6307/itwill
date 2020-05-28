# -*- coding: utf-8 -*-
"""
sklearn 로지스틱 회귀모델
 - y변수가 범주형인 경우
"""

from sklearn.datasets import load_breast_cancer, load_iris # dataset 
from sklearn.linear_model import LogisticRegression # model 생성
from sklearn.metrics import accuracy_score, confusion_matrix # model 평가(분류정확도)


#############################
## 1. 이항분류 모델
############################

# 1. dataset load & 변수 선택
breast = load_breast_cancer()

X = breast.data # x변수
y = breast.target # y변수

X.shape #  (569, 30)
y.shape #  (569,)


pd.unique(y) # array([0, 1])


#2. model 생성-로지스틱 이항분류 : LogisticRegression(기본값)
help(LogisticRegression)
#@@3
'''
random_state=None, solver='lbfgs', max_iter=100, multi_class='auto'

random_state=None : 난수 seed값 지정
solver='lbfgs' : 알고리즘(기본 => 'lbfgs') 
 - 데이터 특성에 따라 알고리즘 선택 {'newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'}
#@@4
max_iter=100 : 반복학습 횟수(기본 => 100)
multi_class='auto' : 다항분류 지정할때 사용
 - multi_class : {'auto', 'ovr', 'multinomial'}, default='auto'

※ 적용 예)
일반 데이터, 이항분류 : default(기본값)
일반 데이터, 다항분류 : solver = 'lbfgs', multi_class = 'multinomial'
빅 데이터, 이항분류 :  solver = 'sag' or 'saga'
빅 데이터, 다항분류 : solver = 'sag' or 'saga', multi_class = 'multinomial'

'''

lr = LogisticRegression(random_state=123)
# multi_class = 'auto'(기본값) : sigmoid 활용함수 이용 -> 이항분류
model = lr.fit(X, y)
model # LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)


# 3. model 평가 => 분류정확도(accuracy_score), confusion_matrix
acc = model.score(X, y)
print('accuracy = ', acc) # accuracy =  0.9472759226713533

y_pred = model.predict(X)
acc2 = accuracy_score(y, y_pred)
acc2 # 0.9472759226713533

con_max = confusion_matrix(y, y_pred)
print(con_max)
'''
[[193  19]
 [ 11 346]]
'''
type(con_max) # numpy.ndarray

acc3 = (con_max[0,0] + con_max[1,1])/con_max.sum()
acc3 # 0.9472759226713533

import pandas as pd

tab = pd.crosstab(y, y_pred, rownames=['관측치'], colnames=['예측치'])
tab
'''
예측치    0    1
관측치          
0    193   19
1     11  346
'''
acc4 = (tab.loc[0,0] + tab.loc[1,1]) / len(y) # sum(tab)=1
acc4 # 0.9472759226713533


###################################
## 2. 다항분류 모델
##################################

# 1. dataset load
iris = load_iris()
iris.target_names #  array(['setosa', 'versicolor', 'virginica'], dtype='<U10')

X, y = load_iris(return_X_y=True)

X.shape(150, 4)
y.shape(150,)

pd.unique(y) # array([0, 1, 2])

# 2. model 생성-로지스틱 다항분류 : LogisticRegression(multi_class = 'multinomial')
# 일반 데이터, 다항분류 : solver = 'lbfgs', multi_class = 'multinomial'
ls = LogisticRegression(random_state=123, solver = 'lbfgs', multi_class = 'multinomial')
# multi_class = 'multinomial' : softmax 활용함수 이용 -> 다항분류

'''
sigmoid function : 0 ~ 1 확률값 -> cutoff=0.5 -> 이항분류
softmax function : 0 ~ 1 확률값 -> 전체합 = 1(c0:0.1, c1 :0.1, c2:0.8) -> 다항분류
'''

model = ls.fit(X, y)

y_pred = model.predict(X) # class(도메인)
y_pred2 = model.predict_proba(X) # 확률값

y_pred # 0~2
y_pred2 
'''
array([[9.81797141e-01, 1.82028445e-02, 1.44269293e-08],
       [9.71725476e-01, 2.82744937e-02, 3.01659208e-08],
       [9.85444223e-01, 1.45557643e-02, 1.23263078e-08],
       [9.76282998e-01, 2.37169623e-02, 3.97229604e-08],
       [9.85381263e-01, 1.46187255e-02, 1.19450737e-08],
       [9.70457205e-01, 2.95427213e-02, 7.35307149e-08],
       ~~
'''
y_pred2.shape # (150, 3)


print(iris.target_names) 
#  ['setosa' 'versicolor' 'virginica']
#  [9.81797141e-01, 1.82028445e-02, 1.44269293e-08]

import numpy as np
arr = np.array([9.81797141e-01, 1.82028445e-02, 1.44269293e-08])
arr.max() # 0.981797141 ==> 'setosa'
arr.min() # 1.44269293e-08
arr.sum() # 0.9999999999269293 ==> 전체합 = 1

# 3. model 평가
acc = accuracy_score(y, y_pred)
acc # 0.9733333333333334 (예측치)

con_mat = confusion_matrix(y, y_pred)
con_mat
'''
array([[50,  0,  0],
       [ 0, 47,  3],
       [ 0,  1, 49]], dtype=int64)
'''
acc2 = (con_max[0,0]+con_max[1,1]+con_max[2,2])/con_max.sum()
acc2 # 0.9733333333333334

# 히트맵 : 분류정확도 결과를 시각화
import seaborn as sn # heatmap - Accuracy Score
import matplotlib.pyplot as plt

# confusion matrix heatmap 
plt.figure(figsize=(6,6)) # chart size
sn.heatmap(con_mat, annot=True, fmt=".3f", linewidths=.5, square = True);# , cmap = 'Blues_r' : map »ö»ó 
plt.ylabel('Actual label');
plt.xlabel('Predicted label');
all_sample_title = 'Accuracy Score: {0}'.format(acc)
plt.title(all_sample_title, size = 18)
plt.show()
#@@5




######################################
## Y범주: mulit class 다항 분류
###################################


# 1. dataset load
digits = datasets.load_digits() # <error> digits = load_digits() -- import 안했기때문
print(digits.DESCR)
digits.target_names # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

X = digits.data
y = digits.target

X.shape # (1797, 64) -> 1797장 images
y.shape # (1797,) -> 1797장 images 10진수 정답


# 2. split
from sklearn.model_selection import train_test_split
img_train, img_test, label_train, label_test = train_test_split(X, y)

# 훈련셋 image -> reshape
img2d = img_train.reshape(-1,8,8) # (전체 image, 세로, 가로)
img2d.shape # (1347, 8, 8)
img2d[0]
'''
array([[ 0.,  0., 15., 16., 16., 15.,  9.,  0.],
       [ 0.,  6., 16., 13., 12., 12., 11.,  2.],
       [ 0.,  3., 15., 14.,  2.,  0.,  0.,  0.],
       [ 0.,  0.,  6., 16.,  5.,  0.,  0.,  0.],
       [ 0.,  0.,  0., 14., 11.,  0.,  0.,  0.],
       [ 0.,  0.,  0., 12.,  8.,  0.,  0.,  0.],
       [ 0.,  1., 14., 14., 10.,  0.,  0.,  0.],
       [ 0.,  0., 13., 16.,  3.,  0.,  0.,  0.]])
'''
plt.imshow(img2d[0])
#@@7
label_train[0] # 5

# 3. model 생성
ls = LogisticRegression(multi_class = 'multinomial')
model = ls.fit(img_train, label_train)


# 4. model 평가
y_pred = model.predict(img_test)

acc = accuracy_score(label_test, y_pred)
acc # 0.9688888888888889

con_mat = confusion_matrix(label_test, y_pred)
con_mat
'''
array([[47,  0,  0,  0,  0,  0,  0,  0,  0,  0],
       [ 0, 49,  0,  0,  0,  0,  0,  0,  1,  0],
       [ 0,  1, 45,  0,  0,  0,  0,  0,  0,  0],
       [ 0,  0,  0, 42,  0,  1,  0,  0,  0,  1],
       [ 0,  0,  0,  0, 33,  0,  0,  0,  0,  0],
       [ 0,  0,  0,  0,  0, 42,  1,  0,  0,  2],
       [ 0,  0,  0,  0,  0,  1, 43,  0,  0,  0],
       [ 0,  0,  0,  0,  1,  0,  0, 39,  0,  0],
       [ 1,  1,  1,  0,  0,  0,  0,  0, 46,  0],
       [ 0,  0,  0,  0,  0,  2,  0,  0,  0, 50]], dtype=int64)
'''

result = label_test == y_pred
result
len(result) #450
pd.value_counts(result) # <error> result.value_counts --numpy 자료형
'''
True     436
False     14
dtype: int64
'''

# True -> 1, False -> 0
result.mean() #  0.96888888888888

# 틀린 image
false_img = img_test[result==False]
false_img.shape # (14, 64)

for img in false_img : 
    fal_img2d = img.reshape(8,8)
    plt.imshow(fal_img2d)
    plt.show()
#@@8
    


# confusion matrix heatmap 
plt.figure(figsize=(6,6)) # chart size
sn.heatmap(con_mat, annot=True, fmt=".3f", linewidths=.5, square = True);# , cmap = 'Blues_r' : map »ö»ó 
plt.ylabel('Actual label');
plt.xlabel('Predicted label');
all_sample_title = 'Accuracy Score: {0}'.format(acc)
plt.title(all_sample_title, size = 18)
plt.show()
#@@9


