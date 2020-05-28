# -*- coding: utf-8 -*-
"""
pipeline : 자료 입력부터 모델생성까지 작업 과정
GridSerch : 최적의 하이퍼 파라미터 찾기

Pipeline vs Grid Search
 1. SVM model
 2. Pipeline : model workflow(dataset 전처리 -> model -> test)
 3. Grid Search
"""
from sklearn.datasets import load_breast_cancer # dataset
from sklearn.svm import SVC # model class
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler # scaling : 특정 x변수를 0~1 사이로 scaling
from sklearn.pipeline import Pipeline # model workflow
import numpy as np


# 1. SVM model Workflow

# 1) dataset load
X, y = load_breast_cancer(return_X_y=True)
X.shape # (569, 30)

# 열 단위 평균
X.mean(axis=0)
'''
array([1.41272917e+01, 1.92896485e+01, 9.19690334e+01, 6.54889104e+02,
       9.63602812e-02, 1.04340984e-01, 8.87993158e-02, 4.89191459e-02,
       1.81161863e-01, 6.27976098e-02, 4.05172056e-01, 1.21685343e+00,
       2.86605923e+00, 4.03370791e+01, 7.04097891e-03, 2.54781388e-02,
       3.18937163e-02, 1.17961371e-02, 2.05422988e-02, 3.79490387e-03,
       1.62691898e+01, 2.56772232e+01, 1.07261213e+02, 8.80583128e+02,
       1.32368594e-01, 2.54265044e-01, 2.72188483e-01, 1.14606223e-01,
       2.90075571e-01, 8.39458172e-02])
'''

X.min() #  0.0
X.max() # 4254.0


# 2) 전처리 :  X 변수 정규화 (MinMaxScaler)
scaler = MinMaxScaler().fit(X) # 1) scaler 객체
X_nor = scaler.transform(X) # 2) 정규화
X_nor.mean(axis=0)
'''
array([0.33822196, 0.32396512, 0.33293507, 0.21692009, 0.39478452,
       0.26060053, 0.20805838, 0.24313691, 0.37960537, 0.27037931,
       0.10634512, 0.18932404, 0.09937611, 0.06263579, 0.18111904,
       0.17443851, 0.08053969, 0.22345401, 0.17814345, 0.10019291,
       0.29666275, 0.36399849, 0.28313767, 0.1709062 , 0.40413785,
       0.22021232, 0.21740294, 0.39383582, 0.26330686, 0.18959607])
'''
X_nor.min() #  0.0
X_nor.max() # 1.0000000000000002

x_train, x_test, y_train, y_test = train_test_split(X_nor, y, test_size=0.3, random_state=123)


# 3) 모델생성 :  SVM model
svc = SVC(gamma='auto') 
model = svc.fit(x_train, y_train)

# 4) 모델 평가
score = model.score(x_test, y_test)
score # 0.9590643274853801


# 2. Pipeline : model workflow

# 1) pipeline step : [(step1), (step2), ...]
'''
step1 : 전처리 -> MinMaxScaler()
step2 : model 생성 -> svc model
'''
pipe_svc = Pipeline([('scaler', MinMaxScaler()), ('svc', SVC(gamma='auto'))])


# 2) pipeline model
model = pipe_svc.fit(x_train, y_train)


# 3) pipeline model test
score = model.score(x_test, y_test)
score # 0.9590643274853801



# 3. Grid Search : model turning
# pipeline -> Grid Search -> model turning

from sklearn.model_selection import GridSearchCV # 최적의 파라미터 찾는
help(SVC)
'''
class SVC(sklearn.svm._base.BaseSVC)
 |  SVC(C=1.0, kernel='rbf', degree=3, gamma='scale', coef0=0.0,  shrinking=True, 
 probability=False, tol=0.001, cache_size=200, class_weight=None, verbose=False, 
 max_iter=-1, decision_function_shape='ovr', break_ties=False, random_state=None)
'''

# 1) params 설정
params = [ 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]   # e-3 ~ e+3

# dict 형식 = {'객체명(object__C)' : params_range}
# (참고) pipe_svc = Pipeline([('svc', SVC(gamma='auto'))]) => 객체명 'svc'

params_grid = [{'svc__C' : params, 'svc__kernel':['linear']}, # 선형 파라미터 환경설정
               {'svc__C' : params, 'svc__gamma': params, 'svc__kernel' : ['rbf']}] # 비선형 파라미터 환경설정


# 2) GridSearchCV 모델 객체
gs = GridSearchCV(estimator = pipe_svc, param_grid = params_grid, scoring = 'accuracy', cv=10)
'''
scoring : 평가방법
cv : 교차검정
n_jobs : cpu 수
'''
model = gs.fit(x_train, y_train)

# best score
score = model.score(x_test, y_test)
score  # 0.9883040935672515 # 기존(score # 0.9590643274853801) 보다 높은 acc

# best parameter
model.best_params_   # {'svc__C': 1.0, 'svc__gamma': 1.0, 'svc__kernel': 'rbf'}


















