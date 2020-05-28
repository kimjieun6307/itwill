# -*- coding: utf-8 -*-
"""
계층적 군집분석(hierarchy)
 - 상향식(Bottom-up)으로 계층적 군집 형성
 - 유클리드안 거리계산식 이용
 - 숫자형 변수만 사용 가능
"""

import pandas as pd # DataFrame
from sklearn.datasets import load_iris # dataset
from scipy.cluster.hierarchy import linkage, dendrogram # 계층적 군집분석 도구(tool)
import matplotlib.pyplot as plt # 산점도 시각화


# 1. dataset load
iris= load_iris()
iris.feature_names

X=iris.data
y=iris.target


type(X) # numpy.ndarray
type(y) # numpy.ndarray

iris_df = pd.DataFrame(X, columns=iris.feature_names)
sp = pd.Series(y)

# y 변수 추가
iris_df['species'] = sp

iris_df.info()
'''<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
 4   species            150 non-null    int32  
 '''
 
# 2. 계측적 군집분석
'''
<군집화 방식>
1. method='single' (단일기준결합방식) : 각 군집에서 중심으로부터 거리가 가까운 것 1개씩 비교하여 가장 가까운 것 끼리 군집화 
2. method='complete' (완전기준결합방식) : 각 군집에서 중심으로부터 가장 먼 대상끼리 비교하여 가장 가까운 것 끼리 군집화 
3. method='average' (평균기준결합방식) : 한 군집 안에 속해 있는 모든 대상과 다른 군집에 속해있는 모든 대상의 쌍 집합에 대한 거리를 
                                        평균 계산하여 가장 가까운 것 끼리 군집화 
'''
clusters = linkage(iris_df, method='complete', metric='euclidean')
clusters.shape # (149, 4)  # (150, 5) -> (149, 4) : 이등변삼각형 구조로 유클리드 거리 계산


# 3. 덴드로그램 시각화
plt.figure(figsize=(20, 5))
dendrogram(clusters, leaf_rotation = 90, leaf_font_size=20,)
plt.show()
'''
leaf_rotation : 회적 각도
마지막에 꼭 ','
''' 
#@@1


# 4. 클러스터 자르기 -> 평가 : 덴드로그램 결과로 판단 
from scipy.cluster.hierarchy import fcluster # cluster 자르기

# 1) 클러스터 자르기
cluster = fcluster(clusters, t=3, criterion='distance')
'''
criterion : 기준 (어떤 기준으로 자를것인지)
criterion = 'distance' : 유클리드 거리계산 기준으로 클러스터 자르기
t = 3 : 덴드로그램 결과로 판단해서 군집 3개로 정함.
'''
cluster
'''
array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
       3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
       3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2, 2, 2, 2, 3, 2, 2, 2,
       2, 3, 2, 3, 3, 2, 2, 2, 2, 3, 2, 3, 2, 3, 2, 2, 3, 3, 2, 2, 2, 2,
       2, 3, 3, 2, 2, 2, 3, 2, 2, 2, 3, 2, 2, 2, 3, 2, 2, 3], dtype=int32)
'''
type(cluster) # numpy.ndarray
cluster.shape # (150,)

# 2) DF칼럼 추가
iris_df['cluster']=cluster
iris_df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 6 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
 4   species            150 non-null    int32  
 5   cluster            150 non-null    int32 
'''

iris_df.head()
'''
   sepal length (cm)  sepal width (cm)  ...  species  cluster
0                5.1               3.5  ...        0        1
1                4.9               3.0  ...        0        1
2                4.7               3.2  ...        0        1
3                4.6               3.1  ...        0        1
4                5.0               3.6  ...        0        1
'''

# 3) 산점도
plt.scatter(x=iris_df['sepal length (cm)'], y=iris_df['petal length (cm)'], 
            c=iris_df['cluster'], marker='o' )
#@@2


# 4) 관측치 vs 예측치
tab = pd.crosstab(iris_df['species'], iris_df['cluster'])
tab
'''
cluster   1   2   3
species            
0        50   0   0
1         0   0  50
2         0  34  16
'''


# 5) 군집별 특성 분석
# DF.groupby('집단변수')

cluster_grp = iris_df.groupby('cluster')
cluster_grp.size()
'''
cluster
1    50
2    34
3    66
'''
cluster_grp.mean()
'''
         sepal length (cm)  sepal width (cm)  ...  petal width (cm)   species
cluster                                       ...                            
1                 5.006000          3.428000  ...          0.246000  0.000000
2                 6.888235          3.100000  ...          2.123529  2.000000
3                 5.939394          2.754545  ...          1.445455  1.242424
'''

grp_m = cluster_grp.mean()
grp_m.iloc[:, :3]
'''
         sepal length (cm)  sepal width (cm)  petal length (cm)
cluster                                                        
1                 5.006000          3.428000           1.462000
2                 6.888235          3.100000           5.805882
3                 5.939394          2.754545           4.442424
'''
grp_m.iloc[:, 3]
'''
cluster
1    0.246000
2    2.123529
3    1.445455
Name: petal width (cm), dtype: float64
'''










