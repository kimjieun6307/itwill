# -*- coding: utf-8 -*-
"""
1. XGBoost Hyper Parameter
2. model 학습 조기 종료 : early stopping rounds
3. Best Hyper parameter : Grid Search
"""

from xgboost import XGBClassifier, XGBRegressor # model
from sklearn.datasets import load_breast_cancer # 이항분류에 적합한 데이터셋
from sklearn.model_selection import train_test_split # split
from sklearn.metrics import accuracy_score, classification_report # 평가


# 1. XGBoost Hyper Parameter 
X, y = load_breast_cancer(return_X_y=True)

X.shape # (569, 30)
y.shape # (569,)
y # (0, 1)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

xgb = XGBClassifier()
model = xgb.fit(x_train, y_train)
model
'''
XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
              colsample_bynode=1, colsample_bytree=1, gamma=0, gpu_id=-1,
              importance_type='gain', interaction_constraints='',
              learning_rate=0.300000012, max_delta_step=0, max_depth=6,
              min_child_weight=1, missing=nan, monotone_constraints='()',
              n_estimators=100, n_jobs=0, num_parallel_tree=1,
              objective='binary:logistic', random_state=0, reg_alpha=0,
              reg_lambda=1, scale_pos_weight=1, subsample=1,
              tree_method='exact', validate_parameters=1, verbosity=None)
'''
'''
1) colsample_bylevel=1 : 트리 모델 생성시 훈련셋의 샘플링의 비율(0.6~1)
2) learning_rate=0.300000012 : 학습율(0.01~0.1)
3) max_depth=6 : 트리의 깊이 - 데이터의 특성에 따라 스스로 결정 --> 클수록 과적합 영향
4) min_child_weight=1 : 자식 노드 분할을 결정하는 최소 가중치의 합 --> 클수록 과적합 영향
5) n_estimators=100 : 학습 트리모델 수
6) objective='binary:logistic' : y변수 자동 인식해서 자동으로 결정 --> 이항 vs 다항
'''

# 2. model 학습 조기 종료 : early stopping rounds
eval_set = [(x_test, y_test)]
model_early = xgb.fit(x_train, y_train, eval_set=eval_set, eval_metric='error', 
                      early_stopping_rounds=50, verbose=True)
'''
X, y : 훈련셋
eval_set : 모델 평가셋
eval_metric='error'  :  평가방법(이항분류:error, 다항:merror, 회귀:rmse) -> 오류율을 가지고 모델 평가 
early_stopping_rounds=50 : 학습 조기 종료 -> 50번까지 학습후 모델 성능 좋아지지 않으면 조기종료
verbose : 학습후 평가한 결과값 출력 여부 -> True(출력함)
'''
'''
Stopping. Best iteration:
[13]    validation_0-error:0.00531
'''
score = model_early.score(x_test, y_test)
score # 0.9946855624446412


# 3. Best Hyper parameter : Grid Search
from sklearn.model_selection import GridSearchCV


# default model object
xgb = XGBClassifier()

params = {'colsample_bylevel' : [0.6, 0.8, 1], 'learning_rate' : [0.01, 0.1, 0.5],
          'max_depth' : [3,5,7], 'min_child_weight' : [1,3,5], 'n_estimators' : [100, 300, 500]}

gs = GridSearchCV(estimator=xgb, param_grid=params, cv=5)

# 훈련셋 : x_train, x_test  평가셋: y_train, y_test
eval_set = [(x_test, y_test)]
model = gs.fit(x_train, y_train, eval_set=eval_set, eval_metric='error')

model.best_score_
# 0.9958238420652998

model.best_params_
'''
{'colsample_bylevel': 0.8,
 'learning_rate': 0.5,
 'max_depth': 3,
 'min_child_weight': 3,
 'n_estimators': 100}
'''












