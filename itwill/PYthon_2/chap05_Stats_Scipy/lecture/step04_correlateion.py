# -*- coding: utf-8 -*-
"""
공분산 vs 상관계수(correlation)
 - 공통점 : 변수간의 상관성 분석
 
1. 공분산 : 두 확률변수 간의 분산(평균에서 퍼진 정도)을 나타내는 통계
  - 두 확률변수 : X,Y -> X표본평균(ux), Y표본평균(uy)
      Cov(X, Y) = sum((X-ux) * (Y-uy)) / n
      Cov(X, Y) > 0 : X증가 -> Y증가
      Cov(X, Y) > 0 : X증가 -> Y감소
      Cov(X, Y) = 0 : 두 변수는 선형관계가 아님
      문제점 : 값이 큰 변수의 영향을 많이 받음.

2. 상관계수 : 공분산을 각각의 표준편차로 나누어서 정규화한 통계
    - 부호는 공분산과 동일하고, 차이점은 절대값 1을 넘지 않음(-1 ~ +1)
      Cor(X, Y) = Cov(X, Y) / std(X) * std(Y)
"""
import numpy as np
import pandas as pd

score_iq = pd.read_csv("score_iq.csv")
score_iq.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 6 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   sid      150 non-null    int64
 1   score    150 non-null    int64
 2   iq       150 non-null    int64
 3   academy  150 non-null    int64
 4   game     150 non-null    int64
 5   tv       150 non-null    int64
 '''


cor = score_iq.corr()
cor # 상관계수 행렬
'''
              sid     score        iq   academy      game        tv
sid      1.000000 -0.014399 -0.007048 -0.004398  0.018806  0.024565
score   -0.014399  1.000000  0.882220  0.896265 -0.298193 -0.819752
iq      -0.007048  0.882220  1.000000  0.671783 -0.031516 -0.585033
academy -0.004398  0.896265  0.671783  1.000000 -0.351315 -0.948551
game     0.018806 -0.298193 -0.031516 -0.351315  1.000000  0.239217
tv       0.024565 -0.819752 -0.585033 -0.948551  0.239217  1.000000
'''
# score 기준으로 상관계수가 가장 높은 것 : academy (0.896265)
# score 기준으로 부정적 관계 tv(-0.819752) 가 가장 높은

'''
1. 공분산
 - score vs iq
 - score vs academy
 
Cov(X, Y) = sum((X-ux) * (Y-uy)) / n
'''

x = score_iq['score']
y1 = score_iq['iq']
y2 = score_iq['academy']
 
def Cov(x, y):
    ux = x.mean()
    uy = y.mean()
    cov_re = sum((x-ux) * (y-uy)) / len(x)
    return cov_re


cov1 = Cov(x, y1) # score vs iq 공분산
cov2 = Cov(x, y2) # score vs academy 공분산
print(cov1, cov2)
# 50.99528888888886 7.072444444444438 ==> 값의 큰 차이가 남.

score_iq.head() # iq는 100단위이고, academy는 1단위 여서 공분산의 값이 차이가 남.
'''
     sid  score   iq  academy  game  tv
0  10001     90  140        2     1   0
1  10002     75  125        1     3   3
2  10003     77  120        1     0   4
3  10004     83  135        2     3   2
4  10005     65  105        0     4   4
'''

score_iq.cov()
'''
                 sid      score         iq   academy      game        tv
sid      1887.500000  -4.100671  -2.718121 -0.231544  1.208054  1.432886
score      -4.100671  42.968412  51.337539  7.119911 -2.890201 -7.214586
iq         -2.718121  51.337539  78.807338  7.227293 -0.413691 -6.972975
academy    -0.231544   7.119911   7.227293  1.468680 -0.629530 -1.543400
game        1.208054  -2.890201  -0.413691 -0.629530  2.186309  0.474899
tv          1.432886  -7.214586  -6.972975 -1.543400  0.474899  1.802640
'''

score_iq['score'].cov(score_iq['academy'])
# 7.11991051454138
score_iq['score'].cov(score_iq['iq'])
# 51.33753914988811



'''
2. 상관계수
Cor(X, Y) = Cov(X, Y) / std(X) * std(Y)
'''
def Cor(x, y):
    cov = Cov(x, y)
    std_x = x.std()
    std_y = y.std()
    cor_re = cov / (std_x * std_y)
    return cor_re

cor1 = Cor(x, y1)  # score vs iq 상관계수
cor2 = Cor(x, y2)  # score vs academy 상관계수
print(cor1, cor2)
# 0.8763388756493802 0.8902895813918037
# 값에 대한 편차에 상관없음(표준편차로 나눠서 정규화 되었음)

score_iq.corr()
'''
              sid     score        iq   academy      game        tv
sid      1.000000 -0.014399 -0.007048 -0.004398  0.018806  0.024565
score   -0.014399  1.000000  0.882220  0.896265 -0.298193 -0.819752
iq      -0.007048  0.882220  1.000000  0.671783 -0.031516 -0.585033
academy -0.004398  0.896265  0.671783  1.000000 -0.351315 -0.948551
game     0.018806 -0.298193 -0.031516 -0.351315  1.000000  0.239217
tv       0.024565 -0.819752 -0.585033 -0.948551  0.239217  1.000000
'''

score_iq['score'].corr(score_iq['academy'])
# 0.8962646792534938

