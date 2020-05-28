# -*- coding: utf-8 -*-
"""
집단간 평균차이 검정(t_test)
 1. 한 집단 평균차이 검정
 2. 두 집단 평균차이 검정
 3. 대응 두 집단 평균차이 검정
"""
from scipy import stats # t검정
import numpy as np # 숫자연산
import pandas as pd # file read

# 1. 한 집단 평균차이 검정

# 대한민국 남자 평균 키(모평균) : 175.5cm
# 모집단 -> 표본 추출(300명) 
sample_data = np.random.uniform(172, 180, size = 300)
sample_data

# 기술통계
sample_data.mean() # 175.99344318408663

one_group_test = stats.ttest_1samp(sample_data, 175.5)
one_group_test
# Ttest_1sampResult(statistic=3.6908988414605757, pvalue=0.00026549934744397207)

print('statistic = %.5f, pvalue = %.5f'%(one_group_test))
#statistic = 3.69090, pvalue = 0.00027 < 0.05 : 평균 차이가 있다.

#--- size = 30-------------------------------------
sample_data = np.random.uniform(172, 180, size = 30)

sample_data.mean() # 175.99344318408663

one_group_test = stats.ttest_1samp(sample_data, 175.5)
print('statistic = %.5f, pvalue = %.5f'%(one_group_test))
#statistic = 1.77523, pvalue = 0.08636 > 0.05 : 평균 차이가 없다.

# 2. 두 집단 평균차이 검정
female_score = np.random.uniform(50, 100, size=30)
male_score = np.random.uniform(45,95, size = 30)
two_sample = stats.ttest_ind(female_score, male_score)

two_sample
# Ttest_indResult(statistic=3.243773569865785, pvalue=0.0019590571625838424)
print('statistic = %.5f, pvalue = %.5f'%(two_sample))
# statistic = 3.24377, pvalue = 0.00196 <0.05 : 남녀 평균 차이가 있다.

# 기술통계
female_score.mean() # 73.62223127608894
male_score.mean() # 62.07018970439184



# csv file load
two_sample = pd.read_csv('C:/ITWILL/4_Python-II/data/two_sample.csv') 
two_sample.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 240 entries, 0 to 239
Data columns (total 5 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   no      240 non-null    int64  
 1   gender  240 non-null    int64  
 2   method  240 non-null    int64  
 3   score   180 non-null    float64
 4   survey  240 non-null    int64 
 '''
 
sample_data = two_sample[['method', 'score']]
sample_data.head() 
'''
   method  score
0       1    5.1
1       1    5.2
2       1    4.7
3       1    NaN
4       1    5.0
'''

sample_data['method'].value_counts()
'''
2    120
1    120
'''

# 교육방법에 따른 subset
method1=sample_data[sample_data['method']==1]
method2=sample_data[sample_data['method']==2]

score1 = method1.score
score2 = method2.score

# nan -> error
two_sample = stats.ttest_ind(score1, score2)
two_sample # Ttest_indResult(statistic=nan, pvalue=nan)

# Nan -> 평균 대체
score1 = score1.fillna(score1.mean())
score2 = score2.fillna(score2.mean())

two_sample = stats.ttest_ind(score1, score2)
print('statistic = %.5f, pvalue = %.5f'%(two_sample))
# statistic = -0.94686, pvalue = 0.34467 > 0.05 : 두 집단 평균 차이 없다.

score1.mean() # 5.496590909090908
score2.mean() # 5.591304347826086


# 3. 대응 두 집단 평균차이 검정 : 복용전 65 -> 복용후 60 변환
before = np.random.randint(65, size = 30)*0.5
after = np.random.randint(60, size = 30)*0.5

before
after

pired_test = stats.ttest_rel(before, after)
pired_test
print('statistic = %.5f, pvalue = %.5f'%(pired_test))
# statistic = 1.22867, pvalue = 0.22907 > 0.05 : 두 집단 평균차이 없다. (다이어트 효능 없음)

before.mean()
after.mean()
