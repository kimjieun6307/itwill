'''
문) load_boston() 함수를 이용하여 보스턴 시 주택 가격 예측 회귀모델 생성 
  조건1> train/test - 7:3비울
  조건2> y 변수 : boston.target
  조건3> x 변수 : boston.data
  조건4> 모델 평가 : MSE, r2_score
'''

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import numpy as np
import pandas as pd

# 1. data load
boston = load_boston()
print(boston)


# 2. 변수 선택  
boston_x = boston.data
boston_y = boston.target

boston_x.shape # (506, 13)



# 3. train/test split
train_x, test_x, train_y, test_y = train_test_split(boston_x, boston_y, test_size=0.3)

train_x.shape # (354, 13)
506*0.7 # 354.2


# 4. 회귀모델 생성 : train set
obj = LinearRegression()
model = obj.fit(train_x, train_y)

# 5. 모델 평가 : test set
y_pred = model.predict(test_x)

from sklearn.metrics import mean_squared_error, r2_score

test_y.min() # 5.0
test_y.max() # 50.0
test_y.mean() # 21.63684210526316
# >> y 값이 정규화 되어 있지 않음 --> mse 평가법 사용 불가

mse = mean_squared_error(test_y, y_pred) #  23.262743871688656
rscore = r2_score(test_y, y_pred) # 0.6807318837570555 >> 68% 예측


# 상관계수 확인
df = pd.DataFrame({'y_treu' : test_y, 'y_pred' : y_pred})
df.corr() # 0.832174
'''
          y_treu    y_pred
y_treu  1.000000  0.832174
y_pred  0.832174  1.000000
'''


# 시각화
import matplotlib.pyplot as plt
type(test_y)
type(y_pred)

plt.plot(test_y, 'r', label='ture')
plt.plot(y_pred, 'b', label='pred')
plt.legend(loc='best')







