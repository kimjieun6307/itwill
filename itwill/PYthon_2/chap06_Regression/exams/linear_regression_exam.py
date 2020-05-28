# -*- coding: utf-8 -*-
"""
문) california 주택가격을 대상으로 다음과 같은 단계별로 선형회귀분석을 수행하시오.
"""

# california 주택가격 데이터셋 
'''
캘리포니아 주택 가격 데이터(회귀 분석용 예제 데이터)

•타겟 변수
1990년 캘리포니아의 각 행정 구역 내 주택 가격의 중앙값

•특징 변수(8) 
MedInc : 행정 구역 내 소득의 중앙값
HouseAge : 행정 구역 내 주택 연식의 중앙값
AveRooms : 평균 방 갯수
AveBedrms : 평균 침실 갯수
Population : 행정 구역 내 인구 수
AveOccup : 평균 자가 비율
Latitude : 해당 행정 구역의 위도
Longitude : 해당 행정 구역의 경도
'''

from sklearn.datasets import fetch_california_housing # dataset load
import pandas as pd # DataFrame 생성 
from sklearn.linear_model import LinearRegression  # model
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import mean_squared_error, r2_score # model 평가 
import matplotlib.pyplot as plt 
import numpy as np

# 캘리포니아 주택 가격 dataset load 
california = fetch_california_housing()
print(california.DESCR)

# 단계1 : 특징변수와 타켓변수(MEDV)를 이용하여 DataFrame 생성하기   
X = california.data
y = california.target


df = pd.DataFrame(X, columns=california.feature_names)
df["MEDV"] = y
df
df.info()
'''
RangeIndex: 20640 entries, 0 to 20639
Data columns (total 9 columns):
'''

# 단계2 : 타켓변수와 가장 상관관계가 높은 특징변수 확인하기 => MedInc 
cor = df.corr()
cor['MEDV']
'''
MedInc        0.688075 ★행정 구역 내 소득의 중앙값
HouseAge      0.105623
AveRooms      0.151948
AveBedrms    -0.046701
Population   -0.024650
AveOccup     -0.023737
Latitude     -0.144160
Longitude    -0.045967
MEDV          1.000000
Name: MEDV, dtype: float64
'''


# 단계3 : california 데이터셋을 대상으로 1만개 샘플링하여 서브셋 생성하기  
'''
행번호 랜덤 선택(샘플 10000개)
#df.sample(10000)
idx = np.random.choice(a=len(data), size = 10000, replace=False)
'''
idx = np.random.choice(a=len(df), size = 10000, replace=False)
len(idx)

data = df.iloc[idx]
data
'''
data = df.sample(10000)
data
'''

# 단계4 : 75%(train) vs 25(test) 비율 데이터셋 split 
data_train, data_test = train_test_split(data)

col = list(data.columns)
len(col) # 9
x_col=col[:8]
'''
<참고> x_col=california.feature_names
'''
y_col=col[-1]


# 단계5 : 선형회귀모델 생성
ls = LinearRegression()
model = ls.fit(data_train[x_col], data_train[y_col])
'''
x변수 : 1~8 칼럼, y변수 : 9칼럼
model = ls.fit(data_train.iloc[:, :8], data_train[:, 8])
'''

# 단계6 : 모델 검정(evaluation)  : 예측력 검정, 과적합(overfitting) 확인  
train_acc = model.score(data_train[x_col], data_train[y_col])
test_acc = model.score(data_test[x_col], data_test[y_col])
'''
train_acc #  0.615508557005572
test_acc # 0.603519613998888
[해설] 훈련셋과 검정셋 모두 비슷한 분류정확도 -> 과적합 없음.
'''

# 단계7 : 모델 평가(test) 
# 조건1) 단계3의 서브셋 대상으로 30% 샘플링 자료 이용
# 조건2) 평가방법 : MSE, r2_score
y_pred = model.predict(data_test[x_col])
y_true = data_test[y_col]

mse = mean_squared_error(y_true, y_pred)
mse # 0.5639222733471806 (56% 오류율)

rscore = r2_score(y_true, y_pred)
rscore # 0.60351961399888 (60% 정확률)



# 단계8 : 예측치 100개 vs 정답 100개 비교 시각화 
a=np.array(y_true[:100])
b=y_pred[:100]

ab=pd.DataFrame(a,b)
ab
'''
1.625648  1.708
0.946050  0.738
1.747310  1.652
3.592283  3.932
2.167315  1.429
~~
'''
plt.plot(a, 'r', label='true')
plt.plot(b, 'b', label='pred')
plt.legend(loc = 'best')
#@@10












