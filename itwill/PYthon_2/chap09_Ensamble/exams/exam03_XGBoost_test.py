'''
 문) iris dataset을 이용하여 다음과 같은 단계로 XGBoost model을 생성하시오.
'''

import pandas as pd # file read
from xgboost import XGBClassifier # model 생성 
from xgboost import plot_importance # 중요변수 시각화  
import matplotlib.pyplot as plt # 중요변수 시각화 
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import confusion_matrix, accuracy_score,classification_report # model 평가 


# 단계1 : data set load 
iris = pd.read_csv("../data/iris.csv")
iris.info()

# 변수명 추출 
cols=list(iris.columns)
col_x=cols[:4] # x변수명 
col_y=cols[-1] # y변수명 

# plt.scatter(x=iris[:,0], y=iris[:,1], s=100, c=iris[:,4], marker='o')
# '(slice(None, None, None), 0)' is an invalid key
y=iris[col_y]
import numpy as np
y=np.array(y)
plt.scatter(x=iris[:,0], y=iris[:,1], c=y, marker='o')


# 단계2 : 훈련/검정 데이터셋 생성
train_set, test_set = train_test_split(iris, test_size=0.25)


# 단계3 : model 생성 : train data 이용
xgb = XGBClassifier()
model = xgb.fit(train_set[col_x], train_set[col_y])
model

# 단계4 :예측치 생성 : test data 이용 
y_pred = model.predict(test_set[col_x])
y_true = test_set[col_y]

y_pred2 = model.predict_proba(test_set[col_x])
y_pred2.shape # (38, 3)
y_pred2
'''
array([[2.1746019e-03, 9.9590498e-01, 1.9204022e-03],
       [9.9528944e-01, 3.9060446e-03, 8.0451195e-04],
       [9.9526840e-01, 3.9059622e-03, 8.2559639e-04],
       ...
'''
y_pred2.sum(axis=1)
'''array([1.        , 1.        , 0.99999994, 1.        , 1.0000001 ,
       1.0000001 , 0.99999994, 1.        , 0.99999994, 1.        ,
       ...
'''
# 확률값 -> 10진수 : .argmax(axis=1)
# 2차원(38, 3) -> 1차원(38,) : 차원 축소
y_pred2_dit = y_pred2.argmax(axis=1)
y_pred2_dit
'''array([1, 0, 0, 0, 2, 2, 0, 1, 0, 2, 1, 1, 2, 2, 2, 1, 0, 2, 1, 2, 2, 2,
       1, 2, 1, 1, 0, 0, 1, 2, 1, 0, 1, 1, 0, 1, 1, 0], dtype=int64)
'''
y_pred2_dit.shape # (38,)


# 단계5 : 중요변수 확인 & 시각화  
plot_importance(model)
#@@5
model.get_booster().get_fscore()
'''
{'Petal.Length': 121,
 'Petal.Width': 114,
 'Sepal.Length': 118,
 'Sepal.Width': 98}
'''

# 단계6 : model 평가 : confusion matrix, accuracy, report
con_mat = confusion_matrix(y_true, y_pred)
con_mat
'''array([[11,  0,  0],
       [ 0, 14,  0],
       [ 0,  1, 12]], dtype=int64)
'''

acc = accuracy_score(y_true. y_pred)
acc # 0.9916666666666667

report = classification_report(y_true, y_pred)
print(report)
'''
              precision    recall  f1-score   support

      setosa       1.00      1.00      1.00        11
  versicolor       0.93      1.00      0.97        14
   virginica       1.00      0.92      0.96        13

    accuracy                           0.97        38
   macro avg       0.98      0.97      0.98        38
weighted avg       0.98      0.97      0.97        38
'''
