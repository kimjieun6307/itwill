# -*- coding: utf-8 -*-
"""
marker, color, line style, label
"""

import  matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot') # 차트 격자 제공

# data생성
data1 = np.random.randn(100) # 평균=0, 표준편차 =1
data2 = 0.5 + 0.1 * np.random.randn(100) # 평균 0.5 표준편차 0.1 
data3 = 0.7 + 0.2 * np.random.randn(100) # 조금씩 다르게 난수 생성
data4 = 0.3 + 0.3 * np.random.randn(100)

fig = plt.figure(figsize=(12, 5))
chart = fig.add_subplot()

chart.plot(data1, marker = 'o', color = 'y', linestyle='-', label='data1')
chart.plot(data2, marker = '+', color = 'r', linestyle='--', label='data2')
chart.plot(data3, marker = '*', color = 'g', linestyle='-.', label='data3')
chart.plot(data4, marker = 's', color = 'b', linestyle=':', label='data4')
plt.legend(loc='best') # 범례추가
chart.set_title('Multi-line chart')
chart.set_xlabel('색인')
chart.set_ylabel('random number')
plt.show()









