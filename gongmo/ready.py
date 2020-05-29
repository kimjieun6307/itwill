# -*- coding: utf-8 -*-
"""
Created on Thu May 28 18:00:50 2020

@author: user
"""
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 13:56:12 2020

@author: user
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plant1 = pd.read_csv("plant1_train.csv")
plant1.info()

# 칼럼명 수정 "." -> " _"
plant1.columns = plant1.columns.str.replace('.', '_')
plant1.columns

# 날짜칼럼에서 년/월/일/시/분 추출
import re

date = plant1['plant1_train_mea_ddhr']
date = [re.sub('-','',str(i)) for i in date]
date = [re.sub(':','',str(i)) for i in date]
len(date) # 58749
date[58600:]

year = [int(i[:4]) for i in date]
moth = [int(i[4:6]) for i in date]
day = [int(i[6:8]) for i in date]
hour = [i[-4:] for i in date]
hour = [int(i[-4:-2]) for i in hour]
minute = [int(i[-2:]) for i in date]

# 데이터 확인
year[58600:]
moth[58600:]
day[58600:]
hour[58600:]
minute[58600:]


pd.Series(minute).unique() # [ 0, 30, 10, 20, 40, 50]
pd.Series(hour).unique() 
'''
array([ 0,  3,  6,  9, 12, 15, 18, 21, 22, 23,  1,  2,  4,  5,  7,  8, 10,
       11, 13, 14, 16, 17, 19, 20], dtype=int64)
'''


plant1['year']=year
plant1['moth']=moth
plant1['day']=day
plant1['hour']=hour
plant1['min']=minute


plant1.info()

##########################################
# 매 정각 데이터만 subset : 58749 -> 21745
#######################################
plant_hour = plant1[plant1['min']==0]
plant_hour.shape #  (21745, 21)


# 한 시간 단위로 데이터 줄임 : plant1_1hour.csv 저장
plant_hour.to_csv('plant1_1hour.csv', index=None, encoding='utf-8')

plant_hour = pd.read_csv('plant1_1hour.csv')


# 센서별 데이터 나누기
plan_a = [1,2,3,4,11,12,13,16,17,18,19,20]
plan_b = [1,5,6,7,11,12,14,16,17,18,19,20 ]
plan_c = [1,8,9,10,11,12,15,16,17,18,19,20]

plant_a_df = plant_hour.iloc[:, plan_a]
plant_b_df = plant_hour.iloc[:, plan_b]
plant_c_df = plant_hour.iloc[:, plan_c]

plant_a_df.shape   # (21745, 12)
plant_b_df.shape   # (21745, 12)
plant_c_df.shape   # (21745, 12)


###############################
# loc2 데이터 plant_a_df
##############################


plant_a_df = plant_a_df.dropna() # 결측치 처리 : 21745->20925
21745-20925 # 820

plant_a_df.info()
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 20925 entries, 0 to 58743
Data columns (total 12 columns):
 #   Column                      Non-Null Count  Dtype  
---  ------                      --------------  -----  
 0   plant1_train_mea_ddhr       20925 non-null  object 
 1   plant1_train_tem_in_loc1    20925 non-null  float64
 2   plant1_train_hum_in_loc1    20925 non-null  float64
 3   plant1_train_tem_coil_loc1  20925 non-null  float64
 4   plant1_train_tem_out_loc1   20925 non-null  float64
 5   plant1_train_hum_out_loc1   20925 non-null  float64
 6   plant1_train_cond_loc1      20925 non-null  float64
 7   year                        20925 non-null  object 
 8   moth                        20925 non-null  object 
 9   day                         20925 non-null  object 
 10  min                         20925 non-null  object 
 11  hour                        20925 non-null  object 
 '''


df_2016 = plant_a_df[plant_a_df['year']==2016]
df_2016['plant1_train_cond_loc1'].value_counts()
'''
0.0    2077
1.0       9
'''

df_2016 = df_2016[df_2016['plant1_train_cond_loc1']==1]
'''
     plant1_train_mea_ddhr  plant1_train_tem_in_loc1  ...  min  hour
92        2016-04-12 12:00                     18.00  ...   00     2
120        2016-04-16 0:00                     17.00  ...   00     0
241        2016-05-01 3:00                     21.00  ...   00     3
257        2016-05-03 3:00                     21.00  ...   00     3
608        2016-06-16 0:00                     24.00  ...   00     0
609        2016-06-16 3:00                     23.00  ...   00     3
610        2016-06-16 6:00                     23.00  ...   00     6
2088       2016-12-22 0:00                     13.24  ...   00     0
2089       2016-12-22 3:00                     14.09  ...   00     3
[9 rows x 12 columns]
'''

plant_a_df = plant_a_df[plant_a_df.year > 2016] # 20925 -> 18839
plant_a_df.shape # (18839, 12)


# 센서 1 데이터 plant_a_df 전처리 결측치 제외 2016년 데이터 제외(1시간 간격 아님)



# shift() 사용
plant_a_df['24hour_after']=plant_a_df['plant1_train_mea_ddhr'].shift(-24)
plant_a_df['24hour_cond_loc1']=plant_a_df['plant1_train_cond_loc1'].shift(-24)
plant_a_df.info() 
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 18839 entries, 2842 to 58743
Data columns (total 14 columns):
 #   Column                      Non-Null Count  Dtype  
---  ------                      --------------  -----  
 0   plant1_train_mea_ddhr       18839 non-null  object 
 1   plant1_train_tem_in_loc1    18839 non-null  float64
 2   plant1_train_hum_in_loc1    18839 non-null  float64
 3   plant1_train_tem_coil_loc1  18839 non-null  float64
 4   plant1_train_tem_out_loc1   18839 non-null  float64
 5   plant1_train_hum_out_loc1   18839 non-null  float64
 6   plant1_train_cond_loc1      18839 non-null  float64
 7   year                        18839 non-null  int64  
 8   moth                        18839 non-null  int64  
 9   day                         18839 non-null  int64  
 10  hour                        18839 non-null  int64  
 11  min                         18839 non-null  int64  
 12  24hour_after                18815 non-null  object 
 13  24hour_cond_loc1            18815 non-null  float64
 '''

plant_a_df.iloc[18600:,[0,12]]
'''
      plant1_train_mea_ddhr     24hour_after
57315       2019-03-22 1:00  2019-03-23 1:00
57321       2019-03-22 2:00  2019-03-23 2:00
57327       2019-03-22 3:00  2019-03-23 3:00
57333       2019-03-22 4:00  2019-03-23 4:00
57339       2019-03-22 5:00  2019-03-23 5:00
'''

a=[0,1,2,3,4,5,13]
plant_a_df = plant_a_df.iloc[:, a]


plant_a_df = plant_a_df.dropna() 
plant_a_df.info() 
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 18815 entries, 2842 to 21720
Data columns (total 7 columns):
 #   Column                      Non-Null Count  Dtype  
---  ------                      --------------  -----  
 0   plant1_train_mea_ddhr       18815 non-null  object 
 1   plant1_train_tem_in_loc1    18815 non-null  float64
 2   plant1_train_hum_in_loc1    18815 non-null  float64
 3   plant1_train_tem_coil_loc1  18815 non-null  float64
 4   plant1_train_tem_out_loc1   18815 non-null  float64
 5   plant1_train_hum_out_loc1   18815 non-null  float64
 6   24hour_cond_loc1            18815 non-null  float64
'''

18839-18815 # 24

plant_a_df.to_csv('plant_a_df.csv')



###################################
# loc2 데이터 plant_b_df
##############################
plant_b_df.info()
'''<class 'pandas.core.frame.DataFrame'>
RangeIndex: 21745 entries, 0 to 21744
Data columns (total 12 columns):
 #   Column                      Non-Null Count  Dtype  
---  ------                      --------------  -----  
 0   plant1_train_mea_ddhr       21745 non-null  object 
 1   plant1_train_tem_in_loc2    21675 non-null  float64
 2   plant1_train_hum_in_loc2    21675 non-null  float64
 3   plant1_train_tem_coil_loc2  21675 non-null  float64
 4   plant1_train_tem_out_loc1   21675 non-null  float64
 5   plant1_train_hum_out_loc1   21675 non-null  float64
 6   plant1_train_cond_loc2      21675 non-null  float64
 7   year                        21745 non-null  int64  
 8   moth                        21745 non-null  int64  
 9   day                         21745 non-null  int64  
 10  hour                        21745 non-null  int64  
 11  min                         21745 non-null  int64  
'''

plant_b_df = plant_b_df.dropna() # 결측치 처리 : 21745->21675
plant_b_df.shape #  (21675, 12)
21745-21675 # 70 -- 결측치 제외


df_2016 = plant_b_df[plant_b_df['year']==2016]
df_2016['plant1_train_cond_loc2'].value_counts()
'''
0.0    2228
1.0      17
'''

df_2016 = df_2016[df_2016['plant1_train_cond_loc2']==1]
'''
     plant1_train_mea_ddhr  plant1_train_tem_in_loc2  ...  hour  min
59         2016-04-08 9:00                     13.00  ...     9    0
67         2016-04-09 9:00                     13.00  ...     9    0
92        2016-04-12 12:00                     16.00  ...    12    0
120        2016-04-16 0:00                     16.00  ...     0    0
539        2016-06-07 9:00                     29.00  ...     9    0
1481       2016-10-03 3:00                     24.10  ...     3    0
1482       2016-10-03 6:00                     24.13  ...     6    0
1829      2016-11-19 15:00                     15.16  ...    15    0
1830      2016-11-19 18:00                     15.65  ...    18    0
1831      2016-11-19 21:00                     15.65  ...    21    0
1955       2016-12-05 9:00                     10.76  ...     9    0
2069      2016-12-19 15:00                     11.68  ...    15    0
2070      2016-12-19 18:00                     11.98  ...    18    0
2087      2016-12-21 21:00                     11.86  ...    21    0
2088       2016-12-22 0:00                     12.38  ...     0    0
2089       2016-12-22 3:00                     13.82  ...     3    0
2090       2016-12-22 6:00                     12.50  ...     6    0
[17 rows x 12 columns]
'''

plant_b_df = plant_b_df[plant_b_df.year > 2016] # 21675 -> 19430
plant_b_df.shape # (19430, 12)


# shift() 사용
plant_b_df['24hour_after']=plant_b_df['plant1_train_mea_ddhr'].shift(-24)
plant_b_df['24hour_cond_loc2']=plant_b_df['plant1_train_cond_loc2'].shift(-24)
plant_b_df.info() 


plant_b_df.iloc[18600:,[0,12]]
'''
      plant1_train_mea_ddhr      24hour_after
20915      2019-02-25 10:00  2019-02-26 10:00
20916      2019-02-25 11:00  2019-02-26 11:00
20917      2019-02-25 12:00  2019-02-26 12:00
20918      2019-02-25 13:00  2019-02-26 13:00
20919      2019-02-25 14:00  2019-02-26 14:00
'''

a=[0,1,2,3,4,5,13]
plant_b_df = plant_b_df.iloc[:, a]

plant_b_df = plant_b_df.dropna() 
plant_b_df.info() 
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 19406 entries, 2250 to 21720
Data columns (total 7 columns):
 #   Column                      Non-Null Count  Dtype  
---  ------                      --------------  -----  
 0   plant1_train_mea_ddhr       19406 non-null  object 
 1   plant1_train_tem_in_loc2    19406 non-null  float64
 2   plant1_train_hum_in_loc2    19406 non-null  float64
 3   plant1_train_tem_coil_loc2  19406 non-null  float64
 4   plant1_train_tem_out_loc1   19406 non-null  float64
 5   plant1_train_hum_out_loc1   19406 non-null  float64
 6   24hour_cond_loc2            19406 non-null  float64
'''
19430 - 19406 # 24

plant_b_df.to_csv('plant_b_df.csv')



###################################
# loc3 데이터 plant_c_df
##############################
plant_c_df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 21745 entries, 0 to 21744
Data columns (total 12 columns):
 #   Column                      Non-Null Count  Dtype  
---  ------                      --------------  -----  
 0   plant1_train_mea_ddhr       21745 non-null  object 
 1   plant1_train_tem_in_loc3    21650 non-null  float64
 2   plant1_train_hum_in_loc3    21650 non-null  float64
 3   plant1_train_tem_coil_loc3  21675 non-null  float64
 4   plant1_train_tem_out_loc1   21675 non-null  float64
 5   plant1_train_hum_out_loc1   21675 non-null  float64
 6   plant1_train_cond_loc3      21650 non-null  float64
 7   year                        21745 non-null  int64  
 8   moth                        21745 non-null  int64  
 9   day                         21745 non-null  int64  
 10  hour                        21745 non-null  int64  
 11  min                         21745 non-null  int64  
'''


df_2016 = plant_c_df[plant_c_df['year']==2016]
df_2016['plant1_train_cond_loc3'].value_counts()
'''
0.0    2210
1.0      35
'''
df_2016 = df_2016[df_2016['plant1_train_cond_loc3']==1]
'''
     plant1_train_mea_ddhr  plant1_train_tem_in_loc3  ...  hour  min
43         2016-04-06 9:00                     13.00  ...     9    0
59         2016-04-08 9:00                     12.00  ...     9    0
60        2016-04-08 12:00                     13.00  ...    12    0
65         2016-04-09 3:00                     13.00  ...     3    0
66         2016-04-09 6:00                     13.00  ...     6    0
67         2016-04-09 9:00                     13.00  ...     9    0
91         2016-04-12 9:00                     14.00  ...     9    0
92        2016-04-12 12:00                     15.00  ...    12    0
106        2016-04-14 6:00                     10.00  ...     6    0
107        2016-04-14 9:00                     11.00  ...     9    0
120        2016-04-16 0:00                     15.00  ...     0    0
121        2016-04-16 3:00                     15.00  ...     3    0
358       2016-05-15 18:00                     23.00  ...    18    0
578        2016-06-12 6:00                     25.00  ...     6    0
765       2016-07-05 15:00                     26.54  ...    15    0
1481       2016-10-03 3:00                     23.68  ...     3    0
1828      2016-11-19 12:00                     14.00  ...    12    0
1829      2016-11-19 15:00                     14.55  ...    15    0
1830      2016-11-19 18:00                     15.07  ...    18    0
1831      2016-11-19 21:00                     15.16  ...    21    0
1832       2016-11-20 0:00                     15.07  ...     0    0
1955       2016-12-05 9:00                     10.31  ...     9    0
2068      2016-12-19 12:00                      9.36  ...    12    0
2069      2016-12-19 15:00                     11.34  ...    15    0
2070      2016-12-19 18:00                     11.25  ...    18    0
2071      2016-12-19 21:00                     10.00  ...    21    0
2086      2016-12-21 18:00                     11.43  ...    18    0
2087      2016-12-21 21:00                     11.59  ...    21    0
2088       2016-12-22 0:00                     11.86  ...     0    0
2089       2016-12-22 3:00                     13.30  ...     3    0
2090       2016-12-22 6:00                     11.71  ...     6    0
2240      2016-12-31 14:00                      6.55  ...    14    0
2241      2016-12-31 15:00                      7.31  ...    15    0
2242      2016-12-31 16:00                      7.68  ...    16    0
2243      2016-12-31 17:00                      7.71  ...    17    0
'''


plant_c_df = plant_c_df[2200:]
plant_c_df.shape # (19545, 12)


# shift() 사용
plant_c_df['24hour_after']=plant_c_df['plant1_train_mea_ddhr'].shift(-24)
plant_c_df['24hour_cond_loc3']=plant_c_df['plant1_train_cond_loc3'].shift(-24)
plant_c_df.info() 


plant_c_df.iloc[18600:,[0,12]]
'''
      plant1_train_mea_ddhr      24hour_after
20800      2019-02-20 15:00  2019-02-21 15:00
20801      2019-02-20 16:00  2019-02-21 16:00
20802      2019-02-20 17:00  2019-02-21 17:00
20803      2019-02-20 18:00  2019-02-21 18:00
20804      2019-02-20 19:00  2019-02-21 19:00
'''

a=[0,1,2,3,4,5,13]
plant_c_df = plant_c_df.iloc[:, a]

plant_c_df.columns = ['plant1_train_mea_ddhr', 'plant1_train_tem_in_loc3',
       'plant1_train_hum_in_loc3', 'plant1_train_tem_coil_loc3',
       'plant1_train_tem_out_loc1', 'plant1_train_hum_out_loc1',
       '24hour_cond_loc3']
plant_c_df = plant_c_df.dropna() 
plant_c_df.info() 
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 19406 entries, 2250 to 21720
Data columns (total 7 columns):
 #   Column                      Non-Null Count  Dtype  
---  ------                      --------------  -----  
 0   plant1_train_mea_ddhr       19406 non-null  object 
 1   plant1_train_tem_in_loc2    19406 non-null  float64
 2   plant1_train_hum_in_loc2    19406 non-null  float64
 3   plant1_train_tem_coil_loc2  19406 non-null  float64
 4   plant1_train_tem_out_loc1   19406 non-null  float64
 5   plant1_train_hum_out_loc1   19406 non-null  float64
 6   24hour_cond_loc2            19406 non-null  float64
'''
19545 - 19342 # 203

plant_c_df.to_csv('plant_c_df.csv')











