# -*- coding: utf-8 -*-
"""
Gini 불순도(Impurity), Entropy
 - Tree model에서 중요변수 선정 기준
 - 정보이득 = base 지수 - Gini 불순도 or entropy 
 - 정보이득이 클 수록 중요변수로 본다. 
 - Gini impurity = sum(p * (1-p)) 
 - Entropy = -sum(p * log(p))
"""

import numpy as np

# 1. 불확실성이 큰 경우
# ex) 동전 앞, 뒤
x1 = 0.5; x2 = 0.5     # 전체 확률 = 1

gini = sum([x1*(1-x1), x2*(1-x2)])
print('gini=', gini)  # gini= 0.5

entropy = -sum([x1 * np.log2(x1), x2 * np.log2(x2)])
print('entropy=', entropy) # entropy= 1.0 >> 불확실성이 큰 경우임.

'''
cost(loss) function : 정답과 예측치 -> 오차 반환 함수
(entropy 수식 이용)
x1 -> y_true, x2 -> y_pred
y_true = x1 * np.log2(x1)
y_pred = x2 * np.log2(x2)
'''
y_true = x1 * np.log2(x1)
y_pred = x2 * np.log2(x2)
cost = -sum([y_true, y_pred])
print('cost = ' , cost) # cost =  1.0
# => 비용(cost)이 작으면 작을수록 오차가 적다. 



# 2. 불확실성 작은 경우
x1 = 0.9 ; x2 = 0.1    # 전체 확률 = 1

gini = sum([x1*(1-x1), x2*(1-x2)])
print('gini=', gini)  # gini= 0.18

entropy = -sum([x1 * np.log2(x1), x2 * np.log2(x2)])
print('entropy=', entropy) # entropy= 0.4689955935892812

y_true = x1 * np.log2(x1)
y_pred = x2 * np.log2(x2)
cost = -sum([y_true, y_pred])
print('cost = ' , cost) # cost =  0.4689955935892812

# => 불확실성이 큰 경우 보다 cost 값이 감소 -> 불확실성 감소


#########################
## dataset 적용
#########################

def createDataSet(): 
    dataSet = [[1, 1, 'yes'], 
               [1, 1, 'yes'], 
               [1, 0, 'no'], 
               [0, 1, 'no'], 
               [0, 1, 'no']] 
    columns = ['dark_clouds','gust'] # X1,X2 label 
    return dataSet, columns
    
dataSet, columns = createDataSet() 
print(dataSet) # [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
print(columns) # ['dark_clouds', 'gust']

type(dataSet) # list
type(columns) # list

# list -> numpy
dataset = np.array(dataSet)
dataset.shape # (5,3)

x=dataset[:, :2]
x
'''
array([['1', '1'],
       ['1', '1'],
       ['1', '0'],
       ['0', '1'],
       ['0', '1']], dtype='<U11'
'''

y=dataset[:, 2]
y # array(['yes', 'yes', 'no', 'no', 'no'], dtype='<U11')

# dummy
y = [1 if i =='yes' else 0 for i in y]
y # [1, 1, 0, 0, 0]

from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn import tree

dt = DecisionTreeClassifier()
model = dt.fit(x, y)

pred = model.predict(x)

acc = accuracy_score(y, pred)
acc # 1.0


# 중요 변수
tree.plot_tree(model)
#@@9

export_graphviz(model, out_file='dataset_tree.dot', max_depth=3, feature_names=columns)
#@@10


# criterion='entropy'
dt = DecisionTreeClassifier(criterion='entropy')
model = dt.fit(x, y)

pred = model.predict(x)

acc = accuracy_score(y, pred)
acc

tree.plot_tree(model)
#@@11




