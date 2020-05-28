# -*- coding: utf-8 -*-
"""
reshape : 차원변경 (ex. 1차원 -> 2차 -> n차)
- 선행 대수 연산 가능하게 하기 위해
"""
'''
1. image shape : 3차원(세로, 가로, 칼러)
2. reshape
'''
import numpy as np
from matplotlib.image import imread # image 읽기
import matplotlib.pylab as plt

# 1.image shape
file_path = './images/test1.jpg' # C:\ITWILL\4_Python-II\workspace\chap04_Numpy
image = imread(file_path)
type(image) # numpy.ndarray

image.shape # (360, 540, 3) --> (세로, 가로, 칼러)  # cf) 칼러 >> 1 : 흑백, 3 : 3원색
print(image) # 0~255
#@@1

# 이미지 보기
plt.imshow(image)
#@@2

# RGB 색상 분류
# [면, 행, 열] => [세로, 가로, 칼러]
r = image[:, :, 0] # Red
g = image[:, :, 1] # Green
b = image[:, :, 2] # Blue
r.shape # (360, 540)
g.shape
b.shape


# 2. image data reshape
from sklearn.datasets import load_digits # 데이타셋 제공
#@@3

digit = load_digits() # dataset loading
digit.DESCR # 설명보기
#@@4

x = digit.data # x변수(입력변수) : image
y = digit.target # y변수(정답 = 정수)

x.shape # (1797, 64) # 64 = 8x8
y.shape # (1797,)

img_0 = x[0].reshape(8,8) # 행index
img_0
#@@5

plt.imshow(img_0)
#@@6
# 이미지 형상 0

y[0] # 0 --> 정답 0

# 전체 이미지(-1) 1797를 8x8픽셀(64)로 reshape : (1797, 64) -> (1797, 8, 8)
x_3d = x.reshape(-1, 8, 8) 
x_3d.shape # (1797, 8, 8) -> (전체이미지, 세로픽셀, 가로픽셀, [칼러])

# 3차원(1797, 8, 8) -> 4차원 (1797, 8, 8, 1)
x_4d = x_3d[:,:,:,np.newaxis] # 4번째축 추가
x_4d.shape #  (1797, 8, 8, 1)


# 3. reshape
'''
 1) 전치행렬 : T, swapaxes() 
 2) transpose() : 3차원 이상 모양 변경
'''

# 1) 전치행렬 : T, swapaxes, swapaxes, transpose
data = np.arange(10).reshape(2,5)
'''
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])
'''
data.T
'''
array([[0, 5],
       [1, 6],
       [2, 7],
       [3, 8],
       [4, 9]])
'''

np.swapaxes(data, 0, 1)
'''
array([[0, 5],
       [1, 6],
       [2, 7],
       [3, 8],
       [4, 9]])
'''
data.swapaxes(0,1)
'''
array([[0, 5],
       [1, 6],
       [2, 7],
       [3, 8],
       [4, 9]])
'''
data.transpose()
'''
array([[0, 5],
       [1, 6],
       [2, 7],
       [3, 8],
       [4, 9]])
'''
np.transpose(data)
'''
array([[0, 5],
       [1, 6],
       [2, 7],
       [3, 8],
       [4, 9]])
'''


# 2) transpose()
'''
1차원 : 효과없음
2차원 : 전치행렬 동일함
3차원 : (0,1,2) -> (2,1,0)
'''
arr3d = np.arange(1,25).reshape(4,2,3)
arr3d.shape # (4, 2, 3)
arr3d
'''
array([[[ 1,  2,  3],
        [ 4,  5,  6]],

       [[ 7,  8,  9],
        [10, 11, 12]],

       [[13, 14, 15],
        [16, 17, 18]],

       [[19, 20, 21],
        [22, 23, 24]]])
'''

# (면, 행, 열) : (0,1,2) 축번호를 가지고 모양 변경
# (0,1,2) -> (2,1,0)
arr3d_tran = arr3d.transpose(2,1,0)
arr3d_tran.shape # (3, 2, 4)
arr3d_tran
'''
array([[[ 1,  7, 13, 19],
        [ 4, 10, 16, 22]],

       [[ 2,  8, 14, 20],
        [ 5, 11, 17, 23]],

       [[ 3,  9, 15, 21],
        [ 6, 12, 18, 24]]])
'''

#(0,1,2) -> (1,2,0)
arr3d_tran = arr3d.transpose(1,2,0)
arr3d_tran.shape # (2, 3, 4)
arr3d_tran
'''
array([[[ 1,  7, 13, 19],
        [ 2,  8, 14, 20],
        [ 3,  9, 15, 21]],

       [[ 4, 10, 16, 22],
        [ 5, 11, 17, 23],
        [ 6, 12, 18, 24]]])
'''



