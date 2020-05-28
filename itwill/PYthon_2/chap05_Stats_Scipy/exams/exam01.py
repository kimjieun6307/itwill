# -*- coding: utf-8 -*-
"""
문01) 이항검정 : 토요일(Sat)에 오는 여자 손님 중 비흡연자가 흡연자 보다 많다고 할 수 있는가?

 # 귀무가설 : 비흡연자와 흡연자의 비율은 차이가 없다.(P=0.5)
"""

import pandas as pd

tips = pd.read_csv("../data/tips.csv")
print(tips.info())
'''
<class 'pandas.core.frame.DataFrame'>
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
 
print(tips.head())

day = tips['day']
print(day.value_counts())
'''
Sat     87  -> 토요일 빈도수 
Sun     76
Thur    62
Fri     19
'''

gender = tips['sex']
print(gender.value_counts())
'''
Male      157
Female     87 -> 여자 빈도수
'''
import numpy as np

sat_Fe=tips[np.logical_and(tips['day']=='Sat', tips['sex']=='Female')]
sat_Fe
len(sat_Fe) # 28 => 시행횟수(토요일에 오는 여자 손님)

sat_Fe_smok = sat_Fe[sat_Fe['smoker']=='Yes']
len(sat_Fe_smok) # 15 => 성공횟수(흡연자)


from scipy import stats
pv=stats.binom_test(15, 28, 0.5, alternative='two-sided')
pv
# 0.8505540192127226 >= 0.05 : 귀무가설 채택(비흡연자와 흡연자 비율 차이 없다.)







