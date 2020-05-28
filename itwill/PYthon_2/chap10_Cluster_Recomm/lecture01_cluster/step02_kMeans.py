# -*- coding: utf-8 -*-
"""
kMeans 알고지름
 - 비계층적(확인적) 군집분석
 - 군집수(k) 알고 있는 경우 이용
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans # model


# 1. dataset

# text file -> numpy
def dataMat(file) :
    dataset = [] # data mat 저장
    
    f = open(file, mode='r') # file object
    lines = f.readlines()  # ==> for i in f.readline() :
    for line in lines :
        cols = line.split('\t')
        
        rows =[] # x, y 저장
        for col in cols : 
            rows.append(float(col))
            
        dataset.append(rows) # [[rows], [rows], ... , [rows]]
    
    return np.array(dataset) # 2차원
    
dataset = dataMat('C:\\ITWILL\\4_Python-II\\data\\testSet.txt')
dataset.shape # (80, 2)
dataset[:5]       
'''
array([[ 1.658985,  4.285136],
       [-3.453687,  3.424321],
       [ 4.838138, -1.151539],
       [-5.379713, -3.362104],
       [ 0.972564,  2.924086]])
'''      
  
# numpy -> pandas
dataset_df = pd.DataFrame(dataset, columns = ['x', 'y'])

dataset_df.info()


# 2. kmeans model
kmeans = KMeans(n_clusters=4, algorithm='auto',)
kmeans
'''
KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
       n_clusters=4, n_init=10, n_jobs=None, precompute_distances='auto',
       random_state=None, tol=0.0001, verbose=0)
'''
model = kmeans.fit(dataset_df)

pred = model.predict(dataset_df)
pred # 0~3


# 3. 시각화
dataset_df['cluster']=pred
dataset_df.head()
'''
          x         y  cluster
0  1.658985  4.285136        3
1 -3.453687  3.424321        0
2  4.838138 -1.151539        1
3 -5.379713 -3.362104        2
4  0.972564  2.924086        3
'''

plt.scatter(x=dataset_df['x'], y=dataset_df['y'], c=dataset_df['cluster'], marker='o')
#@@4














