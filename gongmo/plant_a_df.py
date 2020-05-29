# -*- coding: utf-8 -*-
"""
Created on Thu May 21 13:15:37 2020

@author: user
"""
#################
## plant_a_df.csv
#################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plant_a_df = pd.read_csv('plant_a_df.csv')

plant_a_df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 18815 entries, 0 to 18814
Data columns (total 8 columns):
 #   Column                      Non-Null Count  Dtype  
---  ------                      --------------  -----  
 0   Unnamed: 0                  18815 non-null  int64  
 1   plant1_train_mea_ddhr       18815 non-null  object 
 2   plant1_train_tem_in_loc1    18815 non-null  float64
 3   plant1_train_hum_in_loc1    18815 non-null  float64
 4   plant1_train_tem_coil_loc1  18815 non-null  float64
 5   plant1_train_tem_out_loc1   18815 non-null  float64
 6   plant1_train_hum_out_loc1   18815 non-null  float64
 7   24hour_cond_loc1            18815 non-null  float64
dtypes: float64(6), int64(1), object(1)
'''

X=plant_a_df.iloc[:,1:6]
X.shape # (18815, 5)

y=plant_a_df.iloc[:,-1]
y.shape # (18815,)

y.value_counts()
'''
0.0    18700
1.0      115
'''
115/18700 #  0.006149732620320855


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

# 정규성 검정
from scipy import stats 
svalue, pvalue= stats.shapiro(plant_a_df['plant1_train_tem_in_loc1']) 
print('검정통계량 : %.5f'%(svalue)) 
print('p-value : %.5f'%(pvalue)) 

svalue, pvalue= stats.shapiro(plant_a_df['plant1_train_hum_in_loc1']) 
print('검정통계량 : %.5f'%(svalue)) 
print('p-value : %.5f'%(pvalue)) 

svalue, pvalue= stats.shapiro(plant_a_df['plant1_train_tem_coil_loc1']) 
print('검정통계량 : %.5f'%(svalue)) 
print('p-value : %.5f'%(pvalue)) 

svalue, pvalue= stats.shapiro(plant_a_df['plant1_train_tem_out_loc1']) 
print('검정통계량 : %.5f'%(svalue)) 
print('p-value : %.5f'%(pvalue)) 

svalue, pvalue= stats.shapiro(plant_a_df['plant1_train_hum_out_loc1']) 
print('검정통계량 : %.5f'%(svalue)) 
print('p-value : %.5f'%(pvalue)) 
# 5개 x변수 모두 pvalue < 0.05 : 정규분포 아님

# plt.hist
plt.hist(plant_a_df['plant1_train_tem_in_loc1'])
plt.hist(plant_a_df['plant1_train_hum_in_loc1'])
plt.hist(plant_a_df['plant1_train_tem_coil_loc1'])
plt.hist(plant_a_df['plant1_train_tem_out_loc1'])
plt.hist(plant_a_df['plant1_train_hum_out_loc1'])

X.plot(kind = 'kde')

# 산점도
X_arr=np.array(X)
y_arr = np.array(y)

X.columns
'''Index(['plant1_train_tem_in_loc1', 'plant1_train_hum_in_loc1',
       'plant1_train_tem_coil_loc1', 'plant1_train_tem_out_loc1',
       'plant1_train_hum_out_loc1'],
'''

fig = plt.figure(figsize = (5, 3)) # 차트 크기 지정
x1 = fig.add_subplot(2,2,1)
x2 = fig.add_subplot(2,2,2)
x3 = fig.add_subplot(2,2,3)
x4 = fig.add_subplot(2,2,4)

x1.scatter(x=X_arr[:,0], y=X_arr[:,2], c=y_arr, marker='.')
x2.scatter(x=X_arr[:,0], y=X_arr[:,3], c=y_arr, marker='o')
x3.scatter(x=X_arr[:,2], y=X_arr[:,3], c=y_arr, marker='*')
x4.scatter(x=X_arr[:,1], y=X_arr[:,4], c=y_arr, marker='+')

# 산점도 matrix 
from pandas import plotting
plotting.scatter_matrix(X)

# split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

18815*0.3 # 5644.5

########################
# XGB model
########################
xgb = XGBClassifier()
model = xgb.fit(X, y)

plot_importance(model)
model.get_booster().get_fscore()
'''
{'plant1_train_tem_coil_loc1': 349, <--★
 'plant1_train_tem_in_loc1': 259,
 'plant1_train_tem_out_loc1': 228,
 'plant1_train_hum_in_loc1': 327,  <--★
 'plant1_train_hum_out_loc1': 274}
'''

model = xgb.fit(x_train, y_train)

y_pred = model.predict(x_test)

acc = accuracy_score(y_test, y_pred)
acc # 0.9946855624446412

report = classification_report(y_test, y_pred)
print(report)
'''
              precision    recall  f1-score   support

         0.0       1.00      1.00      1.00      5612
         1.0       0.71      0.15      0.25        33

    accuracy                           0.99      5645
   macro avg       0.85      0.58      0.62      5645
weighted avg       0.99      0.99      0.99      5645
'''

###################
# RandomForest
####################
rf = RandomForestClassifier()
model = rf.fit(X, y)

# 단계4. 교차검정 model 예측/평가 
score = cross_validate(model, X, y, cv=5)
test_score=score['test_score']
test_score.mean() # 0.9914429976082912


# 단계5. 중요변수 시각화 
model.feature_importances_
'''
array([0.21821939, 0.18774164, 0.2151461 , 0.19832923, 0.18056364])
'''
plt.barh(X.columns, model.feature_importances_)
# tem_coil, tem_in

# 최적 parameter
from sklearn.model_selection import GridSearchCV
params = {'n_estimators' : [100, 200, 300, 400], 'max_depth':[3, 6, 8, 10], 
           'min_samples_split' : [2,3,4,5], 'min_samples_leaf' : [1,3,5,7]}

gs = GridSearchCV(estimator = model, param_grid = params, scoring = 'accuracy', cv=5, n_jobs=-1)

model = gs.fit(X, y)

# best score
score = model.score(X, y)
score  # 0.9938878554344938

# best parameter
model.best_params_ 
'''
{'max_depth': 3,
 'min_samples_leaf': 1,
 'min_samples_split': 2,
 'n_estimators': 100}
'''

rf = RandomForestClassifier(max_depth=3, min_samples_leaf=1, min_samples_split=2, n_estimators=100)
model = rf.fit(x_train, y_train)

y_pred = model.predict(x_test)
y_true = y_test

y_pred.size # 5645

pd.crosstab(y_pred, y_true)
'''
24hour_cond_loc1   0.0  1.0
row_0                      
0.0               5612   33
'''

acc = accuracy_score(y_true, y_pred)
acc #  0.9941541186891054

report = classification_report(y_true, y_pred)
print(report)
'''
              precision    recall  f1-score   support

         0.0       0.99      1.00      1.00      5612
         1.0       0.00      0.00      0.00        33

    accuracy                           0.99      5645
   macro avg       0.50      0.50      0.50      5645
weighted avg       0.99      0.99      0.99      5645
'''
















