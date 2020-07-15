# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:01:01 2020

@author: user
"""

import os
import re

import numpy as np
import pandas as pd

user_gr= pd.read_csv('C:/ITWILL/project/kakao_data/read_group.csv')
user_gr.head(20)

n_users = user_gr.user_id.unique().shape[0]
n_users # 306050

n_writers = user_gr.writer_id.unique().shape[0]
n_writers # 17452

ratings = np.zeros((n_users, n_writers))
ratings.shape #  (306050, 17452)


df = user_gr[['user_num', 'writer_num', 'count']]
df.head(20)


for row in df.itertuples() :
    ratings[row[1]-1, row[2]-1] =row[3]

ratings
'''
array([[1., 1., 1., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.],
       [1., 0., 0., ..., 0., 0., 0.],
       ...,
       [0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.]])
'''

ratings.shape # (306050, 17452)


from sklearn.model_selection import train_test_split
ratings_train, ratings_test = train_test_split(ratings, test_size = 0.5, random_state=45)


from sklearn.metrics.pairwise import cosine_distances

distance = 1-cosine_distances(ratings)
distance
# MemoryError: Unable to allocate 39.8 GiB for an array with shape (306050, 17452) and data type float64



