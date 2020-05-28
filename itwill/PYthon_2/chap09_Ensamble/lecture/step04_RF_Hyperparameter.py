# -*- coding: utf-8 -*-
"""
Random Forest Hyper Parameter
(Parameters)
    ----------
    n_estimators : integer, optional (default=100) : 트리 수 
    criterion : string, optional (default="gini") or 'entropy ' : 중요변수 선정
    max_depth : integer or None, optional (default=None) : 트리 깊이
    min_samples_split : int, float, optional (default=2) : 노드 분할 최소 샘플수
    min_samples_leaf : int, float, optional (default=1) : 단노드 분할 최소 샘플수
    max_features : int, float, string or None, optional (default="auto") : 최대 x변수 사용 수
    n_jobs : int or None, optional (default=None) : cpu 수
    random_state : int, RandomState instance or None, optional (default=None)
"""

from sklearn.ensemble import RandomForestClassifier # model
from sklearn.datasets import load_wine # dataset
from sklearn.metrics import accuracy_score

# 1. dataset load
wine = load_wine()
wine.feature_names # x변수명
'''
['alcohol',
 'malic_acid',
 'ash',
 'alcalinity_of_ash',
 'magnesium',
 'total_phenols',
 'flavanoids',
 'nonflavanoid_phenols',
 'proanthocyanins',
 'color_intensity',
 'hue',
 'od280/od315_of_diluted_wines',
 'proline']
'''

wine.target_names # y범주 이름 : ['class_0', 'class_1', 'class_2']

X = wine.data
y = wine.target

X.shape # (178, 13)


# 2. RF model
rf = RandomForestClassifier()
rf
'''
RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_weight=None,
                       criterion='gini', max_depth=None, max_features='auto',
                       max_leaf_nodes=None, max_samples=None,
                       min_impurity_decrease=0.0, min_impurity_split=None,
                       min_samples_leaf=1, min_samples_split=2,
                       min_weight_fraction_leaf=0.0, n_estimators=100,
                       n_jobs=None, oob_score=False, random_state=None,
                       verbose=0, warm_start=False)
'''
model = rf.fit(X, y)

# 3. Grid Search
from sklearn.model_selection import GridSearchCV

# 1) params 설정
# dict 형식 = {'Parameter' : params_range}
params = {'n_estimators' : [100, 200, 300, 400], 'max_depth':[3, 6, 8, 10], 
           'min_samples_split' : [2,3,4,5], 'min_samples_leaf' : [1,3,5,7]}


# 2) GridSearchCV 모델 객체
gs = GridSearchCV(estimator = model, param_grid = params, scoring = 'accuracy', cv=5, n_jobs=-1)
'''
scoring : 평가방법
cv : 교차검정
n_jobs : cpu 수 (-1 : cpu 전부)
#@@6
'''
model = gs.fit(X, y)

# best score
score = model.score(X, y)
score  # 1.0

# best parameter
model.best_params_ 
'''
{'max_depth': 8,
 'min_samples_leaf': 1,
 'min_samples_split': 4,
 'n_estimators': 200}
'''


