# -*- coding: utf-8 -*-
"""
Random Forest Ensemble model
"""

from sklearn.ensemble import RandomForestClassifier # model
from sklearn.datasets import load_wine # dataset
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. dataset load
wine = load_wine()
wine.feature_names # x변수명
'''
['alcohol',
 'malic_acid',
 'ash',
 'alcalinity_of_ash',
 'magnesium',
 'total_phenols',
 'flavanoids',
 'nonflavanoid_phenols',
 'proanthocyanins',
 'color_intensity',
 'hue',
 'od280/od315_of_diluted_wines',
 'proline']
'''

wine.target_names # y범주 이름 : ['class_0', 'class_1', 'class_2']

X = wine.data
y = wine.target

X.shape # (178, 13)


# 2. RF model
#@@1
'''
Parameters
    ----------
    n_estimators : integer, optional (default=100) : 트리 수 
    criterion : string, optional (default="gini") or 'entropy ' : 중요변수 선정
    max_depth : integer or None, optional (default=None) : 트리 깊이
    min_samples_split : int, float, optional (default=2) : 노드 분할 최소 샘플수
    min_samples_leaf : int, float, optional (default=1) : 단노드 분할 최소 샘플수
    max_features : int, float, string or None, optional (default="auto") : 최대 x변수 사용 수
    n_jobs : int or None, optional (default=None) : cpu 수
    random_state : int, RandomState instance or None, optional (default=None)
'''
rf = RandomForestClassifier()
rf
'''
RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_weight=None,
                       criterion='gini', max_depth=None, max_features='auto',
                       max_leaf_nodes=None, max_samples=None,
                       min_impurity_decrease=0.0, min_impurity_split=None,
                       min_samples_leaf=1, min_samples_split=2,
                       min_weight_fraction_leaf=0.0, n_estimators=100,
                       n_jobs=None, oob_score=False, random_state=None,
                       verbose=0, warm_start=False)
'''

import numpy as np

idx = np.random. choice(a=X.shape[0], size = int(X.shape[0]*0.7), replace=False)
x_train = X[idx]
y_train = y[idx]
len(idx) # 124

model = rf.fit(X=x_train, y=y_train)

idx_test = [i for i in range(len(X)) if not i in idx]
len(idx_test) # 54

x_test = X[idx_test]
y_test = y[idx_test]

x_test.shape # (54, 13)

y_pred = model.predict(x_test)
y_true = y_test

con_mat = confusion_matrix(y_true, y_pred)
'''array([[19,  0,  0],
       [ 0, 19,  0],
       [ 0,  0, 16]], dtype=int64)
'''

acc = accuracy_score(y_true, y_pred)
acc # 1.0

report = classification_report(y_true, y_pred)
print(report)
'''
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        19
           1       1.00      1.00      1.00        19
           2       1.00      1.00      1.00        16

    accuracy                           1.00        54
   macro avg       1.00      1.00      1.00        54
weighted avg       1.00      1.00      1.00        54
'''

# 중요변수
model.feature_importances_
''' <13개 x변수에 대한 중요도>
array([0.17959468, 0.01977275, 0.01784574, 0.03216793, 0.02941793,
       0.05264511, 0.13071938, 0.0107501 , 0.03303759, 0.14282835,
       0.0949595 , 0.10298377, 0.15327718])
'''
# model(criterion = "gini")로 계산된 중요도임.

len(model.feature_importances_) # 13

wine.feature_names # x변수명
'''
['alcohol',
 'malic_acid',
 'ash',
 'alcalinity_of_ash',
 'magnesium',
 'total_phenols',
 'flavanoids',
 'nonflavanoid_phenols',
 'proanthocyanins',
 'color_intensity',
 'hue',
 'od280/od315_of_diluted_wines',
 'proline']
'''

# 중요변수 시각화
import matplotlib.pyplot as plt

plt.barh(wine.feature_names, model.feature_importances_ ) # (y,x)
# @@3

x_size = X.shape[1]
plt.barh(range(x_size), model.feature_importances_)
plt.yticks(range(x_size), wine.feature_names)
plt.xlabel('importance')
plt.show()
#@@4










