# -*- coding: utf-8 -*-
"""
< kNN 알고리즘 >
1. 알려진 범주로 알려지지 않은 범주 분류(해석 용이) 
2. 기존에 범주가 존재해야 함 - 식료품(과일, 채소, 단백질 등) 
3. 학습하지 않음 : 게으른 학습 
4. 결측치(NA)/이상치 전처리 중요 
5. 많은 특징을 갖는 데이터 셋은 부적합 
6. 유클리드 거리(Euclidean distance) 계산식 이용  
    - 가장 유사한 범주를 가장 가까운 거리로 선택
7. 적용 분야 
    - 개인별 영화 추천, 이미지/비디오에서 얼굴과 글자 인식, 유전자 데이터 패턴 식별(종양 식별)

    
"""
import numpy as np # 다차원배열, 선형대수 연산 
import matplotlib.pyplot as plt

# 1. 알려진 두 집단 x,y 산점도 시각화 
plt.scatter(1.2, 1.1) # A 집단
plt.scatter(1.0, 1.0)
plt.scatter(1.8, 0.8) # B 집단 
plt.scatter(2, 0.9)

plt.scatter(1.6, 0.85, color='r') # 분류대상 
plt.show()
#@@1


# 2. DATA 생성과 함수 정의 
p1 = [1.2, 1.1] # A 집단 
p2 = [1.0, 1.0]
p3 = [1.8, 0.8] # B 집단
p4 = [2, 0.9]
category = ['A','A','B','B'] # 알려진 집단 분류범주(Y변수)
p5 = [1.6, 0.85] # 분류대상 

# data 생성 함수 정의
def data_set():
    # 선형대수 연산 : numpy형 변환 (중첩리스트로 2차원)
    know_group = np.array([p1, p2, p3, p4]) # 알려진 집단 --2차원
    not_know_group = np.array(p5) # 알려지지 않은 집단--1차원
    class_category = np.array(category) # 정답(분류범주)
    return know_group,not_know_group,class_category 


know, not_know, cate = data_set()

know.shape # (4, 2)
not_know.shape #  (2,)
cate.shape # (4,)

























