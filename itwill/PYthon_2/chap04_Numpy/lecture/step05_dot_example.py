# -*- coding: utf-8 -*-
"""
신경망에서 행렬곱 적용 예
- 은닉층(h) = [입력(x) * 가중치(w)] + 편향(b)
"""
import numpy as np

# 1. ANN model
'''
input : image(28x28) --> 세로픽셀 28 x 가로픽셀 28 (칼러-흑백)
        hidden node : 32개 
-> weight[?, ?]
'''

# 2. input data : image data
28*28 #784
x_img = np.random.randint(0, 256, size = 784) # 0~255 난수
x_img.shape #(784, )
x_img.max() # 255

# <이미지 전처리 과정>
# 이미지 정규화(0~1) : 가장 큰 값으로 나누기
x_img = x_img/255
x_img.max() # 1.0

# 이미지 reshape
x_img2d = x_img.reshape(28, 28)
x_img2d.shape # (28, 28)

# 3. weigth data
weight = np.random.randn(28, 32) # 수일치 : 28개-->행, hidden node : 32개-->열 
weight
weight.shape # (28, 32)

# 4. hidden layer
hidden = np.dot(x_img2d, weight)
hidden.shape # (28, 32)



























