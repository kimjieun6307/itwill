'''
문1) score_iq.csv 데이터셋을 이용하여 단순선형회귀모델을 생성하시오.
   <조건1> y변수 : score, x변수 : academy      
   <조건2> 회귀모델 생성과 결과확인(회귀계수, 설명력, pvalue, 표준오차) 
   <조건3> 회귀선 적용 시각화 

'''

from scipy import stats
import pandas as pd
import statsmodels.formula.api as sm # ols


score_iq = pd.read_csv('score_iq.csv')
score_iq.info()

model = stats.linregress(score_iq['academy'], score_iq['score'])
model
'''
LinregressResult(slope=4.847829398324446, :기울기
intercept=68.23926884996192, y절편
rvalue=0.8962646792534938,  : 설명력
pvalue=4.036716755167992e-54, < 0.05 : 귀무가설 기각(유의하다) 
stderr=0.1971936807753301) : 표준오차
'''

x=score_iq.academy
y_pred = x*model.slope + model.intercept

import  matplotlib.pyplot as plt

plt.plot(score_iq.academy, score_iq.score, 'r.')
plt.plot(score_iq.academy, y_pred,'b')
plt.legend(loc='best')
#@@5


'''
   
문2) irsi.csv 데이터셋을 이용하여 다중선형회귀모델을 생성하시오.
   <조건1> 칼럼명에 포함된 '.' 을 '_'로 수정
   iris = pd.read_csv('../data/iris.csv')
   iris.columns = iris.columns.str.replace('.', '_')
   <조건2> y변수 : 1번째 칼럼, x변수 : 2~4번째 칼럼    
   <조건3> 회귀계수 확인 
   <조건4> 회귀모델 세부 결과 확인  : summary()함수 이용 
'''

iris = pd.read_csv('iris.csv')
iris.info()
iris.columns = iris.columns.str.replace('.', '_')

formula = "Sepal_Length ~ Sepal_Width + Petal_Length + Petal_Width"
model2 = sm.ols(formula, data = iris).fit()
model2.summary()
#@@6
'''
* 설명력 : Adj. R-squared:                  0.856
* Prob (F-statistic):           8.59e-62
* 귀무가설 기각 : 유의하다
* x변수 모두 y값에 영향을 미친다. 
* Petal_Length가 가장 강한 영향을 미치고 Petal_Width는 음의 영향을 미침
'''

# 회귀계수
model2.params
'''
Intercept       1.855997
Sepal_Width     0.650837
Petal_Length    0.709132
Petal_Width    -0.556483
'''

data = iris.iloc[:,:4]
data.head()
data.corr()
'''
              Sepal_Length  Sepal_Width  Petal_Length  Petal_Width
Sepal_Length      1.000000    -0.117570      0.871754     0.817941
Sepal_Width      -0.117570     1.000000     -0.428440    -0.366126
Petal_Length      0.871754    -0.428440      1.000000     0.962865
Petal_Width       0.817941    -0.366126      0.962865     1.000000
'''

plt.plot(model2.fittedvalues, 'r', label = 'true')
plt.plot(iris['Sepal_Length'], 'b', label = 'pred')
plt.legend(loc = 'best')
#@@7


