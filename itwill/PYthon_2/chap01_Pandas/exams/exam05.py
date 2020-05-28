'''   
문5) iris.csv 파일을 읽어와서 다음과 같이 처리하시오.
   조건1> 1~4 칼럼 대상 vector 생성(col1, col2, col3, col4)    
   조건2> 1,4 칼럼 대상 합계, 평균, 표준편차 구하기 
   조건3> 1,2 칼럼과 3,4 칼럼을 대상으로 각 df1, df2 데이터프레임 생성
   조건4> df1과 df2 칼럼 단위 결합 iris_df 데이터프레임 생성      
'''

import pandas as pd

# C:\ITWILL\4_Python-II\data 절대 경로 설정되어 있음.
iris = pd.read_csv('iris.csv')
print(iris.info())

#  조건1> 1~4 칼럼 대상 vector 생성(col1, col2, col3, col4)  
col1 = iris['Sepal.Length']
col2 = iris['Sepal.Width']
col3 = iris['Petal.Length']
col4 = iris['Petal.Width']

#조건2> 1,4 칼럼 대상 합계, 평균, 표준편차 구하기
col1.sum()
col2.sum()
col3.sum()
col4.sum()

col1.mean()
col2.mean()
col3.mean()
col4.mean()

col1.std()
col2.std()
col3.std()
col4.std()
#@@4

# 조건3> 1,2 칼럼과 3,4 칼럼을 대상으로 각 df1, df2 데이터프레임 생성
df1 = pd.concat([col1, col2], axis = 1)
df2 = pd.concat([col3, col4], axis = 1)
#@@5

# df1과 df2 칼럼 단위 결합 iris_df 데이터프레임 생성  
iris_df = pd.concat([df1, df2], axis = 1)
iris_df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Sepal.Length  150 non-null    float64
 1   Sepal.Width   150 non-null    float64
 2   Petal.Length  150 non-null    float64
 3   Petal.Width   150 non-null    float64
'''


