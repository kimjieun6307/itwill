'''
 문) load_breast_cancer 데이터 셋을 이용하여 다음과 같이 Decision Tree 모델을 생성하시오.
 <조건1> 75:25비율 train/test 데이터 셋 구성 
 <조건2> y변수 : cancer.target, x변수 : cancer.data 
 <조건3> 중요변수 확인 

'''
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# 데이터 셋 load 
cancer = load_breast_cancer()
print(cancer)
print(cancer.DESCR)

# 변수 선택 
X = cancer.data
y = cancer.target


cancer.target_names # ['malignant', 'benign']
names = cancer.feature_names
'''
array(['mean radius', 'mean texture', 'mean perimeter', 'mean area',
       'mean smoothness', 'mean compactness', 'mean concavity',
       'mean concave points', 'mean symmetry', 'mean fractal dimension',
       'radius error', 'texture error', 'perimeter error', 'area error',
       'smoothness error', 'compactness error', 'concavity error',
       'concave points error', 'symmetry error',
       'fractal dimension error', 'worst radius', 'worst texture',
       'worst perimeter', 'worst area', 'worst smoothness',
       'worst compactness', 'worst concavity', 'worst concave points',
       'worst symmetry', 'worst fractal dimension'], dtype='<U23')
'''


# <조건1> 75:25비율 train/test 데이터 셋 구성 
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)


# <조건3> 중요변수 확인 
dtc = DecisionTreeClassifier(criterion='gini', max_depth=4, random_state=123)
model = dtc.fit(x_train, y_train)                    

# tree 시각화 관련
from sklearn import tree

tree.plot_tree(model)
#@@4

from sklearn.tree.export import export_text
print(export_text(model, names))
'''
ValueError: The truth value of an array with more than one element is ambiguous
'''
print(export_text(model))
'''
|--- feature_7 <= 0.05
|   |--- feature_20 <= 16.88
|   |   |--- feature_24 <= 0.18
|   |   |   |--- feature_13 <= 46.32
|   |   |   |   |--- class: 1
|   |   |   |--- feature_13 >  46.32
|   |   |   |   |--- class: 0
|   |   |--- feature_24 >  0.18
|   |   |   |--- class: 0
|   |--- feature_20 >  16.88
|   |   |--- feature_3 <= 722.50
|   |   |   |--- class: 0
|   |   |--- feature_3 >  722.50
|   |   |   |--- feature_17 <= 0.01
|   |   |   |   |--- class: 0
|   |   |   |--- feature_17 >  0.01
|   |   |   |   |--- class: 1
'''
names[7] # 'mean concave points'
names[20] # 'worst radius'
names[23] # 'worst area'


y_pred= model.predict(x_test)
y_true = y_test

acc=accuracy_score(y_true, y_pred)
acc # 0.9230769230769231

con_mat = confusion_matrix(y_true, y_pred)
con_mat
'''
array([[43,  5],
       [ 6, 89]], dtype=int64)
'''

dtc2 = DecisionTreeClassifier(criterion='entropy', random_state=123)
model2 = dtc2.fit(x_train, y_train)  
tree.plot_tree(model2)
#@@5
print(export_text(model2))


y_pred2= model2.predict(x_test)
y_true = y_test

acc2=accuracy_score(y_true, y_pred2)
acc2 # 0.9440559440559441

con_mat2 = confusion_matrix(y_true, y_pred2)
con_mat2
'''
array([[46,  2],
       [ 6, 89]], dtype=int64)
'''


dtc3 = DecisionTreeClassifier(max_depth=3)
model3 = dtc3.fit(x_train, y_train)  
tree.plot_tree(model3)
print(export_text(model3))
