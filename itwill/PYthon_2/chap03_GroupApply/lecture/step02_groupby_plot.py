# -*- coding: utf-8 -*-
"""
집단변수 기준 자료 분석
 - subsest 생성
 - group 객체 생성
 - 시각화
"""

import pandas as pd
# 1. dataset load
wine = pd.read_csv("winequality-both.csv")
wine.info() # object 컬럼- type, quality
wine.head()

# 칼럼명 변경 : 공백 -> '_' 교체
wine.columns  = wine.columns.str.replace(' ', '_')
wine.info()

# 집단변수 확인
wine['type'].unique() # ['red', 'white']
wine.quality.unique() # [5, 6, 7, 4, 8, 3, 9] # 최대 9개 정도 집단

# 2.subset 생성
# 1) type 칼럼 : DataFrame
red_wine = wine.loc[wine['type']=='red'] # .loc[row, col]
red_wine.info()
'''
Int64Index: 1599 entries, 0 to 1598
Data columns (total 13 columns):
'''
red_wine.shape # (1599, 13)

# 2)type(행) vs quality(열)) : 1차원
red_quality = wine.loc[wine['type']=='red', 'quality'] 
type(red_quality) # pandas.core.series.Series
red_quality.shape # (1599,)

white_quality = wine.loc[wine['type']=='white', 'quality'] 
type(white_quality) # pandas.core.series.Series
white_quality.shape # (4898,)


white_quality2 = wine.loc[wine['type']=='white', ['quality', 'alcohol']] 
type(white_quality2) # pandas.core.frame.DataFrame
white_quality2.shape # (4898, 2)


# 3. group 객체 생성 : 집단변수 2개-> 11개 변수 그룹화
# 형식) DF.groupby(['칼럼1', '칼럼2'])
wine_grp =  wine.groupby(['type', 'quality'])

# 각 그룹의 빈도수
# 1d -> 2d : 교차분할표
grp_2d = wine_grp.size().unstack()
'''
quality     3      4       5       6      7      8    9
type                                                   
red      10.0   53.0   681.0   638.0  199.0   18.0  NaN
white    20.0  163.0  1457.0  2198.0  880.0  175.0  5.0
'''

# 교차분할표
tab= pd.crosstab(wine['type'], wine['quality']) # (index = 행, columns=열)
tab
'''
quality   3    4     5     6    7    8  9
type                                     
red      10   53   681   638  199   18  0
white    20  163  1457  2198  880  175  5
'''
# 결측치가 'NaN' 이나 '0' 이냐 차이


# 4. group 객체 시각화
import matplotlib.pyplot as plt

type(grp_2d) # pandas.core.frame.DataFrame
# 누적형 가로막대
grp_2d.plot(kind='barh', title='type vs quality', stacked = True)
plt.show()
#@@2


# 5. wine 종류(집단변수) vs 알콜(연속형) 통계량
wine_grp = wine.groupby('type') # 집단변수 1개 -> 나머지(12개)변수 그룹화

# 집단별 알콜 요약통계량
wine_grp['alcohol'].describe()
'''
        count       mean       std  min  25%   50%   75%   max
type                                                          
red    1599.0  10.422983  1.065668  8.4  9.5  10.2  11.1  14.9
white  4898.0  10.514267  1.230621  8.0  9.5  10.4  11.4  14.2
'''













