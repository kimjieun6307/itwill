# -*- coding: utf-8 -*-

"""
1. XGBoost Hyper Parameter
2. model 학습 조기 종료 : early stopping rounds
3. Best Hyper parameter : Grid Search
"""

from xgboost import XGBClassifier, XGBRegressor # model
from sklearn.datasets import make_blobs # 다항분류
from sklearn.model_selection import train_test_split # split
from sklearn.metrics import accuracy_score, classification_report # 평가


# 1. XGBoost Hyper Parameter 
X, y = make_blobs(n_samples=2000, n_features=4, centers=3, cluster_std=2.5)
'''
def make_blobs(n_samples=100, --> 데이터셋 크기
 n_features=2,  --> x변수 
 centers=None,  --> y변수 범주(군집수) 
 cluster_std=1.0,  --> 클러스터 표준편차(클수록 오분류 커짐)
 center_box=(-10.0, 10.0), shuffle=True, random_state=None):
'''
X.shape  # (2000, 4)
y.shape  # (2000, )
y 

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

xgb = XGBClassifier(colsample_bynode=1, learning_rate=0.3, max_depth=3, 
                    min_child_weight=1, n_estimators=100)

model = xgb.fit(x_train, y_train)
model
'''
1) colsample_bylevel=1 : 트리 모델 생성시 훈련셋의 샘플링의 비율(0.6~1)
2) learning_rate=0.3 : 학습율(0.01~0.1)
3) max_depth=3 : 트리의 깊이 - 데이터의 특성에 따라 스스로 결정 --> 클수록 과적합 영향
4) min_child_weight=1 : 자식 노드 분할을 결정하는 최소 가중치의 합 --> 클수록 과적합 영향
5) n_estimators=100 : 학습 트리모델 수
objective='multi:softprob'
'''

# 2. model 학습 조기 종료 : early stopping rounds
eval_set = [(x_test, y_test)]
model_early = xgb.fit(x_train, y_train, eval_set=eval_set, eval_metric='merror', 
                      early_stopping_rounds=100, verbose=True)
'''
X, y : 훈련셋
eval_set : 모델 평가셋
eval_metric='error'  :  평가방법(이항분류:error, 다항:merror, 회귀:rmse) -> 오류율을 가지고 모델 평가 
early_stopping_rounds=50 : 학습 조기 종료 -> 50번까지 학습후 모델 성능 좋아지지 않으면 조기종료
verbose : 학습후 평가한 결과값 출력 여부 -> True(출력함)
'''

score = model_early.score(x_test, y_test)
score # 1.0


# 3. Best Hyper parameter : Grid Search
from sklearn.model_selection import GridSearchCV


# default model object
xgb = XGBClassifier()

params = {'colsample_bylevel' : [0.7, 0.9], 'learning_rate' : [0.01, 0.1],
          'max_depth' : [3,5], 'min_child_weight' : [1,3], 'n_estimators' : [100, 300]}

gs = GridSearchCV(estimator=xgb, param_grid=params, cv=5)

# 훈련셋 : x_train, x_test  평가셋: y_train, y_test
eval_set = [(x_test, y_test)]
model = gs.fit(x_train, y_train, eval_set=eval_set, eval_metric='merror', verbose=True)

model.best_score_
# 1.0

model.best_params_
'''
{'colsample_bylevel': 0.7,
 'learning_rate': 0.01,
 'max_depth': 3,
 'min_child_weight': 1,
 'n_estimators': 100}
'''













