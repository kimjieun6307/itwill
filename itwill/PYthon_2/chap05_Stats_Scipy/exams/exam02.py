'''
문02) winequality-both.csv 데이터셋을 이용하여 다음과 같이 처리하시오.
   <조건1> quality, type 칼럼으로 교차분할표 작성 
   <조건2> 교차분할표를 대상으로 white 와인 내림차순 정렬       
   <조건3> red 와인과 white 와인의 quality에 대한 두 집단 평균 검정
           -> 각 집단 평균 통계량 출력
   <조건4> alcohol 칼럼과 다른 칼럼 간의 상관계수 출력  
'''

import pandas as pd
from scipy import stats
import numpy as np

wine = pd.read_csv("winequality-both.csv")
wine.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6497 entries, 0 to 6496
Data columns (total 13 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   type                  6497 non-null   object 
 1   fixed acidity         6497 non-null   float64
 2   volatile acidity      6497 non-null   float64
 3   citric acid           6497 non-null   float64
 4   residual sugar        6497 non-null   float64
 5   chlorides             6497 non-null   float64
 6   free sulfur dioxide   6497 non-null   float64
 7   total sulfur dioxide  6497 non-null   float64
 8   density               6497 non-null   float64
 9   pH                    6497 non-null   float64
 10  sulphates             6497 non-null   float64
 11  alcohol               6497 non-null   float64
 12  quality               6497 non-null   int64  
 '''
 
# <조건1> quality, type 칼럼으로 교차분할표 작성 
wine_tab = pd.crosstab(wine['quality'], wine['type'])
wine_tab
'''
type     red  white
quality            
3         10     20
4         53    163
5        681   1457
6        638   2198
7        199    880
8         18    175
9          0      5
'''

# <조건2> 교차분할표를 대상으로 white 와인 내림차순 정렬 
wine_tab_dasc = wine_tab.sort_values('white', ascending=False)
wine_tab_dasc
'''
type     red  white
quality            
6        638   2198
5        681   1457
7        199    880
8         18    175
4         53    163
3         10     20
9          0      5
'''

# <조건3> red 와인과 white 와인의 quality에 대한 두 집단 평균 검정 -> 각 집단 평균 통계량 출력
data = wine[['type', 'quality']]
red= data[data['type']=='red']
white= data[data['type']=='white']

x_red=red.quality # = wine[wine['type']=='red', 'quality']
x_whi=white.quality # = wine[wine['type']=='white', 'quality']

x_test = stats.ttest_ind(x_red, x_whi)
x_test
# Ttest_indResult(statistic=-9.685649554187696, pvalue=4.888069044201508e-22)
# pvalue < 0.05 : 귀무가설 기각

# 대립가설 채택 -> 단측 검정  
# (red 와인과 white 와인의 quality에 대한 두 집단 평균 차이가 있다.)

# 단측검정 : red < white
x_red.mean() # 5.6360225140712945
x_whi.mean() # 5.87790935075541


# <조건4> alcohol 칼럼과 다른 칼럼 간의 상관계수 출력  
wine.corr() # -->전체 변수간 상관관계

# error : wine['alcohol'].corr(); wine['alcohol'].corr(wine[])
wine.corrwith(wine['alcohol'])
'''
fixed acidity          -0.095452
volatile acidity       -0.037640
citric acid            -0.010493
residual sugar         -0.359415
chlorides              -0.256916
free sulfur dioxide    -0.179838
total sulfur dioxide   -0.265740
density                -0.686745
pH                      0.121248
sulphates              -0.003029
alcohol                 1.000000
quality                 0.444319
'''
# <해석> alcohol 칼럼과 density칼럼이 가장 큰 음의 상관관계, 
#                       quality칼럼이 가장 큰 양의 상관관계를 가진다.

