'''
외식업종 관련 data set 분석

문) food_df를 대상으로 다음과 같이 xgboost 모델을 생성하시오.
   <조건1> 6:4 비율 train/test set 생성 
   <조건2> y변수 ; 폐업_2년, x변수 ; 나머지 20개 
   <조건3> 중요변수에 대한  f1 score 출력
   <조건4> 중요변수 시각화  
   <조건5> accuracy와 model report 출력 
'''

import pandas as pd
from sklearn import model_selection, metrics
from sklearn.preprocessing import minmax_scale # 정규화 함수 
from xgboost import XGBClassifier # xgboost 모델 생성 
from xgboost import plot_importance # 중요변수 시각화  

# 중요변수 시각화 
from matplotlib import pyplot
from matplotlib import font_manager, rc # 한글 지원
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 외식업종 관련 data set
food = pd.read_csv("food_dataset.csv",encoding="utf-8",thousands=',')

# 결측치 제거
food=food.dropna()  
print(food.info())
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 68796 entries, 0 to 70170
Data columns (total 21 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   소재지면적        68796 non-null  float64
 1   위생업태명        68796 non-null  int64  
 2   주변           68796 non-null  int64  
 3   주변동종         68796 non-null  int64  
 4   기간평균         68796 non-null  float64
 5   pop          68796 non-null  float64
 6   bank         68796 non-null  float64
 7   nonbank      68796 non-null  float64
 8   tax_sum      68796 non-null  float64
 9   유동인구_주중_오전   68796 non-null  float64
 10  유동인구_주중_오후   68796 non-null  float64
 11  유동인구_주말_오전   68796 non-null  float64
 12  유동인구_주말_오후   68796 non-null  float64
 13  X1km_병원갯수    68796 non-null  float64
 14  X1km_초등학교갯수  68796 non-null  float64
 15  X3km_대학교갯수   68796 non-null  float64
 16  X1km_고등학교갯수  68796 non-null  float64
 17  X1km_중학교갯수   68796 non-null  float64
 18  X1km_영화관갯수   68796 non-null  float64
 19  X1km_지하철역갯수  68796 non-null  float64
 20  폐업_2년        68796 non-null  int64  
'''
 

#   <조건1> 6:4 비율 train/test set 생성 
train_set, test_set = model_selection.train_test_split(food, test_size = 0.4)

#   <조건2> y변수 ; 폐업_2년, x변수 ; 나머지 20개 
col = food.columns
x_col = col[:20]
y_col = col[-1]

food[y_col]

xgb = XGBClassifier()
model = xgb.fit(train_set[x_col], train_set[y_col])
model

#   <조건3> 중요변수에 대한  f1 score 출력
model.get_booster().get_fscore()
'''
{'소재지면적': 556,
 '주변': 351,
 'bank': 235,
 '기간평균': 455,
 'X1km_병원갯수': 141,
 'tax_sum': 194,
 '유동인구_주말_오전': 290,
 'pop': 229,
 'X1km_지하철역갯수': 94,
 '유동인구_주중_오후': 285,
 'X1km_초등학교갯수': 97,
 '주변동종': 220,
 'X1km_고등학교갯수': 92,
 'X1km_영화관갯수': 90,
 '위생업태명': 119,
 'X3km_대학교갯수': 115,
 '유동인구_주중_오전': 296,
 '유동인구_주말_오후': 297,
 'nonbank': 231}
'''

#   <조건4> 중요변수 시각화  
plot_importance(model)
#@@7

#   <조건5> accuracy와 model report 출력 
y_pred = model.predict(test_set[x_col])
y_true = test_set[y_col]

y_true.value_counts()
'''
0    21709
1     5810
'''


acc = metrics.accuracy_score(y_true, y_pred)
acc #  0.7880010174788328

report = metrics.classification_report(y_true, y_pred)
print(report)
'''
              precision    recall  f1-score   support

           0       0.80      0.98      0.88     21709
           1       0.49      0.07      0.13      5810
==> f1-score:  0일때 예측력이 88점으로 괜찮지만, 1일때 예측력은 13점으로 낮다. 
    accuracy                           0.79     27519
   macro avg       0.64      0.53      0.50     27519
weighted avg       0.73      0.79      0.72     27519
'''

