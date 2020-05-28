# -*- coding: utf-8 -*-
"""
indexing / slicing
 - 1차원 indexing : list 동일함(차이 : 블럭수정, 사본수정->원본도 수정됨.)
 - 2, 3차 indexing : 2차원- 행index 기본 / 3차원 - 면index 기본
 - boolean indexing
"""

import numpy as np

# 1. indexing
'''
1차원 : obj[index]
2차원 : obj[행index, 열index]
3차원 : obj[면index, 행index, 열index]
'''

# 1) list 객체
ldata = [0,1,2,3,4,5]
ldata
ldata[:] # 전체 원소
ldata[2:] # [n:~] # [2, 3, 4, 5]
ldata[:3] # [~:n] # [0, 1, 2]
ldata[-1] # 5

# 2) numpy 객체
arrld = np.array(ldata)
arrld.shape #(6,)
arrld[2:] # array([2, 3, 4, 5])
arrld[:3] # array([0, 1, 2])
arrld[-1] # 5 


# 2. slicing
arr = np.array(range(1,11))
arr #  array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])

arr_sl = arr[4:8]
arr_sl # array([5, 6, 7, 8])

# 블럭 수정 (list 객체는 블럭 수정 안됨)
arr_sl[:] = 50
arr_sl # array([50, 50, 50, 50])

# ※ 사본(arr_sl)이 수정되면 원본(arr)도 수정됨.
arr # array([ 1,  2,  3,  4, 50, 50, 50, 50,  9, 10])


# 2.  2차원, 3차원 indexing
# np.array([[1행],[2행], ...])
arr2d = np.array([[1,2,3],[2,3,4],[3,4,5]])
arr2d.shape #(3,3)
arr2d
'''
array([[1, 2, 3],
       [2, 3, 4],
       [3, 4, 5]])
'''

# 행 index : default
arr2d[1] # arr2d[1,:]  # array([2, 3, 4])
arr2d[1:] # 2~3행
'''
array([[2, 3, 4],
       [3, 4, 5]])
'''
arr2d[:,1:] # 2~3열
'''
array([[2, 3],
       [3, 4],
       [4, 5]])
'''
arr2d[2,1] # 3행 2열 # 4
arr2d[:2, 1:]
'''
array([[2, 3],
       [3, 4]])
'''

# [면, 행, 열] : 면index, :default
# np.array([ [[]], [[]] ])
arr3d = np.array([ [[1,2,3], [2,3,4], [3,4,5]], 
                  [[2,3,4], [3,4,5], [6,7,8]] ]) # (2,3,3)

arr3d
'''
array([[[1, 2, 3],
        [2, 3, 4],
        [3, 4, 5]],

       [[2, 3, 4],
        [3, 4, 5],
        [6, 7, 8]]])
'''
arr3d.shape # (2, 3, 3)

arr3d[0] # 면index = 1면
'''
array([[1, 2, 3],
       [2, 3, 4],
       [3, 4, 5]])
'''
# 면 -> 행 index
arr3d[0,2] #  array([3, 4, 5])

# 면 -> 행 -> 열 index
arr3d[0, 2, 2] # 5

# box 선택
arr3d[1, 1:, 1:]
'''
array([[4, 5],
       [7, 8]])
'''

# 4. boolean indexing
dataset = np.random.randint(1, 10, 100) 
len(dataset) # 100

dataset
'''
array([3, 7, 4, 3, 8, 2, 8, 7, 9, 2, 4, 1, 3, 2, 1, 1, 5, 6, 9, 2, 5, 9,
       5, 4, 6, 9, 7, 2, 7, 6, 3, 2, 9, 4, 6, 5, 8, 1, 7, 3, 5, 1, 4, 3,
       8, 2, 7, 2, 8, 3, 5, 9, 3, 9, 9, 2, 3, 3, 3, 5, 4, 1, 3, 3, 5, 4,
       9, 2, 9, 4, 1, 3, 9, 9, 1, 9, 6, 6, 5, 1, 7, 6, 8, 7, 4, 5, 4, 8,
       8, 7, 6, 2, 6, 4, 7, 8, 9, 1, 9, 8])
'''

# 5이상 [관계식(>=)]
dataset2 = dataset[dataset >= 5]
len(dataset2) # 54

dataset2
'''
array([7, 8, 8, 7, 9, 5, 6, 9, 5, 9, 5, 6, 9, 7, 7, 6, 9, 6, 5, 8, 7, 5,
       8, 7, 8, 5, 9, 9, 9, 5, 5, 9, 9, 9, 9, 9, 6, 6, 5, 7, 6, 8, 7, 5,
       8, 8, 7, 6, 6, 7, 8, 9, 9, 8])
'''

# 5~8 자료 선택 [관계식 + 논리식(and)] >> error
# index에 논리식 쓸려면 np논리식 사용 해야 함.
# dataset[dataset >= 5 and dataset <=8] # Error : index에 논리식 못씀
np.logical_and
np.logical_or
np.logical_not

dataset2 = dataset[np.logical_and(dataset>=5, dataset <=8)]
dataset2
'''
array([7, 8, 8, 7, 5, 6, 5, 5, 6, 7, 7, 6, 6, 5, 8, 7, 5, 8, 7, 8, 5, 5,
       5, 6, 6, 5, 7, 6, 8, 7, 5, 8, 8, 7, 6, 6, 7, 8, 8])
'''








