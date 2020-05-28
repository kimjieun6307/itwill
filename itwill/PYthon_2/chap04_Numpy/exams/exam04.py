'''
step04_axis_dot 관련문제 : 
문) 다음 같은 입력 x와 가중치 w를 이용하여 hidden node를 구하시오.  
    <조건1> w(3,3) * x(3,1) = h(3,1)  
    <조건2> weight : 표준정규분포 난수 
    <조건3> X : 1,2,3    
'''

import numpy as np

weight = np.random.randn(3,3)
print('weight data : ', weight )

x=np.array([[1],[2],[3]])
x.shape
print('x data :', x)

hidden = np.dot(weighr, x)
print('hidden : ', hidden)








