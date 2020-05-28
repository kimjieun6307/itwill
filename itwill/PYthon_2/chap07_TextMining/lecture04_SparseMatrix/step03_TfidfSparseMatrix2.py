# -*- coding: utf-8 -*-
"""
1. csv file read
2. texts, target -> 전처리
3. max features
4. sparse matrix
5. train/test split
6. binary file save
"""
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# 1. csv file read

spam_data = pd.read_csv('../data/temp_spam_data2.csv', encoding='utf-8', header=None)
spam_data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5574 entries, 0 to 5573
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   0       5574 non-null   object
 1   1       5574 non-null   object
'''
target = spam_data[0]
texts = spam_data[1]

target # y변수
'''
0        ham
1        ham
2       spam
~~
5572     ham
5573     ham
'''
texts # sparse matrix -> x변수
'''
0       Go until jurong point, crazy.. Available only ...
1                           Ok lar... Joking wif u oni...
~~
5572    The guy did some bitching but I acted like i'd...
5573                           Rofl. Its true to its name
'''

# 2. texts, target -> 전처리
# 1) target 전처리 : ham/spam -> 0/1 dummy 변수
target = [0 if i=='ham' else 1 for i in target]
target # [0, 1, 0, 1, 0]

# 2) texts 전처리 생략 : 영문이라서



# 3. max features :  x변수의 개수 (열의 차수)
tfidf_fit = TfidfVectorizer().fit(texts) # 문장 -> 단어 생성
vocs = tfidf_fit.vocabulary_  # 단어 사전
len(vocs) # 8722

max_features = 4000
'''
전체 단어 8,722 중에서 4,000개 단어 이용 열의 차수로 사용
sparse maxtrix = [5574 x 4000]
'''

# 4. sparse matrix 
# max_features 적용
sparse_mat = TfidfVectorizer(stop_words='english', max_features=max_features).fit_transform(texts)
sparse_mat 
'''
<5574x4000 sparse matrix of type '<class 'numpy.float64'>'
	with 39080 stored elements in Compressed Sparse Row format>
'''
print(sparse_mat)
'''
  (0, 3827)     0.22589839945445928
  (0, 1640)     0.18954016110208324
  (0, 919)      0.3415462652078248
  (0, 771)      0.3859368913710106
  (0, 2038)     0.3415462652078248
  (0, 3928)     0.2734743380749632
  (0, 1655)     0.22333592678188377
  (0, 772)      0.3415462652078248
  (0, 569)      0.30239798556416847
  (0, 1062)     0.31309653053925
  (0, 2721)     0.3162190279124655
~~
'''


# scipy -> numpy
sparse_mat_arr = sparse_mat.toarray()
sparse_mat_arr  # x변수
'''
array([[0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.],
       ...,
       [0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.],
       [0., 0., 0., ..., 0., 0., 0.]])
'''



# 5. train/test split
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(sparse_mat_arr, target, test_size = 0.3)

x_train.shape  # (3901, 4000)
5574*0.7  # 3901.7999999999997
x_test.shape # (1673, 4000)


# 6. numpy binary file save
import numpy as np

spam_data_split= (x_train, x_test, y_train, y_test) # 튜플타입으로 저장
np.save('../data/spam_data', spam_data_split) # allow_pickle=True
# numpy형으로 저장하면 확장자 자동 생성 spam_data.npy

# file load : allow_pickle=True
# 현재 경로 (C:\ITWILL\4_Python-II\workspace\chap07_TextMining\data)
x_train2, x_test2, y_train2, y_test2 = np.load('spam_data.npy', allow_pickle=True)
x_train2.shape # (3901, 4000)



















