# -*- coding: utf-8 -*-


import numpy as np

# from module import function
# <현재 경로> C:\ITWILL\4_Python-II\workspace\chap08_classification
from step01_kNN_data import data_set


# dataset 생성
know, not_know, cate = data_set()
know.shape # (4, 2)
know
'''
array([[1.2, 1.1],
       [1. , 1. ],
       [1.8, 0.8],
       [2. , 0.9]])
'''
not_know # array([1.6 , 0.85])
cate # array(['A', 'A', 'B', 'B'], dtype='<U1')


# 거리 계산식 : 차(알려지지 않은 집단 - 알려진 집단)-> 제곱-> 합-> 제곱근
# (1) 차(알려지지 않은 집단 - 알려진 집단)
diff = not_know - know # 순서 상관 없음
diff
'''
array([[ 0.4 , -0.25],
       [ 0.6 , -0.15],
       [-0.2 ,  0.05],
       [-0.4 , -0.05]])
'''
# (2) 제곱 (부호 양수)
square_diff = diff**2
square_diff
'''
array([[0.16  , 0.0625],
       [0.36  , 0.0225],
       [0.04  , 0.0025],
       [0.16  , 0.0025]])
'''
# (3) 행단위 합계(axis=1) : 2차원 -> 1차원
sum_square_diff = square_diff.sum(axis = 1)
sum_square_diff
'''
array([0.2225, 0.3825, 0.0425, 0.1625])
'''
#(4) 제곱근
distance = np.sqrt(sum_square_diff)
distance
'''
array([0.47169906, 0.61846584, 0.20615528, 0.40311289])
'''
cate # ['A', 'A', 'B', 'B']
'''
거리가 가까운 k=3개 : 0.20615528->B, 0.40311289->B, 0.47169906->A
B : 2개, A : 1개 => B집단
'''

sortDist = distance.argsort()
sortDist # [2, 3, 0, 1]


result = cate[sortDist]
result # ['B', 'B', 'A', 'A']

# k=3 : 최근접 이웃 3개(홀수-vote 위해)
k3 = result[:3] # ['B', 'B', 'A']

# dict
classify_re = {}

for key in k3 : 
    classify_re[key] = classify_re.get(key, 0) + 1
    
classify_re # {'B': 2, 'A': 1}


vote_re = max(classify_re)
print('분류결과 : ', vote_re) # 분류결과 :  B


# kNN 알고리즘 함수 생성
def knn_classify(know, not_know, cate, k) : # 4개 파라미터
    # 단계1 : 거리계산식
    diff = know - not_know 
    square_diff = diff**2
    sum_square_diff = square_diff.sum(axis = 1)
    distance = np.sqrt(sum_square_diff)
    
    # 단계 2 : 오름차순 정렬 -> index
    sortDist = distance.argsort()
    
    # 단계 3 : 최근접 이웃(k=3)
    class_result = {}
    for i in range(k) : # k=3 (0~2)
        key = cate[sortDist[i]]
        class_result[key] = class_result.get(key, 0)+1 # 카테고리 빈도수 계산
    
    return class_result
        
        
# 함수 결과 확인
class_result = knn_classify(know, not_know, cate, 3)
class_result # {'B': 2, 'A': 1}
    
print('분류결과 : ', max(class_result, key=class_result.get)) # 분류결과 :  B


    
    
    








