'''
문1) iris.csv 파일을 이용하여 다음과 같이 차트를 그리시오.
    <조건1> iris.csv 파일을 iris 변수명으로 가져온 후 파일 정보 보기
    <조건2> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그리기
    <조건3> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그린 후  5번 칼럼으로 색상 적용 
'''
# plt.scatter(1번 칼럼, 3번 칼럼, c=5번칼럼, marker='o')

import pandas as pd
import matplotlib.pyplot as plt

# <조건1> iris.csv 파일을 iris 변수명으로 가져온 후 파일 정보 보기
iris = pd.read_csv('iris.csv')
iris.info()

# <조건2> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그리기
data1 = iris['Sepal.Length']
data2 = iris['Petal.Length']
plt.plot(data1, data2, 'r+')

# <조건3> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그린 후  5번 칼럼으로 색상 적용 
cdata = iris['Species']
# plt.scatter(data1, data2, c=cdata, marker='o') # error
cdata.unique() # ['setosa', 'versicolor', 'virginica']
len(cdata) # 150

''' **실패**
for i in range(len(cdata)) :
    if i == 'setosa' :
        cdata[i]= 1
    elif i == 'versicolor':
        cdata[i]= 2
    elif i == 'virginica':
        cdata[i]=3

cdata=cdata.drop('setosa')
cdata=cdata.drop('versicolor')
cdata=cdata.drop('virginica')
'''
cnt=[]
for i in cdata :
    if i == 'setosa' :
        cnt.append(1)
    elif i == 'versicolor':
        cnt.append(2)
    elif i == 'virginica':
        cnt.append(3)

len(cnt) # 150
plt.scatter(data1, data2, c=cnt, marker='o')
#@@18


