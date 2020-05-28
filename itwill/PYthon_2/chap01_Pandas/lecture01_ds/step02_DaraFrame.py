# -*- coding: utf-8 -*-
"""
DataFrame 자료구조 특징
 - 2차원 행렬구조(table 유사함)
 - 열(칼럼) 단위 데이터 처리 용이
 - Series(1차)의 모음 <-> DataFrame(2차)
"""

import pandas as pd
from pandas import Series, DataFrame

# 1. DataFrame 생성

# 1) 기본 자료구조(list, dict) 이용
name = ['hong', 'lee', 'kang', 'yoo'] # list
age = [35, 45, 55, 25] # list
pay = [250, 350, 450, 200]
addr = ['서울시', '부산시', '대전시', '인천시']
# dict
data = {'name':name, 'age':age, 'pay':pay, 'addr':addr}
pd.DataFrame(data = data)
'''
   name  age  pay addr
0  hong   35  250  서울시
1   lee   45  350  부산시
2  kang   55  450  대전시
3   yoo   25  200  인천시
'''

frame = pd.DataFrame(data = data, columns = ['name', 'age', 'addr', 'pay'])
print(frame)
'''
   name  age addr  pay
0  hong   35  서울시  250
1   lee   45  부산시  350
2  kang   55  대전시  450
3   yoo   25  인천시  200
'''
# 칼럼 추출
age = frame['age'] # frame.age
print(age.mean()) # 40.0
print(type(age)) # <class 'pandas.core.series.Series'>

# 새 칼럼 추가
gender = Series(['남', '남', '남', '여'])
frame['gender'] = gender
print(frame)
'''
   name  age addr  pay gender
0  hong   35  서울시  250      남
1   lee   45  부산시  350      남
2  kang   55  대전시  450      남
3   yoo   25  인천시  200      여
'''

# 2) numpy 이용 : 선형대수 관련 함수
import numpy as np
frame2 = DataFrame(np.arange(12).reshape(3,4), columns=['a','b','c','d'])
print(frame2)
'''
   a  b   c   d
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
'''

# 행/열 통계
#@@2
print('열 단위 평균 : ', frame2.mean(axis = 0)) # 행축 : 열단위
print(frame2.mean()) # 기본값
'''
a    4.0
b    5.0
c    6.0
d    7.0
'''
print('행 단위 평균 : ', frame2.mean(axis = 1)) # 열축 : 행단위
'''
0    1.5
1    5.5
2    9.5
'''

# 2. DataFrame 칼럼 참조
frame2.index # 행 이름
#RangeIndex(start=0, stop=3, step=1)

frame2.values # 값
'''
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]]
'''
#@@3

# emp.csv
#@@4
emp = pd.read_csv("C:\\ITWILL\\4_Python-II\\data\\emp.csv", encoding='utf-8')
print(emp.info()) # str(emp)
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   No      5 non-null      int64 
 1   Name    5 non-null      object
 2   Pay     5 non-null      int64 
dtypes: int64(2), object(1)
memory usage: 248.0+ bytes
'''

emp.head() # head(emp)
'''
    No Name  Pay
0  101  홍길동  150
1  102  이순신  450
2  103  강감찬  500
3  104  유관순  350
4  105  김유신  400
'''

# 1) 단일 칼럼 선택
print(emp['No'])
print(emp.No) # 칼럼명에 점'.' 포함된 경우 사용할 수 없다.

# 2) 복수 칼럼 선택 : 중첩 list
print(emp[['No', 'Pay']])
'''
print(emp[['No':'Pay']]) # SyntaxError: invalid syntax / R과 차이(연속된 칼럼 선택 차이)
'''
# 특정 원소 선택
print(emp.Name[1]) #이순신
print(emp.Name[1:])

no = emp.No
no.plot()
pay = emp['Pay']
pay.plot()
#@@1
emp[['No', 'Pay']].plot()
#@@2

'''
 3. subset 만들기 : old DF -> new DF
 (1) 특정 칼럼 제외 : 칼럼 적은 경우
'''
emp.info()
''' # 3개의 칼럼 중에서 'No'칼럼 제외하고 2개만 사용하는 경우
 0   No      5 non-null      int64 
 1   Name    5 non-null      object
 2   Pay     5 non-null      int64
'''

subset1 = emp[['Name', 'Pay']]
subset1
'''
  Name  Pay
0  홍길동  150
1  이순신  450
2  강감찬  500
3  유관순  350
4  김유신  400
'''

# (2) 특정 행 제외
subset2 = emp.drop(0) # 홍길동 제외
subset2
'''
    No Name  Pay
1  102  이순신  450
2  103  강감찬  500
3  104  유관순  350
4  105  김유신  400
'''

# (3) 조건식으로 행 선택
subset3 = emp[emp.Pay > 400]
subset3
'''
    No Name  Pay
1  102  이순신  450
2  103  강감찬  500
'''

'''
 (4) columns 이용 : 칼럼 많은 경우
 : list 타입으로 칼럼명(columns) 만들어서 사용 
 
'''
iris = pd.read_csv("C:\\ITWILL\\4_Python-II\\data\\iris.csv")
print(iris.info()) 
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Sepal.Length  150 non-null    float64
 1   Sepal.Width   150 non-null    float64
 2   Petal.Length  150 non-null    float64
 3   Petal.Width   150 non-null    float64
 4   Species       150 non-null    object 
 '''

print(iris.head()) 
'''
   Sepal.Length  Sepal.Width  Petal.Length  Petal.Width Species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa
2           4.7          3.2           1.3          0.2  setosa
3           4.6          3.1           1.5          0.2  setosa
4           5.0          3.6           1.4          0.2  setosa
'''

iris['Sepal.Width'] 
'''
0      3.5
1      3.0
2      3.2
3      3.1
4      3.6

145    3.0
146    2.5
147    3.0
148    3.4
149    3.0
Name: Sepal.Width, Length: 150, dtype: float64
'''
print(iris.Sepal.Width) # iris.Sepal.Width 사용못함.(칼럼명에 .포함되서 )
# AttributeError: 'DataFrame' object has no attribute 'Sepal'

# 칼럼명 추출
cols = list(iris.columns) 
cols
#['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']
type(cols) # list

iris_x = cols[:4]
iris_y = cols[-1]
iris_x # ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']
iris_y #  'Species'

# x, y변수 선택
X = iris[iris_x]
Y = iris[iris_y]
X.shape # (150, 4) : 2차원
Y.shape # (150,): 1차원

X.head()
Y.head()
Y.tail()

# exam01 ~ exam02

'''
4. DataFrame 행렬 index 참조 : DF[row, col]
 1) DF.loc[row, col] : label index
 2) DF.iloc[row, col] : integer index(숫자)
'''

emp
'''
    No Name  Pay
0  101  홍길동  150
1  102  이순신  450
2  103  강감찬  500
3  104  유관순  350
4  105  김유신  400
'''
# 열이름 :  No Name  Pay
# 행 이름 : 0 ~ 4

# loc[행label index, 열label index]
emp.loc[1:3, :] #label index : 글자 그대로 보기때문에 1행~3행(총 3개 행)
emp.loc[1:3]
'''
    No Name  Pay
1  102  이순신  450
2  103  강감찬  500
3  104  유관순  350
'''
emp.loc[1:3, 'Name':'Pay']
'''
  Name  Pay
1  이순신  450
2  강감찬  500
3  유관순  350
'''
emp.loc[1:3, 'Name','Pay'] # error - IndexingError: Too many indexers
emp.loc[1:3, ['Name','Pay']]
'''
  Name  Pay
1  이순신  450
2  강감찬  500
3  유관순  350
'''
emp.loc[1:3, 1:2] #error : loc에서는 문자 그대로 봐야함

# iloc[행label index, 열label index]
emp.iloc[1:3] # 숫자 index : 1행~(3-1)행 (총 2개행)
'''
    No Name  Pay
1  102  이순신  450
2  103  강감찬  500
'''
emp.iloc[1:3, 'Name':'Pay'] # error
emp.iloc[1:3, :2]  # n-1
'''
    No Name
1  102  이순신
2  103  강감찬
'''
emp.iloc[1:3, [0,2]]
'''
    No  Pay
1  102  450
2  103  500
'''
##########################################################
## DF 행렬참조 example
#########################################################
iris.shape # (150, 5)

# choice 함수 이용해서 랜덤하게 훈련 데이타셋 선택
from numpy.random import choice
help(choice)
# choice(a, size=None, replace=True, p=None)
# replace = False : 비복원 추출

row_idx = choice(a=len(iris), size = int(len(iris)*0.7), replace=False)
row_idx
'''
array([  6, 124, 127, 115,  25,   1,  44,  78,  10,  62, 111,  89, 147,
        93,  43,  26, 146,  59,  75, 149,  39, 132,  79, 131,  53,  95,
        19,  81, 140,  54, 137,  47, 119,   7,  74,  88,  76, 130,  85,
        24, 116, 143,  42, 112,  51,  20, 118, 117, 105,  29,  92, 141,
        72,  82, 128,  73, 100,  68,   4,  64,  77,  90,  35,  16, 113,
        40,  37,  58,  49,  80,  45, 114, 120,  46, 133, 109, 142,  52,
        27,  57,  28,   9,  65,  41,  21,  94,  33,  69,   8,  99,  61,
       144,  91, 108,  97,  22,  38, 138,   2,  23,  87,  48,  66, 145,
        84])
'''
len(row_idx) # 105

# train dataset
train_set = iris.iloc[row_idx]
train_set.head
'''
<bound method NDFrame.head of      Sepal.Length  Sepal.Width  Petal.Length  Petal.Width     Species
6             4.6          3.4           1.4          0.3      setosa
124           6.7          3.3           5.7          2.1   virginica
127           6.1          3.0           4.9          1.8   virginica
115           6.4          3.2           5.3          2.3   virginica
25            5.0          3.0           1.6          0.2      setosa
..            ...          ...           ...          ...         ...
87            6.3          2.3           4.4          1.3  versicolor
48            5.3          3.7           1.5          0.2      setosa
66            5.6          3.0           4.5          1.5  versicolor
145           6.7          3.0           5.2          2.3   virginica
84            5.4          3.0           4.5          1.5  versicolor

[105 rows x 5 columns]>
'''

train_set2 = iris.loc[row_idx]
train_set2.head
'''
<bound method NDFrame.head of      Sepal.Length  Sepal.Width  Petal.Length  Petal.Width     Species
6             4.6          3.4           1.4          0.3      setosa
124           6.7          3.3           5.7          2.1   virginica
127           6.1          3.0           4.9          1.8   virginica
115           6.4          3.2           5.3          2.3   virginica
25            5.0          3.0           1.6          0.2      setosa
..            ...          ...           ...          ...         ...
87            6.3          2.3           4.4          1.3  versicolor
48            5.3          3.7           1.5          0.2      setosa
66            5.6          3.0           4.5          1.5  versicolor
145           6.7          3.0           5.2          2.3   virginica
84            5.4          3.0           4.5          1.5  versicolor

[105 rows x 5 columns]>
'''

# test dataset : list + for
test_idx = [i for i in range(len(iris)) if not i in row_idx]
len(test_idx) # 45

test_set = iris.iloc[test_idx]
test_set.shape # (45, 5)

# x변수, y 변수 분리
cols = list(iris.columns)
x = cols[:4]
y = cols[-1]

iris_x = iris.loc[test_idx, x] # idex가 문자로 되어 있으면 무조건 'loc'사용
iris_y = iris.loc[test_idx, y]
iris_x.shape # (45, 4)
iris_y.shape #(45,)










