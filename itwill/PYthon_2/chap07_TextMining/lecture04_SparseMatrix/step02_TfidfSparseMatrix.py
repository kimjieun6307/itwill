# -*- coding: utf-8 -*-
"""
1. csv file read
2. texts, target -> 전처리
3. max features
4. sparse matrix
"""

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer() 

import pandas as pd

# 1. csv file read

spam_data = pd.read_csv('../data/temp_spam_data.csv', encoding='utf-8', header=None)
spam_data
'''
      0                        1
0   ham    우리나라    대한민국, 우리나라 만세
1  spam      비아그라 500GRAM 정력 최고!
2   ham               나는 대한민국 사람
3  spam  보험료 15000원에 평생 보장 마감 임박
4   ham                   나는 홍길동
'''

target = spam_data[0]
texts = spam_data[1]

target # y변수
'''
0     ham
1    spam
2     ham
3    spam
4     ham
'''
texts # sparse matrix -> x변수
'''
0      우리나라    대한민국, 우리나라 만세
1        비아그라 500GRAM 정력 최고!
2                 나는 대한민국 사람
3    보험료 15000원에 평생 보장 마감 임박
4                     나는 홍길동
'''

# 2. texts, target -> 전처리
# 1) target 전처리 : ham/spam -> 0/1 dummy 변수
target = [0 if i=='ham' else 1 for i in target]
target # [0, 1, 0, 1, 0]

# 2) texts 전처리 : 
import string # text 전처리 

def text_prepro(texts):  # 문단(input) -> 문장(string) -> 음절 -> 문장
    # Lower case
    texts = [x.lower() for x in texts]
    # Remove punctuation (불용어 제거:, !)
    texts = [''.join(c for c in x if c not in string.punctuation) for x in texts]
    # Remove numbers (숫자제거)
    texts = [''.join(c for c in x if c not in string.digits) for x in texts]
    # Trim extra whitespace (공백 1칸)
    texts = [' '.join(x.split()) for x in texts]
    return texts

texts_re = text_prepro(texts)
texts_re


# 3. max features
# 사용한 x변수의 개수 (열의 차수)
tfidf_fit = tfidf.fit(texts_re) # 문장 -> 단어 생성
# tfidf_fit = TfidfVectorizer() .fit(texts_re)


vocs = tfidf_fit.vocabulary_  # 단어 사전
vocs
'''
{'우리나라': 9,
 '대한민국': 2,
 '만세': 4,
 '비아그라': 7,
 'gram': 0,
 '정력': 12,
 '최고': 13,
 '나는': 1,
 '사람': 8,
 '보험료': 6,
 '원에': 10,
 '평생': 14,
 '보장': 5,
 '마감': 3,
 '임박': 11,
 '홍길동': 15}
'''
max_features = len(vocs) # 16
'''
만약 max_features = 10 라고하면 16개 단어중 10개 단어만 이용
sparse maxtrix = [5 x 10]
'''

# 4. sparse matrix 
sparse_mat = tfidf.fit_transform(texts_re)  #[Doc x Terim])
sparse_mat  # <5x16 sparse matrix of type '<class 'numpy.float64'>'

# max_features 적용 예
max_features = 10

#sparse_mat = tfidf(max_features=max_features).fit_transform(texts_re) --TypeError: 'TfidfVectorizer' object is not callable
sparse_mat = TfidfVectorizer(max_features=max_features).fit_transform(texts_re)
sparse_mat # <5x10 sparse matrix of type '<class 'numpy.float64'>'
sparse_mat.shape # (5, 10)
print(sparse_mat)
'''
  (0, 4)        0.4206690600631704
  (0, 2)        0.3393931489111758
  (0, 9)        0.8413381201263408
  (1, 0)        0.7071067811865475
  (1, 7)        0.7071067811865475
  (2, 8)        0.6591180018251055
  (2, 1)        0.5317722537280788
  (2, 2)        0.5317722537280788
  (3, 3)        0.5773502691896258
  (3, 5)        0.5773502691896258
  (3, 6)        0.5773502691896258
  (4, 1)        1.0
'''

# scipy -> numpy
sparse_mat_arr = sparse_mat.toarray()
sparse_mat_arr  # x변수
'''
array([[0.        , 0.        , 0.33939315, 0.        , 0.42066906,
        0.        , 0.        , 0.        , 0.        , 0.84133812],
       [0.70710678, 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.        , 0.70710678, 0.        , 0.        ],
       [0.        , 0.53177225, 0.53177225, 0.        , 0.        ,
        0.        , 0.        , 0.        , 0.659118  , 0.        ],
       [0.        , 0.        , 0.        , 0.57735027, 0.        ,
        0.57735027, 0.57735027, 0.        , 0.        , 0.        ],
       [0.        , 1.        , 0.        , 0.        , 0.        ,
        0.        , 0.        , 0.        , 0.        , 0.        ]])
'''


'''
TfidfVectorizer
한글은 형태소 분석을 해주지 않음(영어는 형태소 분석 자동으로 됨)
공백을 기준으로 split하는 기능만
'''










