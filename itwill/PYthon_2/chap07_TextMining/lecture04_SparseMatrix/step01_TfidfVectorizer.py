# -*- coding: utf-8 -*-
"""
#@@ 2

TFiDF 단어 생성기 : TfidfVectorizer  
  1. 단어 생성기[word tokenizer] : 문장(sentences) -> 단어(word) 생성
  2. 단어 사전[word dictionary] : (word, 고유수치)
  3. 희소행렬[sparse matrix] : 단어 출현 비율에 의해서 가중치 적용[type-TF, TFiDF]
    1] TF : 가중치 설정 - 단어 출현 빈도수
    2] TFiDF : 가중치 설정 - 단어 출현 빈도수 x 문서 출현빈도수의 역수            
    - tf-idf(d,t) = tf(d,t) x idf(t) [d(document), t(term)]
    - tf(d,t) : term frequency - 특정 단어 빈도수 
    - idf(t) : inverse document frequency - 특정 단어가 들어 있는 문서 출현빈도수의 역수
       -> TFiDF = tf(d, t) x log( n/df(t) ) : 문서 출현빈도수의 역수(n/df(t))
"""

# 실습용 문장 생성
sentences = [
    "Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.",
    "Professor Plum has a green plant in his study.",
    "Miss Scarlett watered Professor Plum's green plant while he was away from his office last week."
]


#  1. 단어 생성기[word tokenizer]
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer() # object

tfidf
'''
TfidfVectorizer(analyzer='word', binary=False, decode_error='strict',
                dtype=<class 'numpy.float64'>, encoding='utf-8',
                input='content', lowercase=True, max_df=1.0, max_features=None,
                min_df=1, ngram_range=(1, 1), norm='l2', preprocessor=None,
                smooth_idf=True, stop_words=None, strip_accents=None,
                sublinear_tf=False, token_pattern='(?u)\\b\\w\\w+\\b',
                tokenizer=None, use_idf=True, vocabulary=None)
'''

# 2. 문장(sentences) -> 단어(word) 생성
tfidf_fit = tfidf.fit(sentences)
tfidf_fit
'''
TfidfVectorizer(analyzer='word', binary=False, decode_error='strict',
                dtype=<class 'numpy.float64'>, encoding='utf-8',
                input='content', lowercase=True, max_df=1.0, max_features=None,
                min_df=1, ngram_range=(1, 1), norm='l2', preprocessor=None,
                smooth_idf=True, stop_words=None, strip_accents=None,
                sublinear_tf=False, token_pattern='(?u)\\b\\w\\w+\\b',
                tokenizer=None, use_idf=True, vocabulary=None)
'''

# 3. 단어 사전[word dictionary] : (word, 고유수치)
vocs = tfidf_fit.vocabulary_ # 단어들  # <error> vocs = tfidf_fit.vocabulary
vocs # dict {'word1' : 고유숫자, 'word2' : 고유숫자}
'''{'mr': 14,
 'green': 5,
 'killed': 11,
 'colonel': 2,
 'mustard': 15,
 ~~
 '''
len(vocs) # 31

# 4. 희소행렬[sparse matrix] <-> 밀도행렬
sparse_mat = tfidf.fit_transform(sentences)  #[Doc x Terim])
type(sparse_mat)     # scipy.sparse.csr.csr_matrix                

sparse_mat # <3x31 sparse matrix of type '<class 'numpy.float64'>'
sparse_mat.shape # (3, 31) => 3개 문장, 31개 단어
print(sparse_mat)
'''
(row, col)       weight(tfidf)-가중치
(doc, word)      가중치
  (0, 3)        0.2205828828763741
  (0, 16)       0.2205828828763741
  (0, 25)       0.2205828828763741
  (0, 17)       0.2205828828763741
  (0, 10)       0.2205828828763741
  (0, 1)        0.2205828828763741
  (0, 30)       0.2205828828763741
  (0, 23)       0.1677589680512606
  (0, 24)       0.4411657657527482
~~
  (0, 14)       0.4411657657527482 -> 'mr'
'''

# scipy -> numpy
sparse_mat_arr = sparse_mat.toarray()
sparse_mat_arr
#@@3

















