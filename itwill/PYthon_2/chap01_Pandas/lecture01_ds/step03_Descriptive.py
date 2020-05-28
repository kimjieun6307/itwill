# -*- coding: utf-8 -*-
"""
Descriptive 
: 기술통계(요약통계)
"""

'''
- DataFrame의 요약통계량
- 상관계수
'''

import pandas as pd

product = pd.read_csv("C:/ITWILL/4_Python-II/data/product.csv")
product.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 264 entries, 0 to 263
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   a       264 non-null    int64
 1   b       264 non-null    int64
 2   c       264 non-null    int64
 '''
product.head()
product.tail()
 
 # 요약통계량
summary = product.describe() # R에서 summary와 비슷
summary
'''
                a           b           c
count  264.000000  264.000000  264.000000
mean     2.928030    3.132576    3.094697
std      0.970345    0.859657    0.828744
min      1.000000    1.000000    1.000000
25%      2.000000    3.000000    3.000000
50%      3.000000    3.000000    3.000000
75%      4.000000    4.000000    4.000000
max      5.000000    5.000000    5.000000
'''

# 행/열 통계(sum, mean, var, std ..)
product.sum(axis = 0) # 행축
'''
a    773
b    827
c    817
'''
product.sum(axis = 1) # 열축

# 산포도 : 분산, 표준편차
product.var() # axis = 0
''' 
a    0.941569
b    0.739011
c    0.686816
'''
product.std()
'''
a    0.970345
b    0.859657
c    0.828744
'''

# 빈도수(value_counts) : 집단변수
a_cnt = product['a'].value_counts()
a_cnt
''' # (자동으로 내림차순 정렬)
3    126
4     64
2     37
1     30
5      7
'''

b_cnt = product['b'].value_counts()
b_cnt
'''
3    119
4     79
2     48
5     10
1      8
'''

# 유일값(unique) 보기 : 중복되지 않은 값
print(product['c'].unique()) # [3 2 4 5 1]

# 상관관계 (corr)
product.corr() #상관계수 정방행렬
'''
          a         b         c
a  1.000000  0.499209  0.467145
b  0.499209  1.000000  0.766853
c  0.467145  0.766853  1.000000
'''
'''
>>> b변수와 c변수 상관성이 가장 높다. (0.7이상이면 높은 상관관계)
>>> a변수와 c변수 상관성이 가장 낮다. (0.3이하면 상관관계 없다.)
'''

# iris dataset 적용
iris = pd.read_csv("iris.csv") # 절대경로 설정 되어있으면 바로 파일명만 써서 가져올수 있음.
iris.info()

# subset 생성
iris_df = iris.iloc[:,:4]
iris_df.shape # (150, 4)

# 변수 4개 요약통계량
iris_df.describe()
'''
       Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.057333      3.758000     1.199333
std        0.828066     0.435866      1.765298     0.762238
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000
'''

# 상관계수 행렬
iris_df.corr()
'''
              Sepal.Length  Sepal.Width  Petal.Length  Petal.Width
Sepal.Length      1.000000    -0.117570      0.871754     0.817941
Sepal.Width      -0.117570     1.000000     -0.428440    -0.366126
Petal.Length      0.871754    -0.428440      1.000000     0.962865
Petal.Width       0.817941    -0.366126      0.962865     1.000000
'''

# 집단변수
species = iris.Species
species.value_counts()
'''
setosa        50
virginica     50
versicolor    50
'''
species.unique()
#array(['setosa', 'versicolor', 'virginica'], dtype=object)

list(species.unique())
#['setosa', 'versicolor', 'virginica']

















