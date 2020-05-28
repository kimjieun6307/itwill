# -*- coding: utf-8 -*-
"""
data scaling (normalize, standardize)
- 특정 variable value 따라 model에 영향을 미치는 경우
ex) 범죄율 (0.1~0.99) 주택 가격 (99~999)

- 정규화(normalize) : 변수의 값을 일정한 범위로(0~1 / -1~1) -> x변수
    정규화 공식 nor = (x - min) / (max - min)
- 표준화 : 평균 =0과 표준편차 = 1를 이용(Y변수)
    표준화 공식 z= (x-mean) / std
"""

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression # model object
from sklearn.model_selection import train_test_split # train/test split
from sklearn.metrics import mean_squared_error, r2_score # model 평가


import numpy as np


# 1. dataset load
X, y = load_boston(return_X_y=True)
X.shape # (506, 13)
y.shape # (506,)


# 2. data scaling
'''
X : 정규화 (0~1)
Y : 표준화 (평균 = 0, 표준편차 = 1)
'''
X.max() # 711.0
X.mean() # 70.0739670446944
y.max() # 50.0
y.mean() # 22.53280632411

# 정규화 함수 생성
def normal(x) :
    nor = (x - np.min(x)) / (np.max(x) - np.min(x))
    return nor

# 표준화 함수 생성
def zscore(y) :
    mu = y.mean()
    z = (y-mu) / y.std()
    return z

# X변수 정규화
x_nor = normal(X)
x_nor.mean() #  0.09855691567467571

# y변수 표준화 (평균 = 0, 표준편차 =1)
y_zsc = zscore(y)
y_zsc.mean() # -5.195668225913776e-16 -> 평균은 0에 수렴
y_zsc.std() # 0.9999999999999999 -> 표준편차는 1에 수렴


# 3. dataset split
x_train, x_test, y_train, y_test = train_test_split(x_nor, y_zsc, random_state =123) # test_size = 0.25 기본값

x_train.shape # (379, 13)
506*0.75 # 379.5
x_test.shape


# 4. 모델생성
lr = LinearRegression()
model = lr.fit(x_train, y_train)
model


# 5. 모델 평가
y_pred = model.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
mse #  0.2933980240643525 (오류율 : 30%)

rscore = r2_score(y_test, y_pred)
rscore # 0.68624488572957 (정확률 : 70%)




































