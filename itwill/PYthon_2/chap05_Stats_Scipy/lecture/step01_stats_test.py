# -*- coding: utf-8 -*-
"""
< scipy 패키지의 확률분포 검정 >
- 연속형 확률분포 : "정규분포", 균등분포, 카이제곱, T-분포, F-분포, Z-분포
- 이산 확률분포 : 베르누이분포, "이항분포", 포아송분포(빈도수 희박한 확률)

1. 정규 분포 검정 : 연속변수의 확률분포
2. 이항 분포 검정 : 2가지 범주의 확률분포 (ex. 성공(1) vs 실패(0))
"""

from scipy import stats # 확률분포 검정
import numpy as np
import matplotlib.pyplot as plt # 히스토그램

# 1. 정규분포 검정 : 평균 중심 좌우 대칭성 검정
# stats.norm(mu, std).rvs(n)

# 1) 정규분포객체 생성
mu =0 ; std = 1 # 표준정규분포
std_norm = stats.norm(mu, std) # <정규분포객체 생성>
std_norm # 객체 정보 : <scipy.stats._distn_infrastructure.rv_frozen at 0x2ccf81b63c8>

# 2) 정규분포 확률변수
n=1000 # 시행횟수
norm_data = std_norm.rvs(n) # 시뮬레이션 : n개의 난수 생성
len(norm_data) # 1000
norm_data

# 3) 히스토그램 : 좌우 대칭성
plt.hist(norm_data) # 그림으로 좌우 대칭성 확인

# 4) 정규성 검정
'''
귀무가설(H0) : 정규분포와 차이가 없다.(정규분포와 동일하다.)
p-value >= 0.05 : 귀무가설 채택
'''
stats.shapiro(norm_data)
# (0.998534619808197, 0.5773680210113525)
'''
검정통계량 : 0.998534619808197   -> -1.96 ~ 1.96 : 채택역
p-value : 0.5773680210113525  >= 알파(0.05) : 채택역
[해설] 귀무가설 채택 : 정규분포와 차이가 없다.
'''
svalue, pvalue = stats.shapiro(norm_data)
print('검정통계량 : %.5f'%(svalue)) # 검정통계량 : 0.99853
print('p-value : %.5f'%(pvalue)) # p-value : 0.57737



# 2. 이항분포 검정 : 2가지(성공/실패) 범주의 확률분포 + 가설검정
'''
- 베르누이 분포 : 이항변수(두가지 범주(성공/실패)만 가지고 있는 변수)에서 성공이 나올 확률분포(모수 : 성공확률)
- 이상분포 : 베르누이 분포를 기반으로 시행횟수(n)를 적용한 확률분포(모수 : 성공확률(p), 시행횟수(n))

ex) 게임에 이길 확률 40%(p), 100번(n) 시행했을때 성공횟수 ?
'''
n=100 # 시행횟수
p=0.4 # 성공확률

# 1) 베르누이 분포(stats.bernoulli(p)) -> 이항분포 확률변수
x=stats.bernoulli(p).rvs(n) # 성공확률 40% -> 100번 시뮬레이션
x # 0(실패) or 1(성공)

# 2) 성공횟수
x_succ = np.count_nonzero(x)
print('성공횟수 : ', x_succ) # 성공횟수 :  33

# 3) 이항분포 검정 : 이항분포에 대한 가설검정
'''
귀무가설 : 게임에 이길 확률은 40%와 차이가 없다.(게임에 이길 확률이 40% 이다.)
'''
pvalue = stats.binom_test(x_succ, n, p, alternative='two-sided')
'''
#@@3
x : 성공횟수
n : 시행횟수
p : 성공확률
alternative='two-sided' : 양측검정
'''
pvalue # 0.18423369266065193

if pvalue >= 0.05 :
    print('게임에 이길 확률이 40%와 차이가 없다.')
else:
    print('게임에 이길 확률이 40%와 차이가 있다고 볼 수 있다.')
# 게임에 이길 확률이 40%와 차이가 없다.


'''
100명의 합격자 중에서 남자 합격자는 45일때
남여 합격률에 차이가 있다고 할 수 있는가?
n=100, x =45, p=0.5
귀무가설 : 남여 합격률에 차이가 없다.(p=0.5)
'''
pvalue = stats.binom_test(45, 100, 0.5, alternative='two-sided')
pvalue #  0.36820161732669654 >=0.05 : 남여 합격률에 차이가 없다.








