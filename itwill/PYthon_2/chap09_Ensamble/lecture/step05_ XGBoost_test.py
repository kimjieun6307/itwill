# -*- coding: utf-8 -*-
"""
XGBoost model : 분류트리(XGBClassifier)
> anaconda prompt 에서 별도 인스톨 필요
> pip install xgboost 
"""

from xgboost import XGBClassifier, XGBRegressor # model
from xgboost import plot_importance # 중요변수 시각화
from sklearn.datasets import make_blobs # 클러스터 데이터셋 생성
from sklearn.model_selection import train_test_split # split
from sklearn.metrics import accuracy_score, classification_report # 평가
import matplotlib.pyplot as plt # 데이터셋 시각화


# 1. dataset load
X, y = make_blobs(n_samples=2000, n_features=4, centers=2, cluster_std=2.5)
'''
def make_blobs(n_samples=100, --> 데이터셋 크기
 n_features=2,  --> x변수 
 centers=None,  --> y변수 범주(군집수) 
 cluster_std=1.0,  --> 클러스터 표준편차(클수록 오분류 커짐)
 center_box=(-10.0, 10.0), shuffle=True, random_state=None):
'''
X.shape  # (2000, 4)
y.shape  # (2000, )
y  # array([0, 1, 0, ..., 0, 1, 0])
'''
import numpy as np
np.unique(y) # array([0, 1])
'''

# 산점도 통해서 데이터 확인
plt.scatter(x=X[:,0], y=X[:,1], s=100, c=y, marker='o')
'''
c=y : y에 대한 색상 구분
#@@1
'''

# 2. train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)


# 3. model 생성
xgb = XGBClassifier()
model = xgb.fit(x_train, y_train)
model
'''(기본 파라미터 확인 할수 있음)
XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
              colsample_bynode=1, colsample_bytree=1, gamma=0, gpu_id=-1,
              importance_type='gain', interaction_constraints='',
              learning_rate=0.300000012, max_delta_step=0, max_depth=6,
              min_child_weight=1, missing=nan, monotone_constraints='()',
              n_estimators=100, n_jobs=0, num_parallel_tree=1,
              objective='binary:logistic', random_state=0, reg_alpha=0,
              reg_lambda=1, scale_pos_weight=1, subsample=1,
              tree_method='exact', validate_parameters=1, verbosity=None)

>> n_estimators=100 : 100개의 트리(random forest와 동일)
>> objective='binary:logistic' : 이항분류
>> max_depth=6 : 트리 깊이
>> learning_rate=0.300000012 : 학습률 (작으면 작을 수록 정밀하게 학습-> 정확도 높아짐)
'''

# 4. model 평가
y_pred = model.predict(x_test)

acc = accuracy_score(y_test, y_pred)
acc # 0.9933333333333333

report = classification_report(y_test, y_pred)
print(report)
'''
              precision    recall  f1-score   support

           0       1.00      0.99      0.99       300
           1       0.99      1.00      0.99       300

    accuracy                           0.99       600
   macro avg       0.99      0.99      0.99       600
weighted avg       0.99      0.99      0.99       600
'''


# 5. 중요변수 시각화
plot_importance(model)
plt.show
#@@2

model.get_booster().get_fscore()
#  {'f3': 91, 'f1': 65, 'f0': 38, 'f2': 36}

##########################
## centers=3
##########################
# 1. dataset load
X, y = make_blobs(n_samples=2000, n_features=4, centers=3, cluster_std=2.5)

X.shape  # (2000, 4)
y.shape  # (2000, )
y # array([2, 2, 2, ..., 0, 0, 0])

np.unique(y) array([0, 1, 2])


# 산점도 통해서 데이터 확인
plt.scatter(x=X[:,0], y=X[:,1], s=100, c=y, marker='o')
#@@3

# 2. train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)


# 3. model 생성
xgb = XGBClassifier()
model = xgb.fit(x_train, y_train)
model #  objective='multi:softprob' --> 다항분류

# 4. model 평가
y_pred = model.predict(x_test)

acc = accuracy_score(y_test, y_pred)
acc  # 0.9916666666666667


report = classification_report(y_test, y_pred)
print(report)
'''
            precision    recall  f1-score   support

           0       0.99      0.98      0.99       187
           1       1.00      1.00      1.00       209
           2       0.99      0.99      0.99       204

    accuracy                           0.99       600
   macro avg       0.99      0.99      0.99       600
weighted avg       0.99      0.99      0.99       600
'''

# 5. 중요변수 시각화
plot_importance(model)
#@@4

model.get_booster().get_fscore()
# {'f0': 287, 'f2': 302, 'f1': 262, 'f3': 176}



