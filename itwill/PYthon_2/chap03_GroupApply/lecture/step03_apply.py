# -*- coding: utf-8 -*-
"""
1. group 객체에 외부 함수 적용
 - object.apply(func1)
 - object.agg([func1, func2, ...]) : 여러개 함수를 객체에 apply

2. data 정규화
"""

import pandas as pd

# 1. group 객체에 외부 함수 적용
'''
apply vs agg
 - 공통점 : 그룹객체, pandas_DaraFrame 객체에 외부 함수 적용
 - 차이점 : 적용할 함수에 개수
'''

# apply()
test = pd.read_csv("test.csv")
test.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   key     6 non-null      object
 1   data1   6 non-null      int64 
 2   data2   6 non-null      int64 
'''
grp = test['data2'].groupby(test['key'])
grp.size()
grp.sum()
grp.min()
grp.max()

# 사용자 정의 함수
def diff(grp) :
    result = grp.max() - grp.min()
    return result

# 그룹객체 내장함수 적용 : grp.apply(내장함수)
grp.apply(sum)
'''
a    300
b    500
'''
grp.apply(max)
'''
a    100
b    200
'''
grp.apply(min)
'''
a    100
b    100
'''

# 사용자함수 적용
grp.apply(diff)
'''
a      0
b    100
'''

# agg([func1, func2, ... ])
agg_func = grp.agg(['sum', 'max', 'min', diff])
'''
     sum  max  min  diff
key                     
a    300  100  100     0
b    500  200  100   100
'''

# 2. data 정규화 
# - 다양한 특징을 갖는 변수(독립변수, x)를 대상으로 일정한 범위(ex. 0~1)로 조정
# - x(30) -> y

import numpy as np # max, min, log

# 1) 사용자 함수 : 0~1
def normal(x) : 
    n = (x - np.min(x)) / (np.max(x)- np.min(x))
    return n

x=[10, 20000, -100, 0]
normal(x)
 # [0.00547264, 1.        , 0.        , 0.00497512]

# 2) 자연 log함수
np.log(x) # 밑수e : 음수, 영 -> 결측치, 무한대
# [2.30258509, 9.90348755,        nan,       -inf])


e = np.exp(1)
e # 2.718281828459045

# 로그 -> 지수값(8 = 2^3)
np.log(10) # 밑수 e : 2.302585092994046 = e^2.3025
e**2.3025 # 9.999149106262605

# 지수 -> 로그값
np.exp(2.302585092994046) # 10.000000000000002

'''
로그 vs 지수 역함수 관계
 - 로그 : 지수값 반환
 - 지수 : 로그값 반환
'''

iris = pd.read_csv("iris.csv")
iris.info()
# 전체 칼럼명 가져오기
cols = list(iris.columns)
cols #  ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']

iris_x = iris[cols[:4]]
iris_x.shape # (150, 4)
iris_x.head()

# x변수 정규화
iris_x_nor = iris_x.apply(normal)
iris_x_nor.head()
'''   Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
0      0.222222     0.625000      0.067797     0.041667
1      0.166667     0.416667      0.067797     0.041667
2      0.111111     0.500000      0.050847     0.041667
3      0.083333     0.458333      0.084746     0.041667
4      0.194444     0.666667      0.067797     0.041667
'''

iris_x.agg(['var', 'mean', 'max', 'min'])















