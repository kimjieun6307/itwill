# -*- coding: utf-8 -*-
"""
XGBoost model :  회귀트리(XGBRegressor)
"""

from xgboost import XGBRegressor # model
from xgboost import plot_importance # 중요변수 시각화
from sklearn.datasets import load_boston # 주택가격 데이터셋--회귀
from sklearn.model_selection import train_test_split # split
from sklearn.metrics import mean_squared_error, r2_score # 평가
import matplotlib.pyplot as plt # 데이터셋 시각화


# 1. dataset load
X, y = load_boston(return_X_y=True)
X.shape  # (506, 13)

y  # array([24. , 21.6, 34.7, 33.4, 36.2, --> 비율척도, 비정규화

boston = load_boston()
x_names = boston.feature_names
x_names
'''
array(['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD',
       'TAX', 'PTRATIO', 'B', 'LSTAT'], dtype='<U7')
'''


# 2. data split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


# 3. model
xgb = XGBRegressor()
model = xgb.fit(x_train, y_train)
model
'''
XGBRegressor(base_score=0.5, booster='gbtree', colsample_bylevel=1,
             colsample_bynode=1, colsample_bytree=1, gamma=0, gpu_id=-1,
             importance_type='gain', interaction_constraints='',
             learning_rate=0.300000012, max_delta_step=0, max_depth=6,
             min_child_weight=1, missing=nan, monotone_constraints='()',
             n_estimators=100, n_jobs=0, num_parallel_tree=1,
             objective='reg:squarederror', random_state=0, reg_alpha=0,
             reg_lambda=1, scale_pos_weight=1, subsample=1, tree_method='exact',
             validate_parameters=1, verbosity=None)

>> objective='reg:squarederror' 
'''

# 4. 중요변수 시각화
plot_importance(model)
#@@6
#model.get_booster.get_fscore() # AttributeError: 'function' object has no attribute 'get_fscore'
model.get_booster().get_fscore()
'''
{'f12': 304,
 'f5': 412,
 'f4': 179,
 'f0': 729,
 'f2': 124,
 'f7': 338,
 'f6': 362,
 'f11': 243,
 'f1': 60,
 'f9': 66,
 'f10': 77,
 'f8': 30,
 'f3': 16}
'''


x_names[0]  # 'CRIM'
x_names[5]  # 'RM'


# 5. model 평가
y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
mse  # 10.5547125151301

score = r2_score(y_test, y_pred)
score  #  0.869375095291496











