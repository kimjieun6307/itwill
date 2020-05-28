# -*- coding: utf-8 -*-
"""
step01_Series.py

Series 객체 특징
 - 1차원의 배열구조
 - 자체 객체에서 수학/통계 함수 제공
 - 범위 수정, 블럭 연산
 - indexing/slicing
 - 시계열 데이터 생성
"""

import pandas as pd # 별칭 pd
from pandas import Series # 패키지 import class

'''
1. Series 객체 생성
 (1) list 이용
'''
lst = [4000, 3000, 3500, 2000]
ser = pd.Series(lst) # list -> Series 객체 생성
print('lst = ', lst) # lst =  [4000, 3000, 3500, 2000]
print('ser = ', ser)
''' ser =
0    4000
1    3000
2    3500
3    2000
dtype: int64
'''
# object.member
print(ser.index) # 색인
# RangeIndex(start=0, stop=4, step=1)
print(ser.values) # 값
#[4000 3000 3500 2000]

ser1_2 = Series([4000, 3000, 3500, 2000],index=['a','b','c','d'])
print(ser1_2.index) 
# Index(['a', 'b', 'c', 'd'], dtype='object')
print(ser1_2.values) 
# [4000 3000 3500 2000]
print(ser1_2)
'''
a    4000
b    3000
c    3500
d    2000
dtype: int64
'''

'''
 (2) dict 이용
'''
person = {'name': '홍길동', 'age':35, 'addr':'서울시'}
ser2 = Series(person)
print(ser2)
'''
name    홍길동
age      35
addr    서울시
dtype: object
'''
print(ser2.index) # Index(['name', 'age', 'addr'], dtype='object')
print(ser2.values) # ['홍길동' 35 '서울시']

# index 사용 : object[n or 조건식]
print(ser2['age']) # 35
print(ser[0]) # 4000

# boolean 조건식
print(ser[ser>=3500])
'''
0    4000
2    3500
dtype: int64
'''


#2. indexing : list 동일
ser3 = Series([4, 4.5, 6, 8, 10.5]) # 생성자
print(ser3[0]) 
print(ser3[:3])
print(ser3[3:])
# Series에서 인텍스 음수 값 사용 못함(list 타입과 차이점)
print(ser3[-1]) # KeyError: -1


# 3. Series 결합과 NA 처리
p1 = Series([400, None, 350, 200], index=['a','b','c','d'])
p2 = Series([400, 150, 350, 200], index=['a','c','d','e'])

# Series 결합(연산)
p3 = p1 + p2
print(p3)
'''
a    800.0
b      NaN
c    500.0
d    550.0
e      NaN
dtype: float64
'''

# 4. 결측치 처리 방법(평균, 0, 제거) 
print(type(p3))
#<class 'pandas.core.series.Series'>

# 1) 평균 대체
p4 = p3.fillna(p3.mean())
print(p4)
'''
a    800.000000
b    616.666667
c    500.000000
d    550.000000
e    616.666667
dtype: float64
'''

# 2) 0으로 대체
p5 = p3.fillna(0)
print(p5)
'''
a    800.0
b      0.0
c    500.0
d    550.0
e      0.0
dtype: float64
'''

# 3) 결측치 제거
p6 = p3[pd.notnull(p3)] # subset
print(p6)
'''
a    800.0
c    500.0
d    550.0
dtype: float64
'''

# 5.범위 수정, 블럭 연산
print(p2) # p2 = Series([400, 150, 350, 200], index=['a','c','d','e'])
'''
a    400
c    150
d    350
e    200
dtype: int64
'''

# 범위 수정
p2[1:3] = 300
print(p2)
'''
a    400
c    300
d    300
e    200
dtype: int64
'''

# list에서 범위 수정 사용 못함.
lst = [1,2,3,4]
lst[1:3] = 3 # TypeError: can only assign an iterable

# 2) 블럭 연산
print(p2+p2) # 2배
print(p2-p2) # 0

# 3) breacast 연산 : 1차원 vs 0차원(scala)
v1 = Series([1,2,3,4])
scala = 0.5
b = v1 * scala
print(b)
'''
0    0.5
1    1.0
2    1.5
3    2.0
dtype: float64
'''

# list타입일때 연산방법
for i in v1 :
    b = i *scala
    print(b)
'''
0.5
1.0
1.5
2.0
'''

# 4) 수학/통계 함수
print('sum = ', v1.sum()) 
print('mean = ', v1.mean())
print('var = ', v1.var())
print('std = ', v1.std())
print('max = ' , v1.max())
'''
sum =  10
mean =  2.5
var =  1.6666666666666667
std =  1.2909944487358056
max =  4
'''

# 호출 가능한 멤버 확인
print(dir(v1))
#@@1 
print(v1.shape) # (4,0)
print(v1.size) # 4 
















