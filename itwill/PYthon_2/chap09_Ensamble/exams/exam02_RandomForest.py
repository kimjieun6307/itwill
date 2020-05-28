'''
 문) 당료병(diabetes.csv) 데이터 셋을 이용하여 다음과 같은 단계로 
     RandomForest 모델을 생성하시오.

  <단계1> 데이터셋 로드
  <단계2> x,y 변수 생성 : y변수 : 9번째 칼럼, x변수 : 1 ~ 8번째 칼럼
  <단계3> 500개의 트리를 random으로 생성하여 모델 생성 
  <단계4> 5겹 교차검정/평균 분류정확도 출력
  <단계5> 중요변수 시각화 
'''

from sklearn.model_selection import train_test_split, cross_validate
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import matplotlib.pyplot as plt # 중요변수 시각화 
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 단계1. 테이터셋 로드  
dia = pd.read_csv('diabetes.csv', header=None) # 제목 없음  
print(dia.info()) 
print(dia.head()) 

# 단계2. x,y 변수 생성 
X = dia.iloc[:, :8]
X.shape
y=dia.iloc[:, -1]

# 단계3. model 생성
rf = RandomForestClassifier()
model = rf.fit(X, y)

# 단계4. 교차검정 model 예측/평가 
score = cross_validate(model, X, y, cv=7)
test_score=score['test_score']
test_score.mean() # 0.7510800446580264

# 단계5. 중요변수 시각화 
model.feature_importances_
'''
array([0.08154309, 0.25563534, 0.08673714, 0.07821175, 0.09001479,
       0.16908725, 0.12730778, 0.11146286])
'''

plt.barh(X.columns, model.feature_importances_)
#@@5

##########################
# model 변경
#######################

rf2 = RandomForestClassifier(criterion='entropy')
model2 = rf2.fit(X, y)
score2 = cross_validate(model2, X, y, cv=7, scoring='accuracy')
test_score2=score2['test_score']
test_score2.mean() #  0.753774088636474


from sklearn.svm import SVC
svc = SVC()
model3 = svc.fit(X, y)
score3 = cross_validate(model3, X, y, cv=7)
test_score3 = score3['test_score']
test_score3.mean() # 0.7629484005630794


from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()
model4 = dt.fit(X, y) 
score4 = cross_validate(model4, X, y, cv=7)
test_score4 = score4['test_score']
test_score4.mean() # 0.7062885296830251


from sklearn.tree.export import export_text
from sklearn import tree
tree.plot_tree(model4)
print(export_text(model4))
'''print(export_text(model4))
|--- feature_1 <= 0.28
|   |--- feature_5 <= -0.20
'''












