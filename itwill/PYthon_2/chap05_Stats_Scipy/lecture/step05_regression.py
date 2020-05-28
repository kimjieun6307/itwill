# -*- coding: utf-8 -*-
"""
scipy 패키지의 stats 모듈의 함수
 - 통계적인 방식의 회귀분석 ( vs 기계학습 방식은 다음 chapter에서)
 1. 단순선형회귀모델
 2. 다중선형회귀모델
"""
from scipy import stats # 회귀모델 생성
import pandas as pd


# 1. 단순선형회귀모델
# x(iq) -> y(score)
score_iq = pd.read_csv("score_iq.csv")
score_iq.info()

# 변수 선택
x=score_iq.iq
y=score_iq['score']

# 회귀모델 생성
# from scipy import stats => stats.linregress()
model = stats.linregress(x, y)
model
'''
LinregressResult(slope=0.6514309527270075, => 기울기
intercept=-2.8564471221974657,  => 절편
rvalue=0.8822203446134699,      => 설명력
pvalue=2.8476895206683644e-50,  => x의 유의성 검정
stderr=0.028577934409305443)    => 표본 오차
'''
print('x의 기울기' , model.slope) # x의 기울기 0.6514309527270075
print('y의 절편', model.intercept) # y의 절편 -2.8564471221974657


score_iq.head()
'''
     sid  score   iq  academy  game  tv
0  10001     90  140        2     1   0
'''

# y=a*x +b
X=140
y_pred = X*model.slope + model.intercept
y_pred # 88.34388625958358

y = 90
err = y - y_pred
err # 1.6561137404164157


################
#product.csv
################
product = pd.read_csv("product.csv")
product.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 264 entries, 0 to 263
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   a       264 non-null    int64
 1   b       264 non-null    int64
 2   c       264 non-null    int64
'''

product.corr()
'''
          a         b         c
a  1.000000  0.499209  0.467145
b  0.499209  1.000000  0.766853
c  0.467145  0.766853  1.000000
'''
# b와 c는 비교적 높은 상관성을 가진다.

# x : 제품의 적절성 -> y : 제품만족도
model2 = stats.linregress(product['b'], product['c'])
model2
'''
LinregressResult(slope=0.7392761785971821, 
intercept=0.7788583344701907, 
rvalue=0.766852699640837, 
pvalue=2.235344857549548e-52, 
stderr=0.03822605528717565)
'''
product.head(1)
'''
   a  b  c
0  3  4  3
'''
x=4
y_pred = x *model2.slope + model2.intercept
y_pred
y= 3
err = (y-y_pred) **2
err # 0.5416416092857157 # (y-y_pred) = -0.7359630488589191


X = product['b']
y_pred = X * model2.slope + model2.intercept  # 예측치
Y= product['c']

len(y_pred) # 264
y_pred[:10]
Y[:10]


# ※ 회귀모델 시각화
from pylab import plot, legend, show

plot(product['b'], product['c'], 'b.') # (x, y) 산점도 => 파란색 점
plot(product['b'], y_pred, 'r.-') # 회귀선 => 빨강색 .- 모양 선
legend(['x, y scatter', 'regress model line'])
#@@1



# 2. 다중선행회귀모델 : y = x1 + x2 ...
from statsmodels.formula.api import ols # 모듈.모듈.모듈 안에 ols 함수

wine = pd.read_csv('winequality-both.csv')
wine.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6497 entries, 0 to 6496
Data columns (total 13 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   type                  6497 non-null   object 
 1   fixed acidity         6497 non-null   float64
 2   volatile acidity      6497 non-null   float64
 ~~
'''

# 칼럼명 변경(칼럼명에 공백 있어서)
wine.columns = wine.columns.str.replace(' ','_')
wine.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6497 entries, 0 to 6496
Data columns (total 13 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   type                  6497 non-null   object 
 1   fixed_acidity         6497 non-null   float64
 2   volatile_acidity      6497 non-null   float64
 ~~
'''
 
# quality vs other
cor = wine.corr()
cor['quality']
'''
fixed_acidity          -0.076743
volatile_acidity       -0.265699  -->★
citric_acid             0.085532
residual_sugar         -0.036980
chlorides              -0.200666  -->★
free_sulfur_dioxide     0.055463
total_sulfur_dioxide   -0.041385
density                -0.305858
pH                      0.019506
sulphates               0.038485
alcohol                 0.444319  -->★
quality                 1.000000
'''

# formula 생성(인수 넣기)
formula = "quality ~ alcohol + chlorides + volatile_acidity"

model = ols(formula, data = wine).fit()
model # ==> 객체 정보 제공
# <statsmodels.regression.linear_model.RegressionResultsWrapper at 0x1cf380aea08>

# 모델 분석 결과 확인 cf) R에서 summary(model)
model.summary()
#@@2
# Adj. R-squared:                  0.259 ==> 설명력
# F-statistic:                     758.6
# Prob (F-statistic):               0.00 < 0.05 : 귀무가설 기각(유의하다)
# x의 유의성 검정


# 멤버 호출 ex) 기울기, 절편
model.params #  기울기
'''
Intercept           2.909941
alcohol             0.319578
chlorides           0.159258
volatile_acidity   -1.334944
'''

# y의 예측치 vs 관측치
y_pred = model.fittedvalues # 예측치
y_true = wine['quality'] # 관측치

err = (y_true - y_pred) **2
err # 잔차
'''
0       0.000070
1       0.013768
2       0.001756
  ~~
6495    0.146759
6496    0.163060
'''

y_true.mean() # 5.818377712790519
y_pred.mean() # 5.81837771279059


# 차트 확인(시각화)
import matplotlib.pyplot as plt

plt.plot(y_true[:10], 'b', label='real values')
plt.plot(y_pred[:10], 'r', label='y_prediction')
plt.yticks(range(0,10))
plt.legend(loc = 'best')
#@@3


plt.plot(y_true[:50], 'b', label='real values')
plt.plot(y_pred[:50], 'r', label='y_prediction')
plt.legend(loc = 'best')
#@@4


