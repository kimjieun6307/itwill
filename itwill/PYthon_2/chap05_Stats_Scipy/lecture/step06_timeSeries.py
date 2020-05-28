# -*- coding: utf-8 -*-
"""
시계열 분석(time series analysis)
 1. 시계열 자료 생성 방법
 2. 날짜형식 수정(다국어) : 외국식 -> 국내식
 3. 시계열 시각화
 4. 이동평균 기능 : 5일, 10일 단위 평균 -> 추세선 평활(스무딩)
"""

from datetime import datetime # 날짜형식 수정
import pandas as pd # 파일 읽기
import matplotlib.pyplot as plt  # 시각화
import numpy as np # 수치 자료 생성

# 1. 시계열 자료 생성 방법
time_data = pd.date_range("2017-03-01", "2020-03-30")
time_data
'''
DatetimeIndex(['2017-03-01', '2017-03-02', '2017-03-03', '2017-03-04',
               '2017-03-05', '2017-03-06', '2017-03-07', '2017-03-08',
               '2017-03-09', '2017-03-10',
               ...
               '2020-03-21', '2020-03-22', '2020-03-23', '2020-03-24',
               '2020-03-25', '2020-03-26', '2020-03-27', '2020-03-28',
               '2020-03-29', '2020-03-30'],
              dtype='datetime64[ns]', length=1126, freq='D')
'''
# freq='D' ==> 날짜(day)별 --기본값

# 월단위 시계열 자료 (freq = 'M')  ==> 월의 마지막 날 기준
time_data2 = pd.date_range("2017-03-01", "2020-03-30", freq = 'M')
time_data2
'''
DatetimeIndex(['2017-03-31', '2017-04-30', '2017-05-31', '2017-06-30',
               '2017-07-31', '2017-08-31', '2017-09-30', '2017-10-31',
               '2017-11-30', '2017-12-31', '2018-01-31', '2018-02-28',
               '2018-03-31', '2018-04-30', '2018-05-31', '2018-06-30',
               '2018-07-31', '2018-08-31', '2018-09-30', '2018-10-31',
               '2018-11-30', '2018-12-31', '2019-01-31', '2019-02-28',
               '2019-03-31', '2019-04-30', '2019-05-31', '2019-06-30',
               '2019-07-31', '2019-08-31', '2019-09-30', '2019-10-31',
               '2019-11-30', '2019-12-31', '2020-01-31', '2020-02-29'],
              dtype='datetime64[ns]', freq='M')
'''
len(time_data2) # 36

# 월 단위 매출현황
x= pd.Series(np.random.uniform(10, 100, size=36))

df = pd.DataFrame({'data' : time_data2, 'price':x})
df
'''
         data      price
0  2017-03-31  35.106769
1  2017-04-30  99.994198
2  2017-05-31  75.532740
3  2017-06-30  58.946318
4  2017-07-31  69.727474
~~
'''

plt.plot(df['data'], df['price']) # (x,y)
#@@8



# 2. 날짜형식 수정(다국어) : 외국식(26-Feb-16) -> 국내식(2016-02-26)
cospi = pd.read_csv('cospi.csv')
cospi.info()
cospi.head()
'''
        Date     Open     High      Low    Close  Volume
0  26-Feb-16  1180000  1187000  1172000  1172000  176906
1  25-Feb-16  1172000  1187000  1172000  1179000  128321
2  24-Feb-16  1178000  1179000  1161000  1172000  140407
~~
'''

date = cospi['Date']
len(date) # 247

# list + for : 외국식(26-Feb-16) -> 국내식(2016-02-26)
kdate = [datetime.strptime(i, '%d-%b-%y') for i in date]
kdate
'''
[datetime.datetime(2016, 2, 26, 0, 0),
 datetime.datetime(2016, 2, 25, 0, 0),
 datetime.datetime(2016, 2, 24, 0, 0),
 ~~
'''

# 날짜 칼럼 수정
cospi['Date'] = kdate
cospi.info()
'''
 0   Date    247 non-null    datetime64[ns]
'''
 
cospi.head()
'''
        Date     Open     High      Low    Close  Volume
0 2016-02-26  1180000  1187000  1172000  1172000  176906
1 2016-02-25  1172000  1187000  1172000  1179000  128321
2 2016-02-24  1178000  1179000  1161000  1172000  140407
~~
'''
cospi.tail()


# 3. 시계열 시각화
cospi.index # RangeIndex(start=0, stop=247, step=1)

# 특정 칼럼 -> index 적용
new_cospi = cospi.set_index('Date')
new_cospi.head()
'''
               Open     High      Low    Close  Volume
Date                                                  
2016-02-26  1180000  1187000  1172000  1172000  176906
2016-02-25  1172000  1187000  1172000  1179000  128321
2016-02-24  1178000  1179000  1161000  1172000  140407
~~
'''
new_cospi.info()
new_cospi.index
'''
DatetimeIndex(['2016-02-26', '2016-02-25', '2016-02-24', '2016-02-23',
               '2016-02-22', '2016-02-19', '2016-02-18', '2016-02-17',
               '2016-02-16', '2016-02-15',
               ...
               '2015-03-13', '2015-03-12', '2015-03-11', '2015-03-10',
               '2015-03-09', '2015-03-06', '2015-03-05', '2015-03-04',
               '2015-03-03', '2015-03-02'],
              dtype='datetime64[ns]', name='Date', length=247, freq=None)
'''

new_cospi['2016']
len(new_cospi['2016'])
new_cospi['2015']
new_cospi['2015-05':'2015-03']


# subset
new_cospi_HL = new_cospi[['High', 'Low']]
new_cospi_HL.index # Date
new_cospi_HL.columns # ['High', 'Low']
new_cospi_HL.head()
'''
               High      Low
Date                        
2016-02-26  1187000  1172000
2016-02-25  1187000  1172000
2016-02-24  1179000  1161000
~~
'''

# 2015년 기준
new_cospi_HL['2015'].plot(title = '2015 year : High vs Low')
#@@9

# 2016년 기준
new_cospi_HL['2016'].plot(title = '2016 year : High vs Low')
#@@10

# 2016년 2월 기준
new_cospi_HL['2016-02'].plot()


# 4. 이동평균 기능 : 5, 10, 20일 평균 -> 추세선 평활(스무딩)

# 1) 5일 단위 이동평균 : 5일 단위 평균 -> 마지막 5일째 이동
roll_mean5 = pd.Series.rolling(new_cospi_HL.High, window = 5, center=False).mean()
roll_mean5


# 2) 10일 단위 이동평균 : 10일 단위 평균 -> 마지막 10일째 이동
roll_mean10 = pd.Series.rolling(new_cospi_HL.High, window = 10, center=False).mean()
roll_mean10


# 3) 20일 단위 이동평균 : 20일 단위 평균 -> 마지막 20일째 이동
roll_mean20 = pd.Series.rolling(new_cospi_HL.High, window = 20, center=False).mean()
roll_mean20[:30]

# rolling mean 시각화
new_cospi_HL.High.plot(color = 'blue', label = 'High column') # 원본
roll_mean5.plot(color='red', label = 'rolling mean 5day')
roll_mean10.plot(color='green', label = 'rolling mean 10day')
roll_mean20.plot(color='orange', label = 'rolling mean 20day')
plt.legend(loc='best') # 범례










