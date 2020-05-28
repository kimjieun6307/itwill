# -*- coding: utf-8 -*-
"""
문) wine dataset을 이용하여 다음과 같이 다항분류 모델을 생성하시오. 
 <조건1> tree model 200개 학습
 <조건2> tree model 학습과정에서 조기 종료 100회 지정
 <조건3> model의 분류정확도와 리포트 출력   
"""
from xgboost import XGBClassifier # model
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine # 다항분류
from sklearn.metrics import accuracy_score, classification_report


#################################
## 1. XGBoost Hyper Parameter
#################################

# 1. dataset load
X, y = load_wine(return_X_y=True)
X.shape # (178, 13)

# 2. train/test 생성 
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

# 3. model 객체 생성 : tree model 200개 학습
xgb = XGBClassifier(n_estimators=200)

# 4. model 학습 조기종료 : 100회
model = xgb.fit(x_train, y_train, eval_set=[(x_test, y_test)], 
                eval_metric='merror', early_stopping_rounds=100, verbose=True)
'''
Stopping. Best iteration:
[2]     validation_0-merror:0.03704
'''
model
'''
XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
              colsample_bynode=1, colsample_bytree=1, gamma=0, gpu_id=-1,
              importance_type='gain', interaction_constraints='',
              learning_rate=0.300000012, max_delta_step=0, max_depth=6,
              min_child_weight=1, missing=nan, monotone_constraints='()',
              n_estimators=200, n_jobs=0, num_parallel_tree=1,
              objective='multi:softprob', random_state=0, reg_alpha=0,
              reg_lambda=1, scale_pos_weight=None, subsample=1,
              tree_method='exact', validate_parameters=1, verbosity=None)
'''

# 5. model 평가 : 분류정확도와 리포트 출력
y_pred = model.predict(x_test)
y_true = y_test
acc=accuracy_score(y_true, y_pred)
acc # 0.9629629629629629

report = classification_report(y_true, y_pred)
print(report)
'''
              precision    recall  f1-score   support

           0       0.88      1.00      0.93        14
           1       1.00      0.92      0.96        24
           2       1.00      1.00      1.00        16

    accuracy                           0.96        54
   macro avg       0.96      0.97      0.96        54
weighted avg       0.97      0.96      0.96        54
'''


