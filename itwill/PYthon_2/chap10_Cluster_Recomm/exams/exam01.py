'''
 문) 중학교 1학년 신체검사(bodycheck.csv) 데이터 셋을 이용하여 다음과 같이 군집모델을 생성하시오.
  <조건1> 악력, 신장, 체중, 안경유무 칼럼 대상 [번호 칼럼 제외]
  <조건2> 계층적 군집분석의 완전연결방식 적용 
  <조건3> 덴드로그램 시각화 
  <조건4> 텐드로그램을 보고 3개 군집으로 서브셋 생성  
'''

import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster # 계층적 군집 model
import matplotlib.pyplot as plt

# data loading - 중학교 1학년 신체검사 결과 데이터 셋 
body = pd.read_csv("../data/bodycheck.csv", encoding='ms949')
print(body.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 15 entries, 0 to 14
Data columns (total 5 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   번호      15 non-null     int64
 1   악력      15 non-null     int64
 2   신장      15 non-null     int64
 3   체중      15 non-null     int64
 4   안경유무    15 non-null     int64
'''
 
# <조건1> subset 생성 - 악력, 신장, 체중, 안경유무 칼럼  이용 
# body_df = body[['악력', '신장', '체중', '안경유무']]
body_df = body.iloc[:, 1:5]
body_df.info()
'''
RangeIndex: 15 entries, 0 to 14
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   악력      15 non-null     int64
 1   신장      15 non-null     int64
 2   체중      15 non-null     int64
 3   안경유무    15 non-null     int64
 '''

# <조건2> 계층적 군집 분석  완전연결방식 
clusters = linkage(body_df, method='complete',  metric='euclidean')
clusters


# <조건3> 덴드로그램 시각화 : 군집수는 사용 결정 
dendrogram(clusters,)
#@@3

# <조건4> 텐드로그램을 보고 3개 군집으로 서브셋 생성
'''
cluster1 - 9 3 7 0 14
cluster2 - 10 2 4 5 13
cluster3 - 1 8 12 6 11
'''

cluster = fcluster(clusters, t=3, criterion='distance',)
body_df['cluster']=cluster
body_df
'''
    악력   신장  체중  안경유무  cluster
0   28  146  34     1        4
1   46  169  57     2       14
2   39  160  48     2        6
3   25  156  38     1        1
4   34  161  47     1        7
5   29  168  50     1        9
6   38  154  54     2       11
7   23  153  40     1        2
8   42  160  62     2       13
9   27  152  39     1        3
10  35  155  46     1        8
11  39  154  54     2       11
12  38  157  57     2       12
13  32  162  53     2       10
14  25  142  32     1        5
'''

# cluster 구성
cluster1 = [9, 3, 7, 0, 14]
cluster2 = [10, 2, 4, 5, 13]
cluster3 = [1, 8, 12, 6, 11]

cluster1_df = body_df.iloc[cluster1]
cluster2_df = body_df.iloc[cluster2]
cluster3_df = body_df.iloc[cluster3]

# 칼럼 추가
body_df.loc[cluster1, 'cluster'] = 1
body_df.loc[cluster2, 'cluster'] = 2
body_df.loc[cluster3, 'cluster'] = 3

body_df
'''
    악력   신장  체중  안경유무  cluster
0   28  146  34     1        1
1   46  169  57     2        3
2   39  160  48     2        2
3   25  156  38     1        1
4   34  161  47     1        2
5   29  168  50     1        2
6   38  154  54     2        3
7   23  153  40     1        1
8   42  160  62     2        3
9   27  152  39     1        1
10  35  155  46     1        2
11  39  154  54     2        3
12  38  157  57     2        3
13  32  162  53     2        2
14  25  142  32     1        1
'''

# 각 집단별 특성 분석
cluster_grp = body_df.groupby('cluster')
cluster_grp.size()
cluster_grp.describe()
cluster_grp.mean()
'''
           악력     신장    체중  안경유무
cluster                         
1        25.6  149.8  36.6   1.0
2        33.8  161.2  48.8   1.4
3        40.6  158.8  56.8   2.0
'''

