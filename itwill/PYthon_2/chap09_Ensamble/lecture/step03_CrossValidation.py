# -*- coding: utf-8 -*-
"""
교차검정(CrossValidation)
: 균등분할해서 교차검정
"""

from sklearn.datasets import load_digits # 다항분류 dataset
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_validate # split, 교차검정
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. dataset load
digits = load_digits()
X = digits.data
y = digits.target

X.shape #  (1797, 64)

import pandas as pd
pd.unique(y) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# 2. model
rf = RandomForestClassifier()
model = rf.fit(X, y)

pred = model.predict(X) # class 예측치

acc = accuracy_score(y, pred)
acc # 1.0

pred2 = model.predict_proba(X) # 확률예측치
pred2
'''
array([[1.  , 0.  , 0.  , ..., 0.  , 0.  , 0.  ],
       [0.  , 1.  , 0.  , ..., 0.  , 0.  , 0.  ],
       [0.  , 0.04, 0.81, ..., 0.  , 0.12, 0.  ],
       ...,
       [0.  , 0.05, 0.  , ..., 0.  , 0.93, 0.01],
       [0.  , 0.01, 0.  , ..., 0.  , 0.02, 0.95],
       [0.  , 0.02, 0.01, ..., 0.  , 0.91, 0.  ]])
'''
y  #  array([0, 1, 2, ..., 8, 9, 8]) --> 정답

# 확률값 -> index(10진수)
pred2_dit = pred2.argmax(axis=1)
pred2_dit # array([0, 1, 2, ..., 8, 9, 8], dtype=int64)

acc2 = accuracy_score(y, pred2_dit)
acc2 # 1.0


# 3. 교차검정(cross_validate)
score = cross_validate(model, X, y, scoring='accuracy', cv=5) #  cv=5 : 5겹으로 교차검정

score
'''{'fit_time': array([0.20197272, 0.20307732, 0.20564866, 0.20307612, 0.21869922]),
 'score_time': array([0.01562071, 0.01562095, 0.01563168, 0.        , 0.        ]),
 'test_score': array([0.93055556, 0.91666667, 0.95821727, 0.96100279, 0.93036212])}
'''
test_score = score['test_score']
test_score.mean() # 0.9393608789848343














