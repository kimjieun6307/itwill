# -*- coding: utf-8 -*-
"""
merge : 공통 칼럼을 가지고 dataframe 병합/join
"""
'''
DataFrame 병합(merge)
 ex) DF1(id) + DF2(id) -> DF3
'''
import pandas as pd
from pandas import Series, DataFrame

# 1. Seroes marge : 1차원 (rbind, cbind)
s1 = Series([1,3], index = ['a','b'])
s2 = Series([5,6,7], index = ['a','b','c'])
s3 = Series([11,13], index = ['a','b'])

# 행 단위 결합(axis = 0) :  rbind
s4 = pd.concat([s1, s2, s3], axis = 0)
s4
'''
a     1
b     3
a     5
b     6
c     7
a    11
b    13
'''
s4.shape # (7,)


# 열 단위 결합(axis = 1) : cbind
s5 = pd.concat([s1, s2, s3], axis = 1)
s5
'''
     0  1     2
a  1.0  5  11.0
b  3.0  6  13.0
c  NaN  7   NaN
'''
s5.shape # (3, 3) # 2차원

# 2. DataFrame 병합
wdbc = pd.read_csv('wdbc_data.csv')
wdbc.info()
'''
RangeIndex: 569 entries, 0 to 568
Data columns (total 32 columns):
'''

# total 32 columns => DF1(16) + DF2(16)
cols = list(wdbc.columns)
len(cols) # 32

DF1 = wdbc[cols[:16]] 
DF1.shape # (569, 16)

DF2 = wdbc[cols[16:]]
DF2.shape # (569, 16)

# id 칼럼 추가 (공통칼럼)
id = wdbc.id
DF2['id'] = id    
DF2.shape # (569, 17)
DF2.head()
'''
   smoothness_se  compactness_se  ...  dimension_worst        id
0       0.008045        0.011800  ...          0.06771  87139402
1       0.007470        0.035810  ...          0.07587   8910251
2       0.005158        0.009355  ...          0.07881    905520
3       0.011270        0.034980  ...          0.06784    868871
4       0.005012        0.014850  ...          0.06766   9012568
'''

# ● 병합(merge) : 공통칼럼 기준으로 합칠때
DF_merge = pd.merge(DF1, DF2)
DF_merge.info()
'''
Int64Index: 569 entries, 0 to 568
Data columns (total 32 columns):
'''

# ● 결합 : 공통칼럼 없이 합칠때
DF1 = wdbc[cols[:16]] 
DF1.shape # (569, 16)

DF2 = wdbc[cols[16:]]
DF2.shape # (569, 16)

DF_concat = pd.concat([DF1, DF2], axis=1) # 열 단위
DF_concat.info()
'''
RangeIndex: 569 entries, 0 to 568
Data columns (total 32 columns):
'''







