# -*- coding: utf-8 -*-
"""
카이제곱검정(chisquare test)
- 일원 카이제곱, 이원 카이제곱
"""

from scipy import stats
import numpy as np


# 1. 일원 카이제곱
# 귀무가설 : 관측치와 기대치는 차이가 없다.(게임에 적합하다.) 
# 대립가설 : 관측치와 기대치는 차이가 있다.(게임에 적합하지 않다.) 
real_data = [4, 6, 17, 16, 8, 9] # 관측치 
exp_data = [10,10,10,10,10,10] # 기대치 
chis = stats.chisquare(real_data, exp_data) 
chis
# Power_divergenceResult(statistic=14.200000000000001, pvalue=0.014387678176921308)
'''
statistic=14.200000000000001 ==기대비율 ==χ2
χ2 = Σ (관측값 - 기댓값)2 / 기댓값
'''

print('statistic = %.3f, pvalue= %.3f'%(chis)) 
# statistic = 14.200
# pvalue = 0.014 < 0.05 : 귀무가설 기각(게임에 적합하지 않다.)

# list -> numpy : 수학/통계 함수 사용하기 위해
real_arr = np.array(real_data)
exp_arr = np.array(exp_data)

chis2 = sum((real_arr - exp_arr)**2 / exp_arr)
chis2 # 14.200000000000001 ==statistic과 동일


# 2. 이원 카이제곱 검정
import pandas as pd

'''
 교육수준과 흡연유무 간의 관련성(독립성) 검정 
 귀무가설 : 교육수준과 흡연유무 간의 관련성 없다.
'''
smoke = pd.read_csv("smoke.csv")
smoke.info()
'''
RangeIndex: 355 entries, 0 to 354
Data columns (total 2 columns):
 #   Column     Non-Null Count  Dtype
---  ------     --------------  -----
 0   education  355 non-null    int64
 1   smoking    355 non-null    int64
'''

# DF -> vector
education = smoke.education
smoking = smoke.smoking

chis = stats.chisquare(education, smoking)
chis
# Power_divergenceResult(statistic=347.66666666666663, pvalue=0.5848667941187113)
# 검정통계량이 크면 클수록 pvalue값도 1에 가까워짐 >> 귀무가설 채택(두변수 간의 관련성 없다.)
# pvalue=0.5848667941187113 >=0.05 : 귀무가설 채택(교육수준과 흡연유무 간의 관련성 없다.)

# 카이제곱 검정 하기 전에 교차분할표 확인 할 것. (회귀분석 전에 상관관계 확인하는 것과 비슷)
# cross table
table = pd.crosstab(education, smoking)
table
'''
smoking     1   2   3
education            
1          51  92  68
2          22  21   9
3          43  28  21
'''


'''
성별 vs 흡연 독립성 검정
'''
tips = pd.read_csv('tips.csv')
tips.info()

sex = tips.sex
smoker = tips.smoker

ctable = pd.crosstab(sex, smoker)
ctable
'''
smoker  No  Yes
sex            
Female  54   33
Male    97   60
'''

tips_chis = stats.chisquare(sex, smoker) # error -- 관측치가 문자면 검정 안됨.
# TypeError: unsupported operand type(s) for -: 'str' and 'str'

# dummy 생성 :  1 or 2
sex_dum = [1 if i == 'Male' else 2 for i in sex]
smoker_dum = [1 if i == 'No' else 2 for i in smoker]

tips_chis = stats.chisquare(sex_dum, smoker_dum)
tips_chis # Power_divergenceResult(statistic=84.0, pvalue=1.0)
#  pvalue=1.0 > 0.05 : 귀무가설 채택 (성별과 흡연여부는 관계 없다. )

