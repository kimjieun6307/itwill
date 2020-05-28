'''
분류용 sklearn dataset 정리
'''
from sklearn import datasets # dataset 제공 library
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

######################################
# 분류분석(다항로지스틱 회귀분석)에 적합한 데이터셋
# 1. wine 
# 2. breast cancer 데이터셋
# 3. digits 데이터셋 - 숫자 예측(0~9)
# 4. Covertype
# 5. news group 
######################################

# 1. wine 
'''
와인의 화학 조성을 사용하여 와인의 종류를 예측하기 위한 데이터

•타겟 변수
◦와인의 종류 : 0, 1, 2 세가지 값 

•특징 변수 
◦알콜(Alcohol)
◦말산(Malic acid)
◦회분(Ash)
◦회분의 알칼리도(Alcalinity of ash) 
◦마그네슘(Magnesium)
◦총 폴리페놀(Total phenols)
◦플라보노이드 폴리페놀(Flavanoids)
◦비 플라보노이드 폴리페놀(Nonflavanoid phenols)
◦프로안토시아닌(Proanthocyanins)
◦색상의 강도(Color intensity)
◦색상(Hue)
◦희석 와인의 OD280/OD315 비율 (OD280/OD315 of diluted wines)
◦프롤린(Proline)
'''
from sklearn.datasets import load_wine
wine = load_wine()
print(list(wine.target_names)) # ['class_0', 'class_1', 'class_2']
#cf) target_names ==> y변수가 범주형이면 target_names 가지고 있다.(연속형이면 없음)

wine_x, wine_y = load_wine(return_X_y=True)
print(type(wine_x)) # <class 'numpy.ndarray'>
print(np.shape(wine_x)) # (178, 13) : matrix
print(np.shape(wine_y)) # (178,) : vector

# numpy -> DataFrame 
wine_df = pd.DataFrame(wine_x, columns=wine.feature_names)
tg = pd.Series(wine_y, dtype="category")
tg = tg.cat.rename_categories(wine.target_names)
wine_df['class'] = tg
wine_df.tail()

# class별 주요변수 간 산점도 
sn.pairplot(vars=["alcohol", "alcalinity_of_ash", "total_phenols", "flavanoids"], 
             hue="class", data=wine_df)
plt.show()
#@@1


# 2. breast cancer 데이터셋
'''
유방암(breast cancer) 진단 데이터 

•타겟 변수 
 - 종양이 양성(benign)인지 악성(malignant)인지를 판별 ==> 이항
•특징 변수(30개) 
 - 유방암 진단 사진으로부터 측정한 종양(tumar)의 특징값
'''
cancer = datasets.load_breast_cancer()
print(cancer)
print(cancer.DESCR)

cancer_x = cancer.data
cancer_y = cancer.target
print(np.shape(cancer_x)) # (569, 30) : matrix
print(np.shape(cancer_y)) # (569,) : vector

cencar_df = pd.DataFrame(cancer_x, columns=cancer.feature_names)
tg = pd.Series(cancer_y, dtype="category")
tg = tg.cat.rename_categories(cancer.target_names)
cencar_df['class'] = tg
cencar_df.tail()

# 타겟 변수 기준 주요변수 간 산점도 
sn.pairplot(vars=["worst radius", "worst texture", "worst perimeter", "worst area"], 
             hue="class", data=cencar_df)
plt.show()


# 3. digits 데이터셋 - 숫자 예측(0~9)
'''
숫자 필기 이미지 데이터

•타겟 변수 
 - 0 ~ 9 : 10진수 정수 
•특징 변수(64픽셀) 
 -0부터 9까지의 숫자를 손으로 쓴 이미지 데이터
 -각 이미지는 0부터 15까지의 16개 명암을 가지는 8x8=64픽셀 해상도의 흑백 이미지
'''
digits = datasets.load_digits()
print(digits.DESCR)

print(digits.data.shape) # (1797, 64)
print(digits.target.shape) # (1797,)
print(digits) # 8x8 image of integer pixels in the range 0..16

# 첫번째 이미지 픽셀, 정답 확인
img2 = digits.data[0].reshape(8,8)
plt.imshow(img2)
#@@2 ==> 0처럼 보이는 이미지
digits.target[0] # 0 ==> 정답 0

np.random.seed(0)
N = 4
M = 10
fig = plt.figure(figsize=(10, 5))
plt.subplots_adjust(top=1, bottom=0, hspace=0, wspace=0.05)
for i in range(N): # 4
    for j in range(M): # 10
        k = i*M+j
        ax = fig.add_subplot(N, M, k+1)
        ax.imshow(digits.images[k], cmap=plt.cm.bone, interpolation="none")
        ax.grid(False)
        ax.xaxis.set_ticks([])
        ax.yaxis.set_ticks([])
        plt.title(digits.target_names[digits.target[k]])
plt.tight_layout()
plt.show()


# 4. Covertype
'''
대표 수종 데이터

•타겟 변수 
 - 미국 삼림을 30×30m 영역으로 나누어 각 영역의 특징으로부터 대표적인 나무의 종(species)을 기록한 데이터
•특징 변수(30개) 
 - 특징 데이터가 54종류, 표본 데이터의 갯수가 581,012개

'''
from sklearn.datasets import fetch_covtype
import pandas as pd

covtype = fetch_covtype()
print(covtype.DESCR)

covtype_x = covtype.data 
covtype_y = covtype.target 

covtype_x.shape #  (581012, 54)
covtype_y.shape # (581012,)
covtype_x[0] # 1row 

# DataFrame의 특징 변수 지정 
covtype.data.shape[1] # 54
columns=["x{:02d}".format(i + 1) for i in range(covtype.data.shape[1])]
columns

# X변수 칼럼명 지정 : x01 ~ x54
df = pd.DataFrame(covtype.data, 
                  columns=["x{:02d}".format(i + 1) for i in range(covtype.data.shape[1])],
                  dtype=float) 
df.head()

# Y변수 DataFrame에 추가 
cy = pd.Series(covtype.target, dtype="category")
df['Cover_Type'] = cy
df.head()
df.tail()
df.info()


# 5. news group 
'''< 텍스트 마이닝 >
- 20개의 뉴스 그룹 문서 데이터(문서 분류 모델 예문으로 사용)

•타겟 변수 
◦문서가 속한 뉴스 그룹 : 20개 

•특징 변수 
◦문서 텍스트 : 18,846
'''

from sklearn.datasets import fetch_20newsgroups
newsgroups = fetch_20newsgroups(subset='all') # 'train', 'test'
# Downloading 20news dataset.

print(newsgroups.DESCR)
'''
**Data Set Characteristics:**

    =================   ==========
    Classes                     20
    Samples total            18846
    Dimensionality               1
    Features                  text
    =================   ==========
'''

# data vs target
newsgroups.data # text
len(newsgroups.data) # 18846

newsgroups.target # array([10,  3, 17, ...,  3,  1,  7])
len(newsgroups.target) # 18846

# 뉴스 그룹 : 20개 이름 
newsgroups.target_names # ['alt.atheism', ... 'talk.religion.misc']


