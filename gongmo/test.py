# -*- coding: utf-8 -*-
"""
Created on Tue May 19 18:16:14 2020

@author: user
"""

import pandas as pd
plant1_train = pd.read_csv("plant1_train.csv")
plant2_train = pd.read_csv("plant2_train.csv")

plant1_train.info()


plant1_train = plant1_train.drop('Unnamed: 0' , axis=1)
cols = ['Date' , 'loc1_tem', 'loc1_hum', 'loc1_coil_temp','loc2_tem', 'loc2_hum', 'loc2_coil_temp' , 'loc3_tem', 'loc3_hum', 'loc3_coil_temp', 'out_tem', 'out_hum', 'loc1' , 'loc2' , 'loc3']
plant1_train.columns = cols

plant1_train_first = plant1_train[['Date','loc1_tem', 'out_tem' , 'loc1_coil_temp','loc1_hum' ,'loc1']]
plant1_train_first["Hour"] = pd.to_datetime(plant1_train_first["Date"])
plant1_train_first["Hour"] = plant1_train_first["Hour"].apply(lambda x: x.hour)
tmp = []
for i in plant1_train_first["Hour"]:
  if 0<=i<6:
    tmp.append(1)
  elif 6<=i<12:
    tmp.append(2)
  elif 12<= i < 18:
    tmp.append(3)
  else:
    tmp.append(4)
plant1_train_first["Hour_label"] = tmp
plant1_train_first



plant1_train_second = plant1_train[['Date','loc2_tem', 'out_tem' , 'loc2_coil_temp','loc2_hum' ,'loc2']]
plant1_train_second["Hour"] = pd.to_datetime(plant1_train_second["Date"])
plant1_train_second["Hour"] = plant1_train_second["Hour"].apply(lambda x: x.hour)
tmp = []
for i in plant1_train_second["Hour"]:
  if 0<=i<6:
    tmp.append(1)
  elif 6<=i<12:
    tmp.append(2)
  elif 12<= i < 18:
    tmp.append(3)
  else:
    tmp.append(4)
plant1_train_second["Hour_label"] = tmp
plant1_train_second


# plant1_train_first
plant1_train_first.info()


p1_yes = plant1_train_first[plant1_train_first.loc1==1]
p1_yes.info()
''' #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   Date            275 non-null    object 
 1   loc1_tem        275 non-null    float64
 2   out_tem         275 non-null    float64
 3   loc1_coil_temp  275 non-null    float64
 4   loc1_hum        275 non-null    float64
 5   loc1            275 non-null    float64
 6   Hour            275 non-null    int64  
 7   Hour_label      275 non-null    int64  
dtypes: float64(5), int64(2), object(1)
'''



p1_yes.to_csv("./p1_yes.csv", index=None, encoding='utf-8')
p1_yes.describe()

p1_yes['diff_coil_temp'] = p1_yes['loc1_tem'] - p1_yes['loc1_coil_temp']
p1_yes['diff_temp'] = p1_yes['loc1_tem'] - p1_yes['out_tem']



p1_no = plant1_train_first[plant1_train_first.loc1==0]
p1_no.info()

p1_no.describe()
'''           loc1_tem       out_tem  ...          Hour    Hour_label
count  57604.000000  57604.000000  ...  57604.000000  57604.000000
mean      17.480594     13.523524  ...     11.456010      2.499010
std        9.884937     10.834775  ...      6.920483      1.118012
min       -7.980000    -13.690000  ...      0.000000      1.000000
25%        8.630000      4.140000  ...      5.000000      1.000000
50%       16.930000     13.000000  ...     11.000000      2.000000
75%       26.360000     23.000000  ...     17.000000      3.000000
max       37.080000     38.570000  ...     23.000000      4.000000
'''



# -*- coding: utf-8 -*-
"""
1일 후 결과값 가져오기
from datetime import datetime , timedelta
datetime.strptime()
"""

import pandas as pd
from datetime import datetime , timedelta
plant1_train = pd.read_csv('plant1_train.csv')
plant2_train = pd.read_csv("plant2_train.csv")

plant1_train = plant1_train.drop('Unnamed: 0' , axis=1)
cols = ['Date' , 'loc1_tem', 'loc1_hum', 'loc1_coil_temp','loc2_tem', 'loc2_hum', 'loc2_coil_temp' , 'loc3_tem', 'loc3_hum', 'loc3_coil_temp', 'out_tem', 'out_hum', 'loc1' , 'loc2' , 'loc3']
plant1_train.columns = cols
plant1_train_first = plant1_train[['Date','loc1_tem', 'out_tem' , 'loc1_coil_temp','loc1_hum' ,'out_hum','loc1']]

a = datetime.strptime(plant1_train_first['Date'][0]  , '%Y-%m-%d %H:%M')

date_trans = []
for i in range(0,len(plant1_train_first)):
    date_trans.append(datetime.strptime(plant1_train_first['Date'][i] , '%Y-%m-%d %H:%M'))

type(date_trans)
date_trans[-10:]



plant1_train_first['date_trans'] = date_trans
#plant1_train_first[plant1_train_first['date_trans']==c]
plant1_train_first

hour24 = []
for i in range(0,len(plant1_train_first)):
    tmp = datetime.strptime(plant1_train_first['Date'][i]  , '%Y-%m-%d %H:%M') + timedelta(days=1)
    tmp1 = datetime.strptime(plant1_train_first['Date'][i]  , '%Y-%m-%d %H:%M')
    if(len(plant1_train_first[plant1_train_first['date_trans']==tmp]) > 0 ):
        loc_24hour = plant1_train_first[plant1_train_first['date_trans']==tmp]
        print(plant1_train_first['Date'][i])
        print(loc_24hour['Date'])
        print("this", float(loc_24hour['loc1'].values))
        print("-"*10)
        hour24.append(float(loc_24hour['loc1'].values))
    else:
        hour24.append(float('NaN'))

plant1_train_first['24hourloc'] = hour24
plant1_train_first

plant1_train_first_24 = plant1_train_first.dropna(axis=0)
plant1_train_first_24[plant1_train_first_24['24hourloc']==1]


plant1_train_first_24.info()
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 57400 entries, 0 to 58604
Data columns (total 9 columns):
 #   Column          Non-Null Count  Dtype         
---  ------          --------------  -----         
 0   Date            57400 non-null  object        
 1   loc1_tem        57400 non-null  float64       
 2   out_tem         57400 non-null  float64       
 3   loc1_coil_temp  57400 non-null  float64       
 4   loc1_hum        57400 non-null  float64       
 5   out_hum         57400 non-null  float64       
 6   loc1            57400 non-null  float64       
 7   date_trans      57400 non-null  datetime64[ns]
 8   24hourloc       57400 non-null  float64       
 '''
 

plant1_train_first_24['24hourloc'].value_counts()
'''
0.0    57133
1.0      267
'''

57133+267 #57400
(267/57400)*100 #  0.465%



plant1_train_first_24.to_csv('plant1_train_first_24.csv')


######## 언더 샘플링(0.5) ############
df_no = plant1_train_first_24[plant1_train_first_24['24hourloc']==0]
df_yes = plant1_train_first_24[plant1_train_first_24['24hourloc']==1]

df_no.shape # (57133, 9)
df_yes.shape #  (267, 9)

57133/2 # 28566.5


df_no_sam = df_no.sample(28566)
df_no_sam.shape # (28566, 9)

df_sam = pd.concat([df_no_sam, df_yes])
df_sam.info()
df_sam.head()


df_sam.columns
'''
['Date', 'loc1_tem', 'out_tem', 'loc1_coil_temp', 'loc1_hum', 'out_hum',
       'loc1', 'date_trans', '24hourloc']
'''

col = df_sam.columns
x_col = col[1:6]
y_col = col[-1]

X=df_sam[x_col]
y=df_sam[y_col]



##################################
### 불균형 데이터 처리 SMOTE 함수
##################################
# pip install -U imbalanced-learn # Anaconda Promt에서 설치

from imblearn.over_sampling import SMOTE


## auto##
sm = SMOTE(k_neighbors=5, random_state=71)
X_data, y_data = sm.fit_sample(X, y)


X_data.shape # (57132, 5)
y_data.shape # (57132,)

y_data.value_counts()
'''
1.0    28566
0.0    28566
'''


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


x_train, x_test, y_train, y_test = train_test_split(X_data, y_data, test_size =0.3)

xgb = XGBClassifier(random_state=123)

model_xgb = xgb.fit(x_train, y_train)
y_pred = model_xgb.predict(x_test)

acc = accuracy_score(y_test, y_pred)
acc 

report = classification_report(y_test, y_pred)
print(report)
'''
              precision    recall  f1-score   support

         0.0       1.00      0.98      0.99      5621
         1.0       0.98      1.00      0.99      5599

    accuracy                           0.99     11220
   macro avg       0.99      0.99      0.99     11220
weighted avg       0.99      0.99      0.99     11220
'''

##################################
plant1_train = pd.read_csv('plant1_train.csv')


plant1_train = plant1_train.drop('Unnamed: 0' , axis=1)
cols = ['Date' , 'loc1_tem', 'loc1_hum', 'loc1_coil_temp','loc2_tem', 'loc2_hum', 'loc2_coil_temp' , 'loc3_tem', 'loc3_hum', 'loc3_coil_temp', 'out_tem', 'out_hum', 'loc1' , 'loc2' , 'loc3']
plant1_train.columns = cols
plant1_train_2 = plant1_train[['Date','loc2_tem', 'out_tem' , 'loc2_coil_temp', 'loc2_hum' ,'out_hum','loc2']]

a = datetime.strptime(plant1_train_2['Date'][0]  , '%Y-%m-%d %H:%M')

date_trans = []
for i in range(0,len(plant1_train_2)):
    date_trans.append(datetime.strptime(plant1_train_2['Date'][i] , '%Y-%m-%d %H:%M'))

type(date_trans)
date_trans[-10:]



plant1_train_2['date_trans'] = date_trans
#plant1_train_first[plant1_train_first['date_trans']==c]
plant1_train_2

hour24 = []
for i in range(0,len(plant1_train_2)):
    tmp = datetime.strptime(plant1_train_2['Date'][i]  , '%Y-%m-%d %H:%M') + timedelta(days=1)
    tmp1 = datetime.strptime(plant1_train_2['Date'][i]  , '%Y-%m-%d %H:%M')
    if(len(plant1_train_2[plant1_train_2['date_trans']==tmp]) > 0 ):
        loc_24hour = plant1_train_2[plant1_train_2['date_trans']==tmp]
        print(plant1_train_2['Date'][i])
        print(loc_24hour['Date'])
        print("this", float(loc_24hour['loc2'].values))
        print("-"*10)
        hour24.append(float(loc_24hour['loc2'].values))
    else:
        hour24.append(float('NaN'))

plant1_train_2['24hourloc'] = hour24
plant1_train_2

plant1_train_2 = plant1_train_2.dropna(axis=0)
plant1_train_2[plant1_train_2['24hourloc']==1]


plant1_train_2.info()
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 58157 entries, 0 to 58604
Data columns (total 9 columns):
 #   Column          Non-Null Count  Dtype         
---  ------          --------------  -----         
 0   Date            58157 non-null  object        
 1   loc2_tem        58157 non-null  float64       
 2   out_tem         58157 non-null  float64       
 3   loc2_coil_temp  58157 non-null  float64       
 4   loc2_hum        58157 non-null  float64       
 5   out_hum         58157 non-null  float64       
 6   loc2            58157 non-null  float64       
 7   date_trans      58157 non-null  datetime64[ns]
 8   24hourloc       58157 non-null  float64    
 '''
 

plant1_train_2['24hourloc'].value_counts()
'''
0.0    57678
1.0      479
'''

57678+479 #58157
(479/58157)*100 #  0.823%


plant1_train_2.to_csv('plant1_train_2.csv')

plant1_train_2.columns = ['Date', 'loc1_tem', 'out_tem', 'loc1_coil_temp', 'loc1_hum', 'out_hum', 'loc1', 'date_trans', '24hourloc']


X=plant1_train_2[x_col]
y=plant1_train_2[y_col]

y_pred2 = model_xgb.predict(X)

acc = accuracy_score(y, y_pred2)
acc 

report = classification_report(y, y_pred2)
print(report)
'''
              precision    recall  f1-score   support

         0.0       1.00      0.98      0.99     57678
         1.0       0.16      0.49      0.24       479

    accuracy                           0.98     58157
   macro avg       0.58      0.73      0.62     58157
weighted avg       0.99      0.98      0.98     58157
'''

############################################

plant1_train = pd.read_csv('plant1_train.csv')


plant1_train = plant1_train.drop('Unnamed: 0' , axis=1)
cols = ['Date' , 'loc1_tem', 'loc1_hum', 'loc1_coil_temp','loc2_tem', 'loc2_hum', 'loc2_coil_temp' , 'loc3_tem', 'loc3_hum', 'loc3_coil_temp', 'out_tem', 'out_hum', 'loc1' , 'loc2' , 'loc3']
plant1_train.columns = cols
plant1_train_3 = plant1_train[['Date','loc3_tem', 'out_tem' , 'loc3_coil_temp', 'loc3_hum', 'out_hum', 'loc3']]

a = datetime.strptime(plant1_train_3['Date'][0]  , '%Y-%m-%d %H:%M')

date_trans = []
for i in range(0,len(plant1_train_3)):
    date_trans.append(datetime.strptime(plant1_train_3['Date'][i] , '%Y-%m-%d %H:%M'))


plant1_train_3['date_trans'] = date_trans
#plant1_train_first[plant1_train_first['date_trans']==c]
plant1_train_3

hour24 = []
for i in range(0,len(plant1_train_3)):
    tmp = datetime.strptime(plant1_train_3['Date'][i]  , '%Y-%m-%d %H:%M') + timedelta(days=1)
    tmp1 = datetime.strptime(plant1_train_3['Date'][i]  , '%Y-%m-%d %H:%M')
    if(len(plant1_train_3[plant1_train_3['date_trans']==tmp]) > 0 ):
        loc_24hour = plant1_train_3[plant1_train_3['date_trans']==tmp]
        print(plant1_train_3['Date'][i])
        print(loc_24hour['Date'])
        print("this", float(loc_24hour['loc3'].values))
        print("-"*10)
        hour24.append(float(loc_24hour['loc3'].values))
    else:
        hour24.append(float('NaN'))

plant1_train_3['24hourloc'] = hour24
plant1_train_3

plant1_train_3 = plant1_train_3.dropna(axis=0)
plant1_train_3[plant1_train_3['24hourloc']==1]


plant1_train_3.info()
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 58108 entries, 0 to 58604
Data columns (total 9 columns):
 #   Column          Non-Null Count  Dtype         
---  ------          --------------  -----         
 0   Date            58108 non-null  object        
 1   loc3_tem        58108 non-null  float64       
 2   out_tem         58108 non-null  float64       
 3   loc3_coil_temp  58108 non-null  float64       
 4   loc3_hum        58108 non-null  float64       
 5   out_hum         58108 non-null  float64       
 6   loc3            58108 non-null  float64       
 7   date_trans      58108 non-null  datetime64[ns]
 8   24hourloc       58108 non-null  float64    
 '''
 

plant1_train_3['24hourloc'].value_counts()
'''
0.0    57471
1.0      637
'''

57471+637 #58108
(637/58108)*100 #  1.096%


plant1_train_3.columns = ['Date', 'loc_tem', 'out_tem', 'loc_coil_temp', 'loc_hum', 'out_hum', 'loc', 'date_trans', '24hourloc']

plant1_train_3.to_csv('plant1_train_3.csv')


plant1_train_2=pd.read_csv('plant1_train_2.csv')
plant1_train_2.info()
plant1_train_2 = plant1_train_2.iloc[:, 1:10]
plant1_train_2.columns = ['Date', 'loc_tem', 'out_tem', 'loc_coil_temp', 'loc_hum', 'out_hum', 'loc', 'date_trans', '24hourloc']

plant1_train_1 = pd.read_csv('plant1_train_first_24.csv')
plant1_train_1.info()
plant1_train_1= plant1_train_1.iloc[:, 1:10]
plant1_train_1.columns = ['Date', 'loc_tem', 'out_tem', 'loc_coil_temp', 'loc_hum', 'out_hum', 'loc', 'date_trans', '24hourloc']

df_plant1_24 = pd.concat([plant1_train_1, plant1_train_2])
df_plant1_24 = pd.concat([df_plant1_24, plant1_train_3])

df_plant1_24.info()
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 173665 entries, 0 to 58604
Data columns (total 9 columns):
 #   Column         Non-Null Count   Dtype  
---  ------         --------------   -----  
 0   Date           173665 non-null  object 
 1   loc_tem        173665 non-null  float64
 2   out_tem        173665 non-null  float64
 3   loc_coil_temp  173665 non-null  float64
 4   loc_hum        173665 non-null  float64
 5   out_hum        173665 non-null  float64
 6   loc            173665 non-null  float64
 7   date_trans     173665 non-null  object 
 8   24hourloc      173665 non-null  float64
'''

57400+58157+58108 # 173665
267+479+637 # 1383

(1383/173665)*100 # 0.796%


df_plant1_24.to_csv('df_plant1_24.csv')


######## 언더 샘플링(0.5) ############
df_no = df_plant1_24[df_plant1_24['24hourloc']==0]
df_yes = df_plant1_24[df_plant1_24['24hourloc']==1]

df_no.shape # (172282, 9)
df_yes.shape #  (1383, 9)

172282/2 # 86141


df_no_sam = df_no.sample(86141)
df_no_sam.shape # (86141, 9)

df_sam = pd.concat([df_no_sam, df_yes])

col = df_sam.columns
x_col = col[1:6]
y_col = col[-1]

X=df_sam[x_col]
y=df_sam[y_col]

### 불균형 데이터 처리 SMOTE 함수 #####

from imblearn.over_sampling import SMOTE


## auto##
sm = SMOTE(k_neighbors=5, random_state=123)
X_data, y_data = sm.fit_sample(X, y)


X_data.shape # (172282, 5)
y_data.shape # (172282,)

y_data.value_counts()
'''
1.0    86141
0.0    86141
'''

x_train, x_test, y_train, y_test = train_test_split(X_data, y_data, test_size =0.3)

xgb = XGBClassifier(random_state=123)

model_xgb = xgb.fit(x_train, y_train)
y_pred = model_xgb.predict(x_test)

acc = accuracy_score(y_test, y_pred)
acc 

report = classification_report(y_test, y_pred)
print(report)


# plant1_train_3
plant1_train_3.columns

X3=plant1_train_3[x_col]
y3=plant1_train_3[y_col]

y3_pred = model_xgb.predict(X3)
report3 = classification_report(y3, y3_pred)
print(report3)
'''
              precision    recall  f1-score   support

         0.0       1.00      0.96      0.98     57471
         1.0       0.23      0.98      0.37       637

    accuracy                           0.96     58108
   macro avg       0.62      0.97      0.68     58108
weighted avg       0.99      0.96      0.97     58108
'''

#######################

X=df_plant1_24[x_col]
y=df_plant1_24[y_col]

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size =0.3)


xgb2 = XGBClassifier(random_state=45)

model_xgb2 = xgb2.fit(x_train, y_train)
y_pred = model_xgb2.predict(x_test)

acc = accuracy_score(y_test, y_pred)
acc 

report = classification_report(y_test, y_pred)
print(report)
'''
              precision    recall  f1-score   support

         0.0       1.00      1.00      1.00     51721
         1.0       0.87      0.50      0.63       379

    accuracy                           1.00     52100
   macro avg       0.93      0.75      0.82     52100
weighted avg       1.00      1.00      1.00     52100
'''


y3_pred = model_xgb2.predict(X3)
report3 = classification_report(y3, y3_pred)
print(report3)
'''
              precision    recall  f1-score   support

         0.0       1.00      1.00      1.00     57471
         1.0       0.96      0.64      0.76       637

    accuracy                           1.00     58108
   macro avg       0.98      0.82      0.88     58108
weighted avg       1.00      1.00      1.00     58108
'''
#####################
# 중복된 행 제거
df_p1=df_plant1_24.drop_duplicates()
df_p1.info()
# Int64Index: 173659 entries, 0 to 58604

df_plant1_24.info()
#Int64Index: 173665 entries, 0 to 58604

173665-173659 # 6

df_p1['24hourloc'].value_counts()
'''
0.0    172276
1.0      1383
'''
df_x = df_p1[['loc_coil_temp', 'loc_hum']]
df_y = df_p1[['24hourloc']]


x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size =0.3)


xgb3 = XGBClassifier(random_state=123)

model_xgb3 = xgb3.fit(x_train, y_train)
y_pred = model_xgb3.predict(x_test)

report = classification_report(y_test, y_pred)
print(report)
'''
              precision    recall  f1-score   support

         0.0       0.99      1.00      1.00     51679
         1.0       0.65      0.06      0.11       419

    accuracy                           0.99     52098
   macro avg       0.82      0.53      0.55     52098
weighted avg       0.99      0.99      0.99     52098
'''
 
########
sm = SMOTE(k_neighbors=5, random_state=123)
X_data, y_data = sm.fit_sample(df_x, df_y)

x_train, x_test, y_train, y_test = train_test_split(X_data, y_data, test_size =0.3)


xgb3 = XGBClassifier(random_state=123)

model_xgb3 = xgb3.fit(x_train, y_train)
y_pred = model_xgb3.predict(x_test)

report = classification_report(y_test, y_pred)
print(report)
'''
              precision    recall  f1-score   support

         0.0       0.95      0.90      0.93     51773
         1.0       0.90      0.96      0.93     51593

    accuracy                           0.93    103366
   macro avg       0.93      0.93      0.93    103366
weighted avg       0.93      0.93      0.93    103366
'''

# plant1_train_3

X3=plant1_train_3[['loc_coil_temp', 'loc_hum']]
y3=plant1_train_3['24hourloc']

y3_pred = model_xgb3.predict(X3)
report3 = classification_report(y3, y3_pred)
print(report3)
'''
              precision    recall  f1-score   support

         0.0       1.00      0.88      0.94     57471
         1.0       0.07      0.83      0.13       637

    accuracy                           0.88     58108
   macro avg       0.54      0.86      0.54     58108
weighted avg       0.99      0.88      0.93     58108
'''

