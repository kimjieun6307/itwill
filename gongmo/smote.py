# -*- coding: utf-8 -*-
"""
Created on Thu May 28 18:01:47 2020

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 27 11:23:29 2020

@author: user
"""

#################
## plant_a_df.csv
#################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from sklearn.linear_model import LogisticRegression # 로지스틱 회귀분석
from sklearn.naive_bayes import GaussianNB, MultinomialNB 
from sklearn.svm import SVC 
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier

from xgboost import XGBClassifier
from xgboost import plot_importance # 중요변수 시각화


from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, cross_validate

from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score, confusion_matrix,  f1_score , classification_report

# 히트맵 : 분류정확도 결과를 시각화
import seaborn as sn # heatmap - Accuracy Score
import matplotlib.pyplot as plt

# tree 시각화 관련
from sklearn.tree.export import export_text  # ==> print(export_text(model))
from sklearn import tree  # ==> tree.plot_tree(model)




plant_a_df = pd.read_csv('plant_a_df.csv')

plant_a_df=plant_a_df.iloc[:, 1:8]
plant_a_df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 18815 entries, 0 to 18814
Data columns (total 7 columns):
 #   Column                      Non-Null Count  Dtype  
---  ------                      --------------  -----  
 0   plant1_train_mea_ddhr       18815 non-null  object 
 1   plant1_train_tem_in_loc1    18815 non-null  float64
 2   plant1_train_hum_in_loc1    18815 non-null  float64
 3   plant1_train_tem_coil_loc1  18815 non-null  float64
 4   plant1_train_tem_out_loc1   18815 non-null  float64
 5   plant1_train_hum_out_loc1   18815 non-null  float64
 6   24hour_cond_loc1 
'''
plant_a_df.columns = ['ddhr', 'tem_in', 'hum_in', 'tem_coil', 'tem_out', 'hum_out', '24hour_cond']
col = plant_a_df.columns
x_col = col[1:6]
y_col = col[-1]

X=plant_a_df[x_col]
y=plant_a_df[y_col]

X.shape #  (18815, 5)
y.value_counts()
'''
0.0    18700
1.0      115
'''


###############################
###불균형 데이터 처리 SMOTE 함수
#############################
# pip install -U imbalanced-learn # Anaconda Promt에서 설치

from imblearn.over_sampling import SMOTE


## auto##
sm = SMOTE(k_neighbors=5, random_state=71)
X_data, y_data = sm.fit_sample(X, y)


X_data.shape # (37400, 5)
y_data.shape # (37400,)

18815-37400 # -18585

y_data.value_counts()
'''
1.0    18700
0.0    18700
'''

x_train, x_test, y_train, y_test = train_test_split(X_data, y_data, test_size =0.3)

##########
# XGB
##########
xgb = XGBClassifier(random_state=123)

model_xgb = xgb.fit(x_train, y_train)
y_pred = model_xgb.predict(x_test)

acc = accuracy_score(y_test, y_pred)
acc # 0.9884135472370766

report = classification_report(y_test, y_pred)
print(report)
'''
              precision    recall  f1-score   support

         0.0       1.00      0.98      0.99      5558
         1.0       0.98      1.00      0.99      5662

    accuracy                           0.99     11220
   macro avg       0.99      0.99      0.99     11220
weighted avg       0.99      0.99      0.99     11220
'''

pd.crosstab(y_pred, y_test)
'''
24hour_cond   0.0   1.0
row_0                  
0.0          5443    15
1.0           115  5647
'''
y_test.value_counts() #11,220
'''
1.0    5662
0.0    5558
'''


##################
### RandomForest
##################

rf = RandomForestClassifier()
model = rf.fit(X=x_train, y=y_train)

y_pred = model.predict(x_test)
y_true = y_test

acc = accuracy_score(y_true, y_pred)
acc # 0.9939393939393939

report = classification_report(y_true, y_pred)
print(report)
'''
              precision    recall  f1-score   support

         0.0       1.00      0.99      0.99      5597
         1.0       0.99      1.00      0.99      5623

    accuracy                           0.99     11220
   macro avg       0.99      0.99      0.99     11220
weighted avg       0.99      0.99      0.99     11220
'''


model.feature_importances_
# array([0.20234667, 0.13226774, 0.35807944, 0.20498742, 0.10231872])

import matplotlib.pyplot as plt
plt.barh(x_col, model.feature_importances_ )
'''
plant1_train_tem_coil_loc1 >>  0.35807944
plant1_train_tem_out_loc1 >> 0.20498742
plant1_train_tem_in_loc1 >> 0.20234667
'''


#######################################################

plant_b_df = pd.read_csv('plant_b_df.csv')

plant_b_df=plant_b_df.iloc[:, 1:8]
plant_b_df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 19406 entries, 0 to 19405
Data columns (total 7 columns):
 #   Column                      Non-Null Count  Dtype  
---  ------                      --------------  -----  
 0   plant1_train_mea_ddhr       19406 non-null  object 
 1   plant1_train_tem_in_loc2    19406 non-null  float64
 2   plant1_train_hum_in_loc2    19406 non-null  float64
 3   plant1_train_tem_coil_loc2  19406 non-null  float64
 4   plant1_train_tem_out_loc1   19406 non-null  float64
 5   plant1_train_hum_out_loc1   19406 non-null  float64
 6   24hour_cond_loc2            19406 non-null  float64
 '''
 
plant_b_df.columns = ['ddhr', 'tem_in', 'hum_in', 'tem_coil', 'tem_out', 'hum_out', '24hour_cond']
col 
'''
Index(['ddhr', 'tem_in', 'hum_in', 'tem_coil', 'tem_out', 'hum_out',
       '24hour_cond'],
'''


X_b = plant_b_df[x_col]
y_b = plant_b_df[y_col]

X_b.shape #  (19406, 5)
y_b.value_counts()
'''
0.0    19199
1.0      207
'''

y_b_pred = model_xgb.predict(X_b)
acc = accuracy_score(y_b, y_b_pred)
acc # 0.9685148923013501

report=classification_report(y_b, y_b_pred)
print(report)













#########
# svm
##########

params = [0.001, 0.01, 0.1, 1, 10, 100] 
kernel = ['linear', 'rbf']
best_score = 0
best_params={} 

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

print('best parameter : ', best_params)


svc = SVC( C =10, gamma=0.01, kernel ='rbf')
model = svc.fit(x_train, y_train)

y_pred = model.predict(x_test)
y_true = y_test

acc = accuracy_score(y_true, y_pred)
acc  #0.9834224598930481

report = classification_report(y_test, y_pred)
print(report)




## 0.5 ##
sm2 = SMOTE(0.5, k_neighbors=5, random_state=71)
X_data2, y_data2 = sm2.fit_sample(X, y)

X_data2.shape # (28050, 5)
y_data2.shape

28050-18815 #9235
y_data2.value_counts()
'''
0.0    18700
1.0     9350
'''





 
