# -*- coding: utf-8 -*-
"""
sklearn 관련 Linear Regression
"""
# 회귀모델의 객체를 만드는 class : LinearRegression 
from sklearn.linear_model import LinearRegression # model object
from sklearn.model_selection import train_test_split # train/test split
from sklearn.metrics import mean_squared_error, r2_score # model 평가
from sklearn.datasets import load_diabetes # 실습용 dataset

import numpy as np # 숫자처리
import pandas as pd # dataframe, 상관계수
import matplotlib.pyplot as plt # 회귀선 시각화

##########################
## diabetes
##########################
## 단순선형회귀 : x(1) -> y

# 1. dataset load
X, y = load_diabetes(return_X_y=True)
X.shape # (442, 10)
y.shape # (422, )

y.mean() # 152.13348416289594

data = load_diabetes()
print(data.DESCR)

# X(bmi : 비만도지수) -> y
x_bmi = X[:, 2]
x_bmi.shape #(422,)


# 3. model 생성 : object -> traing -> model
obj = LinearRegression() # 생성자 -> object
model = obj.fit(x_bmi, y) # (X, y) -> model
''' <error> 해당 모델에 적합한 차원으로 reshape해야함.
Reshape your data either using array.
reshape(-1, 1) if your data has a single feature or array.
reshape(1, -1) if it contains a single sample.
'''

# 1d -> 2d
x_bmi = x_bmi.reshape(442,1)
x_bmi.shape # (442, 1)

model = obj.fit(x_bmi, y)

# y 예측치
y_pred = model.predict(x_bmi)


# 4. model 평가 : MSE(y변수 정규화 되어 있으면 사용), r2_score(비정규화)
MSE = mean_squared_error(y, y_pred) # (y 정답, y 예측치)
rscore = r2_score(y, y_pred) # (y 정답, y 예측치)

#● MSE : 평균제곱오차 = mean((y_true - y_pred)**2) >> 오차률 (0기준)
print('MSE= ', MSE) 
# MSE=  3890.4565854612724 
# y변수가 정규화 되어있지 않아서 모델을 평가하기 적합하지 않다.
y.min() # 25.0
y.max() # 346.0
y.mean() # 152.13348416289594

#● r2_score: 결정계수(1 기준)
print('r2_score= ', rscore) 
# r2_score=  0.3439237602253803 
# >> 1에 가까울 적합한 모델임. (34% 예측력)




# 5. dataset split(7:3)
x_train, x_test, y_train, y_test = train_test_split(x_bmi, y, test_size=0.3)

x_train.shape # (309, 1)
442*0.7 # 309.4
x_test.shape # (133, 1)
442*0.3 # 132.6

# model 생성 
obj = LinearRegression()
model = obj.fit(x_train, y_train) # train dataset

y_pred = model.predict(x_test) # test dataset

# model 평가
MSE = mean_squared_error(y_test, y_pred)
rscore = r2_score(y_test, y_pred)

print('MSE= ', MSE) # MSE=  4152.793323323939
print('r2_score= ', rscore)  # r2_score=  0.2609051818898436

y_test[:10]
y_pred[:10]

# 상관계수 확인
import pandas as pd 

df = pd.DataFrame({'y_true' : y_test, 'y_pred' : y_pred})
df['y_true'].corr(df['y_pred']) # 0.5166701587703161


# 회귀선 시각화
import matplotlib.pyplot as plt 
plt.plot(x_test, y_test, 'ro') # 산점도
plt.plot(x_test, y_pred, 'b-') # 회귀선
#@@6


##################################
## iris
################################
# 다중회귀모델 : x(3) -> y

# 1. dataset load
iris = pd.read_csv("iris.csv")
iris.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Sepal.Length  150 non-null    float64  #--> y
 1   Sepal.Width   150 non-null    float64  #--> x1
 2   Petal.Length  150 non-null    float64  #--> x2
 3   Petal.Width   150 non-null    float64  #--> x3
 4   Species       150 non-null    object 
'''

# 2. 변수 선택
col = list(iris.columns)
col #  ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']

y_col = col[0]
x_col = col[1:-1] #  ['Sepal.Width', 'Petal.Length', 'Petal.Width']
col[1:4] #  ['Sepal.Width', 'Petal.Length', 'Petal.Width']

# 3. dataset split(기본값 : test_size = 0.25)
iris_train, iris_test = train_test_split(iris, test_size=0.3, random_state=123)
'''<train_test_split 파라미터 >
test_size : 검정데이터셋 비율(default = 0.25)
random_state : sampling seed값(매번 할때마다 샘플링 같게 할때)
'''
iris_train.shape # (105, 5)
150*0.7# 105.0
iris_test.shape # (45, 5)

iris_train.head()
'''
     Sepal.Length  Sepal.Width  Petal.Length  Petal.Width     Species
114           5.8          2.8           5.1          2.4   virginica
136           6.3          3.4           5.6          2.4   virginica
53            5.5          2.3           4.0          1.3  versicolor
19            5.1          3.8           1.5          0.3      setosa
38            4.4          3.0           1.3          0.2      setosa
'''
iris_test.head()


# 4. 모델 생성 : train data
lr = LinearRegression()
model = lr.fit(X=iris_train[x_col], y=iris_train[y_col])
model # 모델객체 정보
# LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)


# 5. 모델 평가 : test data
y_pred = model.predict(X=iris_test[x_col]) # 예측치
y_true = iris_test[y_col] # 관측치(정답)=label

y_true.min() # 4.3
y_true.max() # 7.9
y_true.mean() # 5.7822222222222
# y가 어느정도 정규화 됬다고 볼수 있다. >> MSE 평가법 사용 가능

mse = mean_squared_error(y_true, y_pred) 
# 0.11633863200224723 >> 0에 가까우면 가까울 수록 적합한 모델(대략 12% 오차율)

rscore = r2_score(y_true, y_pred) 
# 0.8546807657451759 >> 1에 가까우면 가까울 수록 예측 : 85%의 예측력을 보인다.


# 시각화 : y_true vs y_pred
import matplotlib.pyplot as plt

type(y_true) # pandas.core.series.Series
type(y_pred) # numpy.ndarray
# 동일한 타입으로 수정해서 시각화
y_true = np.array(y_true)

fig = plt.figure( figsize = (10, 5))
chart = fig.subplots()
chart.plot(y_true, color = 'b', label = 'real value')
chart.plot(y_pred, color = 'r', label = 'fitted value')
plt.legend(loc='best')
plt.show()
#@@7












                






