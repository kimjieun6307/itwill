# -*- coding: utf-8 -*-
"""
회귀방정식에서 기울기(slope)와 절편(intercept) 식
    기울기(slope) = Cov(x, y) / Sxx(x의 편차 제곱의 평균)
    절편(intercept) = y_mu - (slope * x_mu)
"""

from scipy import stats  # 회귀모델
import pandas as pd # 파일 읽기
import numpy as np


galton = pd.read_csv("galton.csv")
galton.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 928 entries, 0 to 927
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   child   928 non-null    float64  # -> y
 1   parent  928 non-null    float64  # -> x
 '''
# 변수 모두 숫자로 회쉬모형 독립변수 종속변수로 사용가능
 
# x, y변수 선택
x = galton.parent
y = galton.child

# model 생성
model = stats.linregress(x, y)
model
'''
LinregressResult(slope=0.6462905819936423, -->  기울기
intercept=23.941530180412748,  --> 절편
rvalue=0.4587623682928238, --> 설명력
pvalue=1.7325092920142867e-49,  --> <0.05 귀무가설 기각(영향을 미친다)
stderr=0.04113588223793335)
'''

# 회귀방정식 :  y= x * a + b
#>> a : 기울기(slope) = Cov(x, y) / Sxx(x의 편차 제곱의 평균)
#>> b : 절편(intercept) = y_mu - (slope * x_mu)

y_pred = x * model.slope + model.intercept
y_pred

y_true = y

# 예측치 vs 정답(관측치)
y_pred.mean()  # 68.08846982758534
y_true.mean()  # 68.08846982758512


# 1. 기울기(slope) 계산식 = Cov(x, y) / Sxx(x의 편차 제곱의 평균)
xm = x.mean()
ym = y.mean()
cov_xy = sum((x -xm)*(y-ym))/len(x)
cov_xy  # 2.062389686756837

Sxx = np.mean((x-xm)**2)
Sxx  # 3.1911182743757336

slope = cov_xy / Sxx
slope  # 0.6462905819936413



# 2. 절편(intercept) 계산식 = y_mu - (slope * x_mu)
intercept = ym - (slope * xm)
intercept  # 23.94153018041171


# 3. 설명력(rvalue)
# rvalue=0.4587623682928238
galton.corr() 
'''
           child    parent
child   1.000000  0.458762
parent  0.458762  1.000000
'''
# 설명력 = x와 y의 상관계수

y_pred1 = x * slope + intercept
y_pred1.mean()  #  68.08846982758423
# y_pred=x * model.slope + model.intercept
# y_pred.mean()  # 68.08846982758534


















