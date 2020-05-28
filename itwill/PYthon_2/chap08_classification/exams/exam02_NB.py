'''
문) weatherAUS.csv 파일을 시용하여 NB 모델을 생성하시오
  조건1> NaN 값을 가진 모든 row 삭제 
  조건2> 1,2,8,10,11,22,23 칼럼 제외 
  조건3> 7:3 비율 train/test 데이터셋 구성 
  조건4> formula 구성  = RainTomorrow ~ 나머지 변수(16개)
  조건5> GaussianNB 모델 생성 
  조건6> model 평가 : accuracy, confusion matrix, f1 score
'''
import pandas as pd
from sklearn.model_selection import train_test_split 

data = pd.read_csv('C:/ITWILL/4_Python-II/data/weatherAUS.csv')
print(data.head())
print(data.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 36881 entries, 0 to 36880
Data columns (total 24 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Date           36881 non-null  object 
 1   Location       36881 non-null  object 
 2   MinTemp        36543 non-null  float64
 3   MaxTemp        36639 non-null  float64
 4   Rainfall       36255 non-null  float64
 5   Evaporation    24035 non-null  float64
 6   Sunshine       23317 non-null  float64
 7   WindGustDir    33513 non-null  object 
 8   WindGustSpeed  33520 non-null  float64
 9   WindDir9am     34072 non-null  object 
 10  WindDir3pm     35919 non-null  object 
 11  WindSpeed9am   36219 non-null  float64
 12  WindSpeed3pm   36235 non-null  float64
 13  Humidity9am    36311 non-null  float64
 14  Humidity3pm    36370 non-null  float64
 15  Pressure9am    33309 non-null  float64
 16  Pressure3pm    33329 non-null  float64
 17  Cloud9am       24381 non-null  float64
 18  Cloud3pm       23899 non-null  float64
 19  Temp9am        36394 non-null  float64
 20  Temp3pm        36437 non-null  float64
 21  RainToday      36255 non-null  object 
 22  RISK_MM        36261 non-null  float64
 23  RainTomorrow   36261 non-null  object 
 '''
 

# 조건1> NaN 값을 가진 모든 row 삭제
data=data.dropna()
print(data.head())

# 조건2> 1,2,8,10,11,22,23 칼럼 제외 
col = list(data.columns)
for i in [1,2,8,10,11,22,23] :    
    col.remove(list(data.columns)[i-1])
print(col)
'''
['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine', 'WindGustSpeed', 
'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm', 'Pressure9am', 
'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am', 'Temp3pm', 'RainTomorrow']
'''

# 24 columns -> 17 columns
# dataset 생성 
new_data = data[col]
print(new_data.head())

# 조건3> 7:3 비율 train/test 데이터셋 구성
train_set, test_set = train_test_split(
new_data, test_size=0.3, random_state=0) # seed값 


# 조건4> formula 구성  = RainTomorrow ~ 나머지 변수(16개)
x_col=new_data.columns[:16] # [:-1]
y_col=new_data.columns[-1]

# 조건5> GaussianNB 모델 생성 
from sklearn.naive_bayes import GaussianNB

nb = GaussianNB()
model = nb.fit(train_set[x_col], train_set[y_col])
model

# 조건6> model 평가 : accuracy, confusion matrix, f1 score
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score

y_true = test_set[y_col]
y_pred = model.predict(test_set[x_col])

acc = accuracy_score(y_true, y_pred)
#  0.8051400076716533

con_mat = confusion_matrix(y_true, y_pred)
'''
array([[3391,  676],
       [ 340,  807]], dtype=int64)
'''
score = f1_score(y_true, y_pred, average='micro')
# 0.8051400076716534


score = f1_score(y_true, y_pred)
'''
ValueError: pos_label=1 is not a valid label: array(['No', 'Yes'], dtype='<U3')
'''
help(f1_score)









