# -*- coding: utf-8 -*-
"""
행렬곱 함수(np.dot) 이용해서 y 예측치 구하기
    y_pred = np.dot(x, a) + b
"""

'''
cf) chap04_Numpy -> step04_axis_dot
※ np.dot(x, a) 전제조건 
    1) x, a : 행렬구조( x도 행렬, 기울기 a도 행렬 구조여야 함.)
    2) 수일치 :  x열 차수 = a행 차수( x :(2,2) -> a : (2,1) )
'''
from scipy import stats # 단순회귀모델
from statsmodels.formula.api import ols # 다중회귀모델
import pandas as pd
import numpy as np

# 1. data load
score = pd.read_csv("score_iq.csv")
score.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 6 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   sid      150 non-null    int64
 1   score    150 non-null    int64  #--> y
 2   iq       150 non-null    int64  #--> x1
 3   academy  150 non-null    int64  #--> x2
 4   game     150 non-null    int64
 5   tv       150 non-null    int64
'''
# 사용할 변수 : score(y), iq(x1), academy(x2)

formula = "score ~ iq + academy"
model = ols(formula, data = score).fit()

# 회귀계수 : 기울기, 절편
model.params
'''
Intercept    25.229141
iq            0.376966
academy       2.992800
'''

# model 결과 확인
model.summary()
'''
Adj. R-squared:                  0.946
F-statistic:                     1295.
Prob (F-statistic):           4.50e-94
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     25.2291      2.187     11.537      0.000      20.907      29.551
iq             0.3770      0.019     19.786      0.000       0.339       0.415
academy        2.9928      0.140     21.444      0.000       2.717       3.269
'''

# model 예측치
model.fittedvalues


# y_pred = np.dot(x, a) + b
x = score[['iq', 'academy']] 
x.shape  # (150, 2) 
'''
▶ np.dot(x, a) 전제조건 
    1. x, a : 행렬구조
    2. 수일치 :  x열 차수 = a행 차수

▶ model.params
Intercept    25.229141
iq            0.376966
academy       2.992800
'''
# error : a = np.array[[0.376966], [2.992800]] 
a = np.array([[0.376966], [2.992800]])
a.shape # (2, 1)
    
matmul = np.dot(x, a)  # 행렬곱
matmul.shape  # (150, 1)

b=25.229141 # 절편
y_pred = matmul + b # boardcast(2차원 + 0차원) : 서로 다른 차원의 연산
y_pred.shape  # (150, 1)

# 2차원(150,1) -> 1차원(150) : reshape
y_pred1 = y_pred.reshape(150)
y_pred1.shape  # (150, )

y_true = score['score']
y_true.shape  #(150, )

df = pd.DataFrame({'y_true' : y_true, 'y_pred' : y_pred1})
df.head()
'''
   y_true     y_pred
0      90  83.989981
1      75  75.342691
2      77  73.457861
3      83  82.105151
4      65  64.810571
'''

df.tail()
'''
     y_true     y_pred
145      83  82.105151
146      65  64.810571
147      80  80.574359
148      65  64.810571
149      83  82.105151
'''

cor = df['y_true'].corr(df['y_pred'])
cor  # 0.9727792069594754

















