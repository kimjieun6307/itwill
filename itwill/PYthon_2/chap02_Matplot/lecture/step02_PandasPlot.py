# -*- coding: utf-8 -*-
"""
Pandas 객체에서 지원하는 시각화
    형식) object.plot(kind=차트유형)
    object : Series or DataFrame
    kind : bar, barh, pie, hist, kde, box, scatter
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1. Series 객체 시각화
ser = pd.Series(np.random.randn(10))
print(ser)
'''
0   -1.212322
1   -0.383220
2   -2.481782
3   -0.223017
4    0.296908
5   -0.774793
6    1.248133
7   -1.063947
8    0.988613
9    1.075950
'''
ser = pd.Series(np.random.randn(10), index=np.arange(0,100,10))
print(ser)
'''
0    -2.216169
10    0.304578
20    0.339650
30    0.513637
40   -0.987869
50    0.824736
60    0.470416
70   -0.237279
80    0.936039
90    1.074765
'''
ser.plot(color='r') # 기본차트 : 선 그래프
#@@21
#@@22

# 2. DataFrame 객체 시각화
df = pd.DataFrame(np.random.randn(10,4), columns=['one','two','three','four'])
'''
        one       two     three      four
0 -0.448076  0.348492 -0.774082 -1.812570
1 -0.869673 -0.253701  0.655023 -0.196319
2 -1.384125  0.460298 -0.054195 -0.374271
3  1.008963  1.076081  0.551827  1.399011
4  1.095175  1.722058  0.623936  0.055232
5 -0.135830 -0.097440 -0.973239  1.818148
6 -0.086051 -0.325179 -0.118892 -0.511258
7  1.322146 -0.091066  0.783017 -0.017433
8 -0.325556  2.352182  2.214523  0.160581
9  1.917505 -1.081944  2.681576 -0.199954
'''
df.shape # (10, 4)

# 기본차트
df.plot()
#@@24

# 세로 막대차트
df.plot(kind = 'bar', title = "kind = 'bar'")
#@@25
# 가로 막대차트
df.plot(kind = 'barh', title = "kind = 'barh'(가로)")
#@@26
# 가로 누적형 막대차트
df.plot(kind = 'barh', title = "stacked=True(누적)", stacked=True)
#@@27

# 도수분포(히스토그램)
df.plot(kind = 'hist', title="df.plot(kind = 'hist')")
#@@28

# 커널밀도추정 : kde
df.plot(kind = 'kde', title="df.plot(kind = 'kde')")
#@@29

'''
tips.csv 적용
'''
tips = pd.read_csv('tips.csv')
tips.info()
'''
RangeIndex: 244 entries, 0 to 243
Data columns (total 7 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   total_bill  244 non-null    float64
 1   tip         244 non-null    float64
 2   sex         244 non-null    object 
 3   smoker      244 non-null    object 
 4   day         244 non-null    object 
 5   time        244 non-null    object 
 6   size        244 non-null    int64  
'''
# 전체 7개 칼럼 중에서 차트를 만들수 있는 칼럼(숫자)은 3개
tips.head()
'''
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
'''

# 요일(day) vs 파티규모(size) 범주확인
tips['day'].unique() # ['Sun', 'Sat', 'Thur', 'Fri']
tips['size'].unique() # [2, 3, 4, 1, 6, 5]
# 교차분할표 4x6 = 24셀 : 집단변수 vs 집단변수 빈도수 확인
tab = pd.crosstab(tips['day'], tips['size'])
print(tab)
'''
size  1   2   3   4  5  6
day                      
Fri   1  16   1   1  0  0
Sat   2  53  18  13  1  0
Sun   0  39  15  18  3  1
Thur  1  48   4   5  1  3
'''
type(tab) # pandas.core.frame.DataFrame

tab_result = tab.loc[:,2:5]
tab_result
#@@30
tab_result.plot(kind='barh', stacked=True, title='day vs size columns plot')

# 3. 산점도 matrix : plotting.scatter_matrix(data)
from pandas import plotting
iris = pd.read_csv('iris.csv')
iris.info()

cols = list(iris.columns)
iris_x = iris[cols[:4]]
iris_x.shape

plotting.scatter_matrix(iris_x)
#@@32

# 4. 3d 산점도
from mpl_toolkits.mplot3d import Axes3D

col1 = iris[cols[0]]
col2 = iris[cols[1]]
col3 = iris[cols[2]]

iris['Species'].unique()

cdata = [] 
for i in iris['Species']:
    if i == 'setosa':
        cdata.append(1)
    elif i == 'versicolor':
        cdata.append(2)
    else : 
        cdata.append(3)
        
fig = plt.figure()
chart = fig.add_subplot(1,1,1, projection = '3d')
chart.scatter(col1, col2, col3, c=cdata) #(x,y,z)
chart.set_xlabel('col1')
chart.set_ylabel('col2')
chart.set_zlabel('col3')
#@@33




