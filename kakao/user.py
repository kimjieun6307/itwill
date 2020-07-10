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
import seaborn as sns

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

user_df = read_raw[['user_id', 'writer_id']]
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

user_df1 = user_df.loc[:100000,]
user_df1

user_onehot=pd.get_dummies(user_df1, columns=['writer_id'])
user_onehot
'''
                                  user_id  ...  writer_id_zzzaam_
0       #3d6d98f06ae6024da6e01af11f19dfcb  ...                  0
0       #3d6d98f06ae6024da6e01af11f19dfcb  ...                  0
0       #3d6d98f06ae6024da6e01af11f19dfcb  ...                  0
0       #3d6d98f06ae6024da6e01af11f19dfcb  ...                  0
0       #3d6d98f06ae6024da6e01af11f19dfcb  ...                  0
                                  ...  ...                ...
100000  #f219a82520e825085417777cf05a1ff7  ...                  0
100000  #f219a82520e825085417777cf05a1ff7  ...                  0
100000  #f219a82520e825085417777cf05a1ff7  ...                  0
100000  #f219a82520e825085417777cf05a1ff7  ...                  0
100000  #f219a82520e825085417777cf05a1ff7  ...                  0
'''

user_df1['cnt']=1
'''
                                  user_id         writer_id  cnt
0       #3d6d98f06ae6024da6e01af11f19dfcb  seongheeleelrwn_    1
0       #3d6d98f06ae6024da6e01af11f19dfcb    thewatermelon_    1
0       #3d6d98f06ae6024da6e01af11f19dfcb    thewatermelon_    1
0       #3d6d98f06ae6024da6e01af11f19dfcb   thinkaboutlove_    1
0       #3d6d98f06ae6024da6e01af11f19dfcb        sabumbyun_    1
                                  ...               ...  ...
100000  #f219a82520e825085417777cf05a1ff7   raonjenatravel_    1
100000  #f219a82520e825085417777cf05a1ff7          hakgome_    1
100000  #f219a82520e825085417777cf05a1ff7          antyoon_    1
100000  #f219a82520e825085417777cf05a1ff7        bookdream_    1
100000  #f219a82520e825085417777cf05a1ff7        cswoo0625_    1
'''

matrix = user_df1.pivot_table(index='user_id', columns='writer_id', aggfunc='count')
matrix
'''
                                                                cnt  ...        
writer_id                         00700c454af49d5c9a36a13fcba01d0a_  ... zzzaam_
user_id                                                              ...        
#0001485b31e8f02c1ce117ceb4f41560                               NaN  ...     NaN
#0002531e4382c7f425e586552258ac64                               NaN  ...     NaN
#00040655eb357639383676e6342cc56e                               NaN  ...     NaN
#000474bba0c00c70e12ac7cfc3d04553                               NaN  ...     NaN
#000549d84169355d490b029755f99381                               NaN  ...     NaN
                                                            ...  ...     ...
#fffb7c053ee42209d7a9a38ec1cdbc6d                               NaN  ...     NaN
#fffcc9c67c1dfb2543eccdde30c19d6f                               NaN  ...     NaN
#fffd9342da9adb890ce65b994cd10e44                               NaN  ...     NaN
#fffe67ecc0056dd26ae00511957c5a2b                               NaN  ...     NaN
#ffff69451ff594425637015500410a13                               NaN  ...     NaN

[47023 rows x 10047 columns]
'''

type(matrix) #  pandas.core.frame.DataFrame


