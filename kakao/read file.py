# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 14:46:36 2020

@author: user
"""
import pandas as pd
import os

import glob
read_file_lst = glob.glob('C:/ITWILL/project/kakao_data/read/read/*')


exclude_file_lst = ['read.tar']


read_df_lst = []
for f in read_file_lst:
    file_name = os.path.basename(f)
    if file_name in exclude_file_lst:
        print(file_name)
    else:
        df_temp = pd.read_csv(f, header=None, names=['raw'])
        df_temp['dt'] = file_name[:8]
        df_temp['hr'] = file_name[8:10]
        df_temp['user_id'] = df_temp['raw'].str.split(' ').str[0]
        df_temp['article_id'] = df_temp['raw'].str.split(' ').str[1:].str.join(' ').str.strip()
        read_df_lst.append(df_temp)


read = pd.concat(read_df_lst)

read.shape # (3507097, 5)
read.info()
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 3507097 entries, 0 to 1231
Data columns (total 5 columns):
 #   Column      Dtype 
---  ------      ----- 
 0   raw         object
 1   dt          object
 2   hr          object
 3   user_id     object
 4   article_id  object
'''

article = read['article_id'] 
article.head()

article[:3]
print(type(article))

article.to_csv("C:/ITWILL/project/kakao_data/article.csv", index=None, encoding='utf-8')






try : 
    file = open("C:/ITWILL/project/kakao_data/article.txt", mode='w', encoding='utf-8')
    for i in article[:3507097]:
        file.write(i)
    file.close()
    
except FileNotFoundError as e : 
    print('예외정보 : ', e)
    
finally : 
    pass
    




