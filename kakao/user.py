# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:49:10 2020

@author: user
"""

from collections import Counter
from datetime import timedelta, datetime
import glob
from itertools import chain
import json
import os
import re

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import register_matplotlib_converters
# import seaborn as sns


# read.csv 파일 읽기
read= pd.read_csv('C:/ITWILL/project/kakao_data/read.csv')
read.head()

read.shape # (3507097, 4)

# 결측치 제거
read=read.dropna()
read.shape # (3502099, 4)

def chainer(s):
    return list(chain.from_iterable(s.str.split(' ')))

read_cnt_by_user = read['article_id'].str.split(' ').map(len)


read_raw = pd.DataFrame({'dt': np.repeat(read['dt'], read_cnt_by_user),
                         'hr': np.repeat(read['hr'], read_cnt_by_user),
                         'user_id': np.repeat(read['user_id'], read_cnt_by_user),
                         'article_id': chainer(read['article_id'])})
read_raw.head(20)
'''
         dt  hr                            user_id           article_id
0  20190122  19  #3d6d98f06ae6024da6e01af11f19dfcb   @seongheeleelrwn_2
0  20190122  19  #3d6d98f06ae6024da6e01af11f19dfcb    @thewatermelon_14
0  20190122  19  #3d6d98f06ae6024da6e01af11f19dfcb    @thewatermelon_27
0  20190122  19  #3d6d98f06ae6024da6e01af11f19dfcb  @thinkaboutlove_227
0  20190122  19  #3d6d98f06ae6024da6e01af11f19dfcb        @sabumbyun_29
0  20190122  19  #3d6d98f06ae6024da6e01af11f19dfcb         @taekangk_58
0  20190122  19  #3d6d98f06ae6024da6e01af11f19dfcb         @taekangk_44
1  20190122  19  #a7f157a8a3fa2cb934799b5943dc34a0          @brunch_133
2  20190122  19  #40a04d5f58e3eb86f249f099a1580b2c          @haereka_93
3  20190122  19  #65a8fb00713e0b5bb30f129794e49cfa             @shala_7
3  20190122  19  #65a8fb00713e0b5bb30f129794e49cfa         @cardnews_10
4  20190122  19  #cd221250949c3f97988d43d68decb744        @bang1999_467
4  20190122  19  #cd221250949c3f97988d43d68decb744        @bang1999_467
4  20190122  19  #cd221250949c3f97988d43d68decb744        @bang1999_468
5  20190122  19  #c9a1396bc73b39831353b2041a9d4e1b            @lofac_73
5  20190122  19  #c9a1396bc73b39831353b2041a9d4e1b            @lofac_73
5  20190122  19  #c9a1396bc73b39831353b2041a9d4e1b            @lofac_72
5  20190122  19  #c9a1396bc73b39831353b2041a9d4e1b            @lofac_72
5  20190122  19  #c9a1396bc73b39831353b2041a9d4e1b         @donghlim_13
5  20190122  19  #c9a1396bc73b39831353b2041a9d4e1b         @donghlim_13
'''
read_raw.shape # (22105708, 4)


# read_raw['cnt']=1

read_raw['article_id'].isnull().sum() # 0

len(read_raw['article_id']) # 22105708

from re import findall

article_id=[]
for i in read_raw['article_id']:   
    row = findall('\w{1,}_',i)
    article_id.extend(row)  
    
len(article_id) # 22105708

read_raw['writer_id']=article_id

# matrix = pd.pivot_table(read_raw, index=['user_id'], columns = ['article_id'], aggfunc='count')
# matrix = read_raw.pivot_table(index='user_id', columns='writer_id', values = 'cnt', aggfunc='count')
# index 1046224622 is out of bounds for axis 0 with size 1046217304
'''
matrix = pd.pivot_table(read_raw, index='user_id', columns='writer_id', values = 'cnt', aggfunc='count')
matrix.head(20)
'''
read_raw.info()
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 22105708 entries, 0 to 3507096
Data columns (total 5 columns):
 #   Column      Dtype 
---  ------      ----- 
 0   dt          int64 
 1   hr          int64 
 2   user_id     object
 3   article_id  object
 4   writer_id   object
'''

len(read_raw['writer_id'].unique()) # 17452
len(read_raw['user_id'].unique()) # 306050

306050*17452

user_df = read_raw[['user_id', 'writer_id', 'article_id']]
user_df.head()
'''
                             user_id         writer_id
0  #3d6d98f06ae6024da6e01af11f19dfcb  seongheeleelrwn_
0  #3d6d98f06ae6024da6e01af11f19dfcb    thewatermelon_
0  #3d6d98f06ae6024da6e01af11f19dfcb    thewatermelon_
0  #3d6d98f06ae6024da6e01af11f19dfcb   thinkaboutlove_
0  #3d6d98f06ae6024da6e01af11f19dfcb        sabumbyun_
'''
# user_onehot=pd.get_dummies(user_df, columns=['writer_id'])
# MemoryError: Unable to allocate 359. GiB for an array with shape (22105708, 17452) and data type uint8

user_df.shape # (22105708, 2)
# user_df.value_counts()
# np.array(user_df).value_counts()
'''
user_np = user_df.to_numpy()
user_np
user_np.shape
type(user_np)
user_np.values_counts()
'''
# user_df['writer_id'].apply(pd.value_counts())

user_gr = user_df.groupby(['user_id', 'writer_id'], as_index=False).count()
type(user_gr)
user_gr.columns=['user_id', 'writer_id', 'count']
user_gr.info()
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 6504359 entries, 0 to 6504358
Data columns (total 3 columns):
 #   Column     Dtype 
---  ------     ----- 
 0   user_id    object
 1   writer_id  object
 2   count      int64 
'''
user_gr.head(30)
'''
                              user_id         writer_id       count
0   #00001ba6ca8d87d2fc34d626ba9cfe6f           brunch_           1
1   #00001ba6ca8d87d2fc34d626ba9cfe6f       kecologist_           1
2   #00001ba6ca8d87d2fc34d626ba9cfe6f     swimmingstar_           1
3   #0000d1188f75d0b0ea7a8e23a2b760e5       hyunilikes_           1
4   #0000e87158c1426d6ffb72cebac6cb64        boosw1999_           1
5   #0000e87158c1426d6ffb72cebac6cb64           brunch_           1
6   #0000eea6d339abfd02ed590bc451fc63           sucopy_           1
7   #0000fdba8f35c76eacab74c5c6bc7f1a       4noramyeon_           1
8   #0000fdba8f35c76eacab74c5c6bc7f1a         hyunikun_           2
9   #0000fdba8f35c76eacab74c5c6bc7f1a          lazypic_           2
10  #0000fdba8f35c76eacab74c5c6bc7f1a      myolivenote_           1
11  #0000fdba8f35c76eacab74c5c6bc7f1a          ohj2660_           1
12  #0000fdba8f35c76eacab74c5c6bc7f1a          roysday_           1
13  #0000fdba8f35c76eacab74c5c6bc7f1a  studiocroissant_           1
14  #0000fdba8f35c76eacab74c5c6bc7f1a          tenbody_           2
15  #0000fdba8f35c76eacab74c5c6bc7f1a        yeonjikim_           2
16  #000127ad0f1981cae1292efdb228f0e9        dailylife_           1
17  #000127ad0f1981cae1292efdb228f0e9       seochogirl_          34
18  #000127ad0f1981cae1292efdb228f0e9   shanghaiesther_           1
19  #000127ad0f1981cae1292efdb228f0e9         syshine7_           1
'''
user_gr.shape # (6504359, 3)
user_gr.groupby(['count'])[['user_id']].count()
'''
       user_id
count         
1      3355577
2      1600989
3       428957
4       347220
5       134664
       ...
4212         1
4278         1
5158         1
5190         1
6922         1
'''
user_gr.groupby(['writer_id'])[['user_id']].count()
'''
                                   user_id
writer_id                                 
002_                                     6
002jesus_                                6
002paper_                                8
00700c454af49d5c9a36a13fcba01d0a_      614
008hood_                                14
                                   ...
zzumit_                                 15
zzyoun_                                152
zzz1004jang_                             1
zzzaam_                                244
zzzwhite_                                1
'''

n_users = user_gr.user_id.unique().shape[0]
n_users # 306050

n_writers = user_gr.writer_id.unique().shape[0]
n_writers # 17452

ratings = np.zeros((n_users, n_writers))
ratings.shape #  (306050, 17452)

for row in user_gr.itertuples() :
    ratings[row[1]-1, row[2]-1] =row[3]

ratings
#TypeError: unsupported operand type(s) for -: 'str' and 'int'

# user_id 숫자로 encoding
user_unique = user_gr.user_id.unique()
dict = {x : index +1 for index, x in enumerate(user_unique)}
user_gr['user_num'] = user_gr['user_id'].map(dict)
user_gr.head()

# writer_id 숫자로 encoding
writer_unique = user_gr.writer_id.unique()
dict2 = {x : index +1 for index, x in enumerate(writer_unique)}
user_gr['writer_num'] = user_gr['writer_id'].map(dict2)
user_gr.head()

user_gr.to_csv("C:/ITWILL/project/kakao_data/read_group.csv", index=None)

user_gr.user_num.unique().shape[0] # 306050
user_gr.writer_num.unique().shape[0] # 17452

df = user_gr[['user_num', 'writer_num', 'count']]
df.head(30)
'''
    user_num  writer_num  count
0          1           1      1
1          1           2      1
2          1           3      1
3          2           4      1
4          3           5      1
5          3           1      1
6          4           6      1
7          5           7      1
8          5           8      2
9          5           9      2
10         5          10      1
11         5          11      1
12         5          12      1
13         5          13      1
14         5          14      2
15         5          15      2
16         6          16      1
17         6          17     34
'''

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

from sklearn.metrics.pairwise import cosine_distances

distance = 1-cosine_distances(ratings)
distance
# MemoryError: Unable to allocate 39.8 GiB for an array with shape (306050, 17452) and data type float64

from sklearn.model_selection import train_test_split

ratings_train, ratings_test = train_test_split(ratings, test_size = 0.5, random_state=45)
                                 
