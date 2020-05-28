'''
문) load_wine() 함수를 이용하여 와인 데이터를 다항분류하는 로지스틱 회귀모델을 생성하시오. 
  조건1> train/test - 7:3비울
  조건2> y 변수 : wine.data 
  조건3> x 변수 : wine.data
  조건4> 모델 평가 : confusion_matrix, 분류정확도[accuracy]
'''

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix 

import numpy as np
import pandas as pd

# 1. wine 데이터셋 
wine = load_wine()

# 2. 변수 선택 
wine_x = wine.data # x변수 
wine_y = wine.target # y변수

wine_x.shape(178, 13)
pd.unique(wine_y) # array([0, 1, 2])


# 3. train/test split(7:3)
x_train, x_test, y_train, y_test = train_test_split(wine_x, wine_y, test_size = 0.3)


# 4. model 생성  : solver='lbfgs', multi_class='multinomial'
ls = LogisticRegression(random_state=123, multi_class='multinomial')
model = ls.fit(x_train, y_train)

'''
ls = LogisticRegression(solver='lbfgs',
                        multi_class = 'multinomial'
                        max_iter=200, # 반복횟수
                        n_jobs=1, # 병렬처리 cpu 수
                        verbose = 1) # 학습과정 출력여부
'''

# 5. 모델 평가 : accuracy, confusion matrix
y_pred = model.predict(x_test)

acc = accuracy_score(y_test, y_pred)
acc # 0.9444444444444444

con_mat=confusion_matrix(y_test, y_pred)
con_mat
'''array([[17,  2,  0],
       [ 0, 21,  1],
       [ 0,  0, 13]], dtype=int64)
'''
acc2 = (con_mat[0,0] + con_mat[1,1] + con_mat[2,2])/con_mat.sum()
acc2 # 0.9444444444444444

# 히트맵 : 분류정확도 결과를 시각화
import seaborn as sn # heatmap - Accuracy Score
import matplotlib.pyplot as plt

# confusion matrix heatmap 
plt.figure(figsize=(6,6)) # chart size
sn.heatmap(con_mat, annot=True, fmt=".3f", linewidths=.5, square = True);# , cmap = 'Blues_r' : map »ö»ó 
plt.ylabel('Actual label');
plt.xlabel('Predicted label');
all_sample_title = 'Accuracy Score: {0}'.format(acc)
plt.title(all_sample_title, size = 18)
plt.show()
#@@6




