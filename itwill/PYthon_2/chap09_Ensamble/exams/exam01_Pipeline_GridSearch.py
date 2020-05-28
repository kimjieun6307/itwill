'''
 문) digits 데이터 셋을 이용하여 다음과 단계로 Pipeline 모델을 생성하시오.
  <단계1> dataset load
  <단계2> Pipeline model 생성
          - scaling : StndardScaler 클래스, modeing : SVC 클래스    
  <단계3> GridSearch model 생성
          - params : 10e-2 ~ 10e+2, 평가방법 : accuracy, 교차검정 : 5겹
          - CPU 코어 수 : 2개 
  <단계4> best score, best params 출력 
'''

from sklearn.datasets import load_digits # dataset 
from sklearn.svm import SVC # model
from sklearn.model_selection import GridSearchCV # gride search model
from sklearn.pipeline import Pipeline # pipeline
from sklearn.preprocessing import StandardScaler # dataset scaling
from sklearn.model_selection import train_test_split


# 1. dataset load
digits = load_digits()
X=digits.data
y=digits.target

# data 확인 : scaling 필요
X.min() # 0.0
X.max() # 16.0
 

x_train, x_test, y_train, y_test = train_test_split(X, y)



# 2. pipeline model : data 표준화 -> model 
# - scaling : StndardScaler 클래스, modeing : SVC 클래스

pipe_svc = Pipeline([('scaler',StandardScaler()), ('svc', SVC())])


# 3. gride search model 
'''        
  - params : 10e-2 ~ 10e+2, 평가방법 : accuracy, 교차검정 : 5겹
  - CPU 코어 수 : 2개
'''
help(SVC)

params = [0.01, 0.1, 1.0, 10.0, 100.0]
params_grid = [{'svc__C' : params, 'svc__kernel' : ['linear']}, 
               {'svc__C' : params, 'svc__kernel' : ['rbf'], 'svc__gamma' : params}]


gs = GridSearchCV(pipe_svc, params_grid, scoring='accuracy')
model = gs.fit(x_train, y_train)

'''
훈련 데이터와 검정 데이터는 pipele 모델 만들기 전에 나누는 건가?? 
그럼 표준화가 안된 데이턴데.. 상관없나..??

'''
model = gs.fit(X, y)

# 4. best score, best params

score = model.score(x_test, y_test)
score  # 0.97555555555555

model.best_score_
# 0.9829216577171966

model.best_params_
# {'svc__C': 10.0, 'svc__gamma': 0.01, 'svc__kernel': 'rbf'}

