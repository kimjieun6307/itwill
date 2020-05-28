# -*- coding: utf-8 -*-
"""
Numpy package 특징
     - 선형 대수(벡터, 행렬) 연산 관련 함수 제공
     - list  보다 이점 :  N차원 배열 생성, 선형 대수 연산, 고속 처리
     - Series  공통점
         -> 수학 통계 함수 지원 obj.sum() ...
         -> 범위 수정, 블럭 연산
         -> indexing / slicing
     - 주요 모듈 / 함수
         1. random
         2. array : N 차원 배열 생성 array([list])
         3. sampling 함수
         4. arrange : range() 유사함
    - 차이점
"""

import numpy as np

lst = [1,2,3]

# list**2 #type error

for i in lst :
    print(i**2)
'''
1
4
9
'''

# list -> numpy
arr = np.array(lst)
arr # array([1, 2, 3])
arr**2 # array([1, 4, 9], dtype=int32)

# sam type -> 1(str)
arr=np.array([1,'two',3])
arr # array(['1', 'two', '3'], dtype='<U11')
arr.shape #(3,)

arr=np.array([[1,'two',3]])
arr # array([['1', 'two', '3']], dtype='<U11')
arr.shape # (1, 3)


# 1. random
data = np.random.randn(3,4) # module.module.function()
data
'''
array([[-0.58129024, -0.97894163, -0.93449339,  0.77976582],
       [-2.30427681,  2.45618575,  1.17871998,  0.47662655],
       [-0.04149182, -0.81460286, -1.18346156, -0.47161876]])
'''

for row in data :
    print(row.sum())
    print(row.mean())
'''
-1.714959439719153
-0.42873985992978825
1.8072554701742265
0.4518138675435566
-2.511175015636678
-0.6277937539091695
'''

# 1) 수학 통계 함수 지원
type(data) # numpy.ndarray
print("전체 합계", data.sum()) # 전체 합계 -2.4188789851816046
print("전체 평균", data.mean()) # 전체 평균 -0.20157324876513372
print("전체 분산", data.var()) # 전체 분산 1.4614462500819183
print("전체 표준편차", data.std()) # 전체 표준편차 1.2089029117683183

dir(data)
data.shape # (3,4)
data.size # 12

# 2) 범위 수정, 블럭 연산
data + data
'''
array([[-1.16258048, -1.95788326, -1.86898677,  1.55953163],
       [-4.60855361,  4.9123715 ,  2.35743996,  0.95325309],
       [-0.08298365, -1.62920573, -2.36692313, -0.94323753]])
'''
data - data
'''
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
'''

# 3) indexing
data[0,0] # 1행 1열 # -0.5812902395053829
data[0,:] # 1행 전체 # array([-0.58129024, -0.97894163, -0.93449339,  0.77976582])
data[:,1] # 2열 전체 # array([-0.97894163,  2.45618575, -0.81460286])

# 2. array 함수 : N차원 배열 생성
# list는 수학통계 함수 사용 못함. (but, numpy는 가능) 

# 1) 단일 list
lst1 = [3,5.6,4,7,8] 

# list -> array
arr1 = np.array(lst1)
arr1 # array([3, 5.6, 4, 7, 8])

arr1.var() # 3.4016000000000006

# 2) 중첩 list
lst2 = [[1,2,3,4,5],[2,3,4,5,6]]
lst2 # [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]
lst2[0][2] #  3

arr2 = np.array(lst2)
arr2
'''
array([[1, 2, 3, 4, 5],
       [2, 3, 4, 5, 6]])
'''

arr.shape # (1,3)
arr2[0,2] # 3
arr2[1,:] # 2행 전체 # array([2, 3, 4, 5, 6]) 
arr2[:,1] # 2열 전체 # array([2, 3])
arr2[:, 2:4]
'''
array([[3, 4],
       [4, 5]])
'''

# broadcast 연산
# - 작은 차원이 큰 차원이 늘어난 뒤 연산

# scala(0d) vs vector(1d)
arr1
0.5*arr1  # array([1.5, 2.8, 2. , 3.5, 4. ])

# scala(0d) vs matrix(2d)
arr2
0.5*arr2
'''
array([[0.5, 1. , 1.5, 2. , 2.5],
       [1. , 1.5, 2. , 2.5, 3. ]])
'''

# vector(1d) vs matrix(2d)
print(arr1.shape, arr2.shape) # (5,) (2, 5)

arr3 = arr1 + arr2
print(arr3)
'''
[[ 4.   7.6  7.  11.  13. ]
 [ 5.   8.6  8.  12.  14. ]]
'''

# 3. sampling function
num = list(range(1,11))
num # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
a : 관측치
size : 임의 추출 크기
replace : 복원 or 비복원
p : 확률
'''
idx = np.random.choice(a=len(num), size = 5, replace=False) # module.module.function
idx # array([7, 6, 1, 3, 5])

import pandas as pd

score = pd.read_csv("score_iq.csv")
score.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 6 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   sid      150 non-null    int64
 1   score    150 non-null    int64
 2   iq       150 non-null    int64
 3   academy  150 non-null    int64
 4   game     150 non-null    int64
 5   tv       150 non-null    int64
 '''

len(score) # 150
idx = np.random.choice(a=len(score), size = int(len(score)*0.3), replace=False)
idx
'''
array([147, 105,  68,  53,  87,  26,  39, 113,  97,  41,  90, 136,  67,
       108, 143, 122, 137,   4,  86,  63, 115,  77,  81,  35, 120,  36,
        64,  62, 142,   1, 119,   5, 116,  65,  58, 127,  44,  94,  69,
        27,  54,  96,  38, 126,  43])
'''
len(idx) # 45

# dataframe indexing : train set  선택
score_train = score.iloc[idx, :] # --> DF에서는 iloc 사용
score_train.shape # (45, 6)

# pandas(DF) -> numpy(array) : train set 선택
score_arr = np.array(score)
score_arr.shape #(150, 6)

score_train2 = score_arr[idx, :]
score_train2.shape # (45, 6)

# test set 선택
test_idx = [i for i in range(len(score)) if i not in idx]
len(test_idx)
score_test = score.iloc[test_idx , :]
score_test.shape # (105, 6)

# 4. arrange function
zero_arr = np.zeros((3,5))
zero_arr
'''
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
'''
cnt = 1
for i in range(3) :  # 행 index
    for j in range(5) :  # 열 index
        zero_arr[i,j] = cnt
        cnt+=1

zero_arr
'''
array([[ 1.,  2.,  3.,  4.,  5.],
       [ 6.,  7.,  8.,  9., 10.],
       [11., 12., 13., 14., 15.]])
'''

# range(-1.0, 2, 0.1) # TypeError: 'float' object cannot be interpreted as an integer
np.arange(-1.0, 2, 0.1)
'''
array([-1.00000000e+00, -9.00000000e-01, -8.00000000e-01, -7.00000000e-01,
       -6.00000000e-01, -5.00000000e-01, -4.00000000e-01, -3.00000000e-01,
       -2.00000000e-01, -1.00000000e-01, -2.22044605e-16,  1.00000000e-01,
        2.00000000e-01,  3.00000000e-01,  4.00000000e-01,  5.00000000e-01,
        6.00000000e-01,  7.00000000e-01,  8.00000000e-01,  9.00000000e-01,
        1.00000000e+00,  1.10000000e+00,  1.20000000e+00,  1.30000000e+00,
        1.40000000e+00,  1.50000000e+00,  1.60000000e+00,  1.70000000e+00,
        1.80000000e+00,  1.90000000e+00])
'''

