# -*- coding: utf-8 -*-
"""
Data Frame  객체 대상 그룹화
 - 형식 ) DF.groupby('집단변수').수학/통계 함수()
"""

import pandas as pd

tips = pd.read_csv("C:/ITWILL/4_Python-II/data/tips.csv")
tips.info()
tips.head()
 
#팁 비율 : 파생변수(사칙연산)
tips['tips_pat'] = tips['tip']/tips['total_bill']
tips.info()

# 변수 복제
tips['gender'] =  tips['sex']


# 변수 제거
del tips['sex']

tips.head()


# 1.  집단 변수 1개 -> 전체 칼럼 그룹화
gender_grp=tips.groupby('gender')
gender_grp

# 그룹객체.함수()
# 각 그룹의 빈도수
gender_grp.size() # tips.groupby('gender').size()
'''
Female     87
Male      157
'''

# 그룹 통계량 : 숫자 변수만 대상
gender_grp.sum() # tips.groupby('gender').sum()
'''
        total_bill     tip  size   tips_pat
gender                                     
Female     1570.95  246.51   214  14.484694
Male       3256.82  485.07   413  24.751136
'''
gender_grp.mean() # tips.groupby('gender').mean()
'''
        total_bill       tip      size  tips_pat
gender                                          
Female   18.056897  2.833448  2.459770  0.166491
Male     20.744076  3.089618  2.630573  0.157651
'''

# 객체 -> 호출 가능한 멤버 확인
dir(gender_grp)

# 그룹별 요약통계량 : 숫자변수만 대상
gender_grp.describe() # R에서 summary
'''
       total_bill                       ...  tips_pat                    
            count       mean       std  ...       50%       75%       max
gender                                  ...                              
Female       87.0  18.056897  8.009209  ...  0.155581  0.194266  0.416667
Male        157.0  20.744076  9.246469  ...  0.153492  0.186240  0.710345
'''

gender_grp.boxplot() # descrobe 수치를 그래프로 제공
#@@1


# 2. 집단변수 1개 -> 특정 칼럼 그룹화
smoker_grp=tips['tip'].groupby(tips['smoker'])
smoker_grp.size() # 그룹 빈도수
'''
No     151
Yes     93
'''

smoker_grp.mean()
'''
No     2.991854
Yes    3.008710
'''

tips.info()


# 3. 집단변수 2개 -> 전체 칼럼 그룹화
# 형식) DF.groupby(['칼럼1', '칼럼2']) # 1차 : 칼럼1, 2차: 칼럼2
gender_smoker_grp = tips.groupby(['gender', 'smoker'])
# = tips.groupby([tips['gender'], tips['smoker']])

gender_smoker_grp.size()
'''
gender  smoker
Female  No        54
        Yes       33
Male    No        97
        Yes       60
'''
 
gender_smoker_grp.describe()
'''
              total_bill                       ...  tips_pat                    
                   count       mean       std  ...       50%       75%       max
gender smoker                                  ...                              
Female No           54.0  18.105185  7.286455  ...  0.149691  0.181630  0.252672
       Yes          33.0  17.977879  9.189751  ...  0.173913  0.198216  0.416667
Male   No           97.0  19.791237  8.726566  ...  0.157604  0.186220  0.291990
       Yes          60.0  22.284500  9.911845  ...  0.141015  0.191697  0.710345
'''

# 특정 변수(팁 지불금액) 통계량
gender_smoker_grp['tip'].describe()
'''
               count      mean       std   min  25%   50%     75%   max
gender smoker                                                          
Female No       54.0  2.773519  1.128425  1.00  2.0  2.68  3.4375   5.2
       Yes      33.0  2.931515  1.219916  1.00  2.0  2.88  3.5000   6.5
Male   No       97.0  3.113402  1.489559  1.25  2.0  2.74  3.7100   9.0
       Yes      60.0  3.051167  1.500120  1.00  2.0  3.00  3.8200  10.0
[해석] 여성은 흡연자가, 남성은 비흡연자가  팁 지불 금액이 더 크다.
'''


# 4. 집단변수 2개 -> 특정 칼럼 그룹화
gender_smoker_tip_grp = tips['tip'].groupby([tips['gender'], tips['smoker']])

''' error
gender_smoker_tip_grp = tips['tip'].groupby(tips['gender'], tips['smoker'])
gender_smoker_tip_grp = tips['tip'].groupby(['gender', 'smoker'])
'''

gender_smoker_tip_grp.size().shape

# 각 집단별 tip 합
gender_smoker_tip_grp.sum()

gender_smoker_tip_grp.sum().shape # (4, )

# 1차원 -> 2차원
grp_2d = gender_smoker_tip_grp.sum().unstack()
grp_2d # 성별 vs 흡연유무 -> 교차분할표(합계)
'''
smoker      No     Yes
gender                
Female  149.77   96.74
Male    302.00  183.07
'''

grp_1d = grp_2d.stack()
grp_1d
'''
gender  smoker
Female  No        149.77
        Yes        96.74
Male    No        302.00
        Yes       183.07
'''

# 성별 vs 흡연유무 -> 교차분할표(빈도수)
grp_2d_size = gender_smoker_tip_grp.size().unstack()
grp_2d_size
'''
smoker  No  Yes
gender         
Female  54   33
Male    97   60
'''

# iris dataset 그룹화
# 1) dataset load
iris = pd.read_csv("C:\\ITWILL\\4_Python-II\\data\\iris.csv")
iris.info()

# 2) group : group -> apply(sum)
iris.groupby('Species').sum()

iris['Sepal.Width'].groupby(iris['Species']).sum()
'''
setosa        171.4
versicolor    138.5
virginica     148.7
'''
























