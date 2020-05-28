# -*- coding: utf-8 -*-
"""
<Naive Bayes 알고리즘>
1. 통계적 분류기  
    - 주어진 데이터가 특정 클래스에 속하는지를 확률을 통해서 예측  
    - 조건부 확률 이용 : P(B|A) 
2. 베이즈 확률 정리(Bayes’ theorem)을 적용한 기계학습 방법  
    - 두 확률 변수(사전 확률과 사후 확률) 사이의 관계를 나타내는 이론  
    - 사전확률 : 사건이 발생하기 전에 알려진 확률  
    - 사후확률 : 베이즈 이론에 근거한 확률 
3. 특정 영역에서는 DT나 kNN 분류기 보다 성능이 우수 
4. 텍스트 데이터 처럼 희소한 고차원인 경우 높은 정확도와 속도 제공 
5. 적용분야  
    - Spam 메일 분류, 문서(주제) 분류, 비 유무  
    - 컴퓨터 네트워크에서 침입자 분류(악성코드 유무)
"""

'''
NB모델
    GaussianNB : x변수가 실수형이고 정규분포 형태
    MultinomialNB : 희소행렬과 같은 고차원 데이터를 이용하여 다항분류
'''

import pandas as pd # csv file read
from sklearn.model_selection import train_test_split # split
from sklearn.naive_bayes import GaussianNB, MultinomialNB # model class
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score # model 평가

###########################
## GaussianNB
##########################

# 1. dataset load
iris = pd.read_csv("C:/ITWILL/4_Python-II/data/iris.csv")
iris.info()

# 정규성 검정 : 정규분포 형태 확인
from scipy import stats # 정규분포 검정

svalue, pvalue= stats.shapiro(iris['Sepal.Width']) #  0.10113201290369034
# (0.9849170446395874, 0.10113201290369034)

print('검정통계량 : %.5f'%(svalue)) #검정통계량 : 0.98492
print('p-value : %.5f'%(pvalue)) 
# p-value : 0.10113 > 0.05 : 귀무가설 채택(정규분포와 차이가 없다 = 동일하다)



# 2. x, y 변수 선택
cols=list(iris.columns)
cols # ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']

x_col = cols[:4]
y_col = cols[-1]


# 3. train/test split
train, test = train_test_split(iris, test_size=0.3, random_state=123)


# 4. NB model
nb = GaussianNB()
model = nb.fit(train[x_col], train[y_col])
model # GaussianNB(priors=None, var_smoothing=1e-09)


# 5. model 평가
y_pred = model.predict(test[x_col])
y_true = test[y_col]

acc = accuracy_score(y_true, y_pred) # 분류정확도
con_mat = confusion_matrix(y_true, y_pred) # 교차분할표
score= f1_score(y_true, y_pred, average='micro') # 불균형인 경우
'''
ValueError: Target is multiclass but average='binary'. 
Please choose another average setting, one of [None, 'micro', 'macro', 'weighted'].
'''

acc #  0.9555555555555556
con_mat
'''
array([[18,  0,  0],
       [ 0, 10,  0],
       [ 0,  2, 15]], dtype=int64)
'''
score # 0.9555555555555556



#####################################
## MultinomialNB
####################################

# C:\ITWILL\4_Python-II\workspace\chap06_Regression\sklearn_category_data.py

from sklearn.datasets import fetch_20newsgroups
newsgroups = fetch_20newsgroups(subset='all') # 'train', 'test'
# Downloading 20news dataset.
'''
- 20개의 뉴스 그룹 문서 데이터(문서 분류 모델 예문으로 사용)

•타겟 변수 
◦문서가 속한 뉴스 그룹 : 20개 

•특징 변수 
◦문서 텍스트 : 18,846
'''
print(newsgroups.DESCR)
'''
x변수 : new 기사 내용 (text 자료)
y변수 : 해당 news의 group(20개)
'''
newsgroups.target_names
'''
['alt.atheism',
 'comp.graphics',
 'comp.os.ms-windows.misc',
 'comp.sys.ibm.pc.hardware',
 'comp.sys.mac.hardware',
 'comp.windows.x',
 'misc.forsale',
 'rec.autos',
 'rec.motorcycles',
 'rec.sport.baseball',
 'rec.sport.hockey',
 'sci.crypt',
 'sci.electronics',
 'sci.med',
 'sci.space',
 'soc.religion.christian',
 'talk.politics.guns',
 'talk.politics.mideast',
 'talk.politics.misc',
 'talk.religion.misc']
'''
cats=newsgroups.target_names[:4]
cats
'''
['alt.atheism',
 'comp.graphics',
 'comp.os.ms-windows.misc',
 'comp.sys.ibm.pc.hardware']
'''


# 2. text -> sparse matrix : fetch_20newsgroups(subset='train')
news_train = fetch_20newsgroups(subset='train', categories=cats)
news_train.data # x변수로 사용할 text 자료
news_train.target # array([3, 2, 2, ..., 0, 1, 1], dtype=int64) --y변수

# sparse matrix
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
sparse_mat = tfidf.fit_transform(news_train.data)
sparse_mat.shape #  (2245, 62227)



# 3. model
nb = MultinomialNB()
model = nb.fit(X=sparse_mat, y=news_train.target)



# 4. model 평가 : fetch_20newsgroups(subset='test')
news_test = fetch_20newsgroups(subset='test', categories=cats)
news_test.data # text 
news_test.target #  array([1, 1, 1, ..., 1, 3, 3], dtype=int64)


sparse_test  = tfidf.transform(news_test.data)
sparse_test.shape # (1494, 62227)


'''
obj.fit_transform(train_data)
obj.transform(test_data)
'''


y_pred = model.predict(X=sparse_test)
y_true = news_test.target


acc = accuracy_score(y_true, y_pred) # 분류정확도
# 0.8520749665327979

con_mat = confusion_matrix(y_true, y_pred) # 교차분할표
'''
array([[312,   2,   1,   4],
       [ 12, 319,  22,  36],
       [ 16,  26, 277,  75],
       [  1,   8,  18, 365]], dtype=int64)
'''















