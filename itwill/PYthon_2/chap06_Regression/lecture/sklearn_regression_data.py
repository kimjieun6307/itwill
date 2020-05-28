'''
분류용 sklearn dataset 정리 
'''
from sklearn import datasets # dataset 제공 library
import numpy as np


######################################
# 선형회귀분석에 적합한 데이터셋
######################################

# 1. iris 
#   : 선형회귀분석, 분류분석 적합
'''
붓꽃(iris) 데이터
붓꽃 데이터는 통계학자 피셔(R.A Fisher)의 붓꽃의 분류 연구에 기반한 데이터
•타겟 변수
◦setosa, versicolor, virginica의 세가지 붓꽃 종(species)
•특징 변수(4)
◦꽃받침 길이(Sepal Length)
◦꽃받침 폭(Sepal Width)
◦꽃잎 길이(Petal Length)
◦꽃잎 폭(Petal Width)
'''
iris = datasets.load_iris() # Load the data
print(iris) 
print(iris.DESCR) # dataset 설명제공 : 변수특징, 요약통계 
#@@1
print(iris.data) # x변수 
print(iris.target) # y변수(target)

x=iris.data
y=iris.target
type(x) # numpy.ndarray
x.shape # (150, 4)
y.shape # (150, )

iris.feature_names # x변수 이름
'''
['sepal length (cm)',
 'sepal width (cm)',
 'petal length (cm)',
 'petal width (cm)']
'''
iris.target_names # y의 값
# array(['setosa', 'versicolor', 'virginica'], dtype='<U10')

# numpy -> DataFrame 
import pandas as pd
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df.info() 
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
'''

# class -> 문자이름
tg = pd.Series(iris.target, dtype="category") # 집단변수  
tg = tg.cat.rename_categories(iris.target_names) # 카테고리 이름 변경 
#@@3

iris_df['species'] = tg # target 추가 
iris_df.head()
iris_df.info() 
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column             Non-Null Count  Dtype   
---  ------             --------------  -----   
 0   sepal length (cm)  150 non-null    float64 
 1   sepal width (cm)   150 non-null    float64 
 2   petal length (cm)  150 non-null    float64 
 3   petal width (cm)   150 non-null    float64 
 4   species            150 non-null    category
 '''

# 차트 분석 : 각 특징별 타겟변수의 분포현황  
import seaborn as sn
import matplotlib.pyplot as plt

# 변수 간 산점도 : hue = 집단변수 : 집단별 색상 제공 
sn.pairplot(iris_df, hue="species")
plt.show() 
#@@4
# 연속형 변수가 여러개 있으면 산점도를 통해

# 타겟변수(집단)별 특징 분포현황   
sn.distplot(iris_df[iris_df.species == "setosa"]["petal length (cm)"], label="setosa")
sn.distplot(iris_df[iris_df.species != "setosa"]["petal length (cm)"], label="others")
plt.legend() # 범례
plt.show()
#@@5


# 2. 당료병 데이터셋
'''
442명의 당뇨병 환자를 대상으로한 검사 결과를 나타내는 데이터

•타겟 변수 => y 변수
1년 뒤 측정한 당료병 진행상태 정량적화 자료(연속형)

•특징 변수(10: 모두 정규화된 값) => x변수
age : 나이 (세)
sex : 성별 
bmi : 비만도지수
bp : 평균혈압(Average blood pressure)
S1 ~ S6: 기타 당료병에 영향을 미치는 요인들 
'''

diabetes = datasets.load_diabetes() 
print(diabetes.DESCR) # 컬럼 설명, url
'''
:Target: Column 11 -> 1년기준으로 질병 진행상태를 정량적(연속형)으로 측정 
:Attribute Information: Age ~ S6
''' 
   
print(diabetes.target_names) # None : target 연속형 
# .target_names 이 있다는 것은 범주형 이라는 것.

print(diabetes.feature_names)
# ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']

# ● data load할때 한번에 x, y를 바로 load하는 방법
X, y = datasets.load_diabetes(return_X_y=True)

print(np.shape(X)) # (442, 10) : matrix
print(np.shape(y)) # (442,) : vector
y.mean() # 152.13348416289594
y.min() # 25.0
y.max() # 346.0



# 3. boston 주택가격 
'''
보스턴 주택 가격 데이터(회귀 분석용 예제 데이터)

•타겟 변수
1978 보스턴 주택 가격: 506개 타운의 주택 가격 중앙값(단위 1,000 달러)
•특징 변수(13)
CRIM: 범죄율
INDUS: 비소매상업지역 면적 비율
NOX: 일산화질소 농도
RM: 주택당 방 수
LSTAT: 인구 중 하위 계층 비율
B: 인구 중 흑인 비율
PTRATIO: 학생/교사 비율
ZN: 25,000 평방피트를 초과 거주지역 비율
CHAS: 찰스강의 경계에 위치한 경우는 1, 아니면 0
AGE: 1940년 이전에 건축된 주택의 비율
RAD: 방사형 고속도로까지의 거리
DIS: 직업센터의 거리
TAX: 재산세율
'''

boston = datasets.load_boston()
print(boston)
print(boston.DESCR)
print(boston.target_names) # None : target 연속형 

boston_x = boston.data # 4개 columns
boston_y = boston.target

print(np.shape(boston_x)) # (506, 13) : matrix
print(np.shape(boston_y)) # (506,) : vector

type(boston_x) # numpy.ndarray
type(boston) # sklearn.utils.Bunch



# 4. california 주택가격 
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
from sklearn.datasets import fetch_california_housing
california = fetch_california_housing()
print(california.DESCR)

cal_df = pd.DataFrame(california.data, columns=california.feature_names)
cal_df["MEDV"] = california.target

cal_df.info() 
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20640 entries, 0 to 20639
Data columns (total 9 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   MedInc      20640 non-null  float64
 1   HouseAge    20640 non-null  float64
 2   AveRooms    20640 non-null  float64
 3   AveBedrms   20640 non-null  float64
 4   Population  20640 non-null  float64
 5   AveOccup    20640 non-null  float64
 6   Latitude    20640 non-null  float64
 7   Longitude   20640 non-null  float64
 8   MEDV        20640 non-null  float64
 '''
 
cal_df.tail()
'''
       MedInc  HouseAge  AveRooms  ...  Latitude  Longitude   MEDV
20635  1.5603      25.0  5.045455  ...     39.48    -121.09  0.781
20636  2.5568      18.0  6.114035  ...     39.49    -121.21  0.771
20637  1.7000      17.0  5.205543  ...     39.43    -121.22  0.923
20638  1.8672      18.0  5.329513  ...     39.43    -121.32  0.847
20639  2.3886      16.0  5.254717  ...     39.37    -121.24  0.894
'''

