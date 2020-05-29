# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:45:57 2020

@author: user
"""
#################
## plant_a_df.csv
#################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
 6   24hour_cond_loc1            18815 non-null  float64
'''

df_no = plant_a_df[plant_a_df['24hour_cond_loc1']==0]
df_yes = plant_a_df[plant_a_df['24hour_cond_loc1']==1]

df_no.shape # (18700, 7)
df_yes.shape #  (115, 7)


###########################################
## 상대적으로 결로 관측값이 너무 적어서 관측값 비슷하게 맞춤 120:115
#########################################

df_no_sam = df_no.sample(120)
df_no_sam.shape # (120, 7)


'''
df_sam = pd.merge(df_no_sam, df_yes)
df_sam.shape # (0, 7)
df_sam.info()
'''
df_sam = pd.concat([df_no_sam, df_yes])
df_sam.info()
df_sam.head()

col = df_sam.columns
x_col = col[1:6]
y_col = col[-1]

X=df_sam[x_col]
y=df_sam[y_col]


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

# 산점도
from pandas import plotting
plotting.scatter_matrix(X)

# 정규성 검정
from scipy import stats 
svalue, pvalue= stats.shapiro(X)
print('검정통계량 : %.5f'%(svalue)) # 검정통계량 : 0.94175
print('p-value : %.5f'%(pvalue)) # p-value : 0.00000

svalue, pvalue= stats.shapiro(X.iloc[:,1])
print('검정통계량 : %.5f'%(svalue)) # 검정통계량 : 0.99021
print('p-value : %.5f'%(pvalue)) # p-value : 0.00000

stats.shapiro(X.iloc[:,2]) # (0.9500656723976135, 4.497104725050916e-20)
stats.shapiro(X.iloc[:,3]) # (0.9670422673225403, 3.7304064209974354e-16)
stats.shapiro(X.iloc[:,4]) # (0.9818345308303833, 2.434868799638945e-11)


# split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size =0.3)

########################
# XGB model
########################
xgb = XGBClassifier()

model = xgb.fit(x_train, y_train)
model

y_pred = model.predict(x_test)

acc = accuracy_score(y_test, y_pred)
acc # 0.8309859154929577

report = classification_report(y_test, y_pred)
print(report)
'''
              precision    recall  f1-score   support

         0.0       0.89      0.73      0.80        33
         1.0       0.80      0.92      0.85        38

    accuracy                           0.83        71
   macro avg       0.84      0.82      0.83        71
weighted avg       0.84      0.83      0.83        71
'''

pd.crosstab(y_pred, y_test)
'''
24hour_cond_loc1  0.0  1.0
row_0                     
0.0                24    3
1.0                 9   35
'''
y_test.value_counts()
'''
1.0    38
0.0    33
'''


#########
# svm
##########
svc = SVC( C =1.0, gamma='auto', kernel ='rbf')
model = svc.fit(x_train, y_train)

y_pred = model.predict(x_test)
y_true = y_test

acc = accuracy_score(y_true, y_pred)
acc

report = classification_report(y_test, y_pred)
print(report)

pd.crosstab(y_pred, y_test)
'''
24hour_cond_loc1  0.0  1.0
row_0                     
0.0                34   15
1.0                 2   20
'''

con_mat = confusion_matrix(y_true, y_pred)
con_mat
'''
array([[34,  2],
       [15, 20]], dtype=int64)
'''

# 선형(kernel ='linear')
svc2 = SVC( C =1.0, kernel ='linear')
model2 = svc2.fit(x_train, y_train)

y_pred = model2.predict(x_test)
y_true = y_test

acc = accuracy_score(y_true, y_pred)
acc # 0.8591549295774648

report = classification_report(y_test, y_pred)
print(report)

'''
              precision    recall  f1-score   support

         0.0       0.93      0.78      0.85        36
         1.0       0.80      0.94      0.87        35

    accuracy                           0.86        71
   macro avg       0.87      0.86      0.86        71
weighted avg       0.87      0.86      0.86        71
'''

pd.crosstab(y_pred, y_test)
'''
24hour_cond_loc1  0.0  1.0
row_0                     
0.0                28    2
1.0                 8   33
'''
y_test.value_counts()
'''
0.0    36
1.0    35
'''



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
# best score :  0.9154929577464789
print('best parameter : ', best_params)
# best parameter :  {'kernel': 'rbf', 'gamma': 0.01, 'C': 10}

svc = SVC( C =10, gamma=0.01, kernel ='rbf')
model = svc.fit(x_train, y_train)

y_pred = model.predict(x_test)
y_true = y_test

acc = accuracy_score(y_true, y_pred)
acc # 0.915492957746478

report = classification_report(y_test, y_pred)
print(report)
'''
              precision    recall  f1-score   support

         0.0       0.97      0.87      0.92        39
         1.0       0.86      0.97      0.91        32

    accuracy                           0.92        71
   macro avg       0.92      0.92      0.92        71
weighted avg       0.92      0.92      0.92        71
'''

pd.crosstab(y_pred, y_test)
'''
24hour_cond_loc1  0.0  1.0
row_0                     
0.0                34    1
1.0                 5   31
'''


##### 의사결정나무
x_col = col[1:6]
y_col = col[-1]

X=df_sam[x_col]
y=df_sam[y_col]

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size =0.3)

dtc = DecisionTreeClassifier(criterion='gini',random_state=123, max_depth=3)
model = dtc.fit(x_train, y_train)

names = list(x_col)
tree.plot_tree(model)
print(export_text(model, names))

y_pred = model.predict(x_test)
y_true = y_test

acc = accuracy_score(y_true, y_pred)
acc

con_mat = confusion_matrix(y_true, y_pred)
con_mat



from sklearn.tree import DecisionTreeClassifier, export_graphviz
export_graphviz(model, out_file='DT_tree_graph.dot', 
                feature_names=names, max_depth=3, class_names=True)

####################
## random forest
####################
rf = RandomForestClassifier()
model = rf.fit(X=x_train, y=y_train)

y_pred = model.predict(x_test)
y_true = y_test

acc = accuracy_score(y_true, y_pred)
acc

report = classification_report(y_true, y_pred)
print(report)


model.feature_importances_
# ([0.2363102 , 0.12479202, 0.36578993, 0.16562383, 0.10748402])

import matplotlib.pyplot as plt
plt.barh(names, model.feature_importances_ ) # (y,x)





## x변수 : ['plant1_train_hum_in_loc1', 'plant1_train_tem_coil_loc1']
col
x_col1=col[2:4] # ['plant1_train_hum_in_loc1', 'plant1_train_tem_coil_loc1']
X1=df_sam[x_col1]
y=df_sam[y_col]

x1_train, x1_test, y_train, y_test = train_test_split(X1, y, test_size =0.3, random_state=123)

xgb = XGBClassifier()
model = xgb.fit(x1_train, y_train)
model

y1_pred = model.predict(x1_test)

acc = accuracy_score(y_test, y1_pred)
acc

report = classification_report(y_test, y_pred)
print(report)

pd.crosstab(y1_pred, y_test)















