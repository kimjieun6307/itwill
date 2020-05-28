# -*- coding: utf-8 -*-
"""
피벗테이블(pivot table)
 - 사용자가 직접 행과 열 그리고 교차셀에 변수를 지정하여 테이블 생성
"""
import pandas as pd

pivot_data = pd.read_csv("pivot_data.csv")
pivot_data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 8 entries, 0 to 7
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   year     8 non-null      int64 
 1   quarter  8 non-null      object
 2   size     8 non-null      object
 3   price    8 non-null      int64 
'''
# 교차셀 : 매출액(price)
# 행 : 년도(year),  분기(quarter) --집단변수
# 열 : 매출규모(size) --집단변수
# 셀에 적용할 통계 : sum

p_table = pd.pivot_table(pivot_data, values='price', index = ['year', 'quarter'],
               columns='size', aggfunc = 'sum')

p_table
'''
size          LARGE  SMALL
year quarter              
2016 1Q        2000   1000
     2Q        2500   1200
2017 3Q        2200   1300
     4Q        2800   2300
'''

p_table.shape # (4,2)
p_table.plot(kind='barh')

ptable = pd.pivot_table(pivot_data, index='year', columns = 'size',
                        values='price', aggfunc = 'sum')
ptable
'''
size  LARGE  SMALL
year              
2016   4500   2200
2017   5000   3600
'''

# movie_rating.csv 이용 피벗테이블 생성하기
'''
행 : 평가자(critic)
열 : 영화제목(title)
셀 : 평점(rating)
적용함수 : sum
'''
movie = pd.read_csv("movie_rating.csv")
movie.info()

movie_ptab = pd.pivot_table(movie, index='critic', columns='title', 
                            values='rating', aggfunc='sum')

movie_ptab
'''
title    Just My  Lady  Snakes  Superman  The Night  You Me
critic                                                     
Claudia      3.0   NaN     3.5       4.0        4.5     2.5
Gene         1.5   3.0     3.5       5.0        3.0     3.5
Jack         NaN   3.0     4.0       5.0        3.0     3.5
Lisa         3.0   2.5     3.5       3.5        3.0     2.5
Mick         2.0   3.0     4.0       3.0        3.0     2.0
Toby         NaN   NaN     4.5       4.0        NaN     1.0
'''

# 평가자 기준 평점 평균
movie_ptab.mean(axis=1)
'''
Claudia    3.500000
Gene       3.250000
Jack       3.700000
Lisa       3.000000
Mick       2.833333
Toby       3.166667
'''

#  영화 기준 평점 평균
movie_ptab.mean(axis=0) # = movie_ptab.mean()
'''
Just My      2.375000
Lady         2.875000
Snakes       3.833333
Superman     4.083333
The Night    3.300000
You Me       2.500000
'''









