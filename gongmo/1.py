# -*- coding: utf-8 -*-
"""
Created on Tue May 19 17:06:56 2020

@author: user
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plant1 = pd.read_csv("plant1_train.csv")
plant1.info()

plant1.columns = plant1.columns.str.replace('.', '_')
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 58749 entries, 0 to 58748
Data columns (total 16 columns):
 #   Column                      Non-Null Count  Dtype  
---  ------                      --------------  -----  
 0   Unnamed: 0                  58749 non-null  int64  
 1   plant1_train_mea_ddhr       58749 non-null  object 
 2   plant1_train_tem_in_loc1    57879 non-null  float64
 3   plant1_train_hum_in_loc1    57879 non-null  float64
 4   plant1_train_tem_coil_loc1  57879 non-null  float64
 5   plant1_train_tem_in_loc2    58629 non-null  float64
 6   plant1_train_hum_in_loc2    58629 non-null  float64
 7   plant1_train_tem_coil_loc2  58629 non-null  float64
 8   plant1_train_tem_in_loc3    58604 non-null  float64
 9   plant1_train_hum_in_loc3    58604 non-null  float64
 10  plant1_train_tem_coil_loc3  58629 non-null  float64
 11  plant1_train_tem_out_loc1   58629 non-null  float64
 12  plant1_train_hum_out_loc1   58629 non-null  float64
 13  plant1_train_cond_loc1      57879 non-null  float64
 14  plant1_train_cond_loc2      58629 non-null  float64
 15  plant1_train_cond_loc3      58604 non-null  float64
dtypes: float64(14), int64(1), object(1)
'''


# 2, 3, 4, 11,12,13 / 5,6,7,11,12,14 / 8,9,10,11,12,15

plan_a = [1,2, 3, 4, 11,12,13]
plan_b = [1,5,6,7,11,12,14 ]
plan_c = [1,8,9,10,11,12,15]


plan_a_df = plant1.iloc[:, plan_a]
plan_a_df


plan_b_df = plant1.iloc[:, plan_b]
plan_b_df


plan_c_df = plant1.iloc[:, plan_c]
plan_c_df


plan_a_yes = plan_a_df[plan_a_df.plant1_train_cond_loc1==1]
plan_b_yes = plan_b_df[plan_b_df.plant1_train_cond_loc2==1]
plan_c_yes = plan_c_df[plan_c_df.plant1_train_cond_loc3==1]


plan_a_yes.columns
'''
Index(['plant1_train_mea_ddhr', 'plant1_train_tem_in_loc1',
       'plant1_train_hum_in_loc1', 'plant1_train_tem_coil_loc1',
       'plant1_train_tem_out_loc1', 'plant1_train_hum_out_loc1',
       'plant1_train_cond_loc1'],
      dtype='object')
'''
plan_a_yes.iloc[:,5:7].describe()


import matplotlib.pyplot as plt

plt.hist(plan_a_yes['plant1_train_tem_in_loc1'],)
plt.hist(plan_a_yes['plant1_train_tem_coil_loc1'])
plt.hist(plan_a_yes['plant1_train_tem_out_loc1'])
plt.hist(plan_a_yes['plant1_train_hum_in_loc1'])
plt.hist(plan_a_yes['plant1_train_hum_out_loc1'])




plan_a_yes.iloc[:,:6].plot(kind = 'kde', title="plan_a_yes.plot(kind = 'kde')")

plan_a_no.iloc[:,:6].plot(kind = 'kde', title="plan_a_no.plot(kind = 'kde')")


plan_a_no = plan_a_df[plan_a_df.plant1_train_cond_loc1==0]
plan_a_no.info()

plt.hist(plan_a_no['plant1_train_tem_in_loc1'])
plt.hist(plan_a_no['plant1_train_tem_coil_loc1'])
plt.hist(plan_a_no['plant1_train_tem_out_loc1'])
plt.hist(plan_a_no['plant1_train_hum_in_loc1'])
plt.hist(plan_a_no['plant1_train_hum_out_loc1'])


plan_a_no.mean(axis=0)
'''
plant1_train_tem_in_loc1      17.480594
plant1_train_hum_in_loc1      50.292803
plant1_train_tem_coil_loc1    16.419793
plant1_train_tem_out_loc1     13.523524
plant1_train_hum_out_loc1     60.286956
plant1_train_cond_loc1         0.000000
'''
plan_a_yes.mean(axis=0)
'''
plant1_train_tem_in_loc1      13.894836
plant1_train_hum_in_loc1      81.224945
plant1_train_tem_coil_loc1    10.303818
plant1_train_tem_out_loc1     13.143636
plant1_train_hum_out_loc1     83.810691
plant1_train_cond_loc1         1.000000
dtype: float64
'''

plan_a_yes.to_csv("./plan_a_yes.csv", index=None, encoding='utf-8')
plan_a_no.to_csv("./plan_a_no.csv", index=None, encoding='utf-8')


# 칼럼명 수정한 데이터 저장 = plant1.csv
plant1.to_csv("./plant1.csv", index=None, encoding='utf-8')


import re

plant1.columns

date = plant1['plant1_train_mea_ddhr']
date = [re.sub('-','',str(i)) for i in date]
date = [re.sub(':','',str(i)) for i in date]
len(date) # 58749
date[58600:]

year = [i[:4] for i in date]
moth = [i[4:6] for i in date]
day = [i[6:8] for i in date]
minute = [i[-2:] for i in date]
hour = [i[-3:-2] for i in date]


pd.Series(min).describe()
pd.Series(min).unique() # ['00', '30', '10', '20', '40', '50']
pd.Series(hour).unique() # (['0', '3', '6', '9', '2', '5', '8', '1', '4', '7']



plant1['year']=year
plant1['moth']=moth
plant1['day']=day
plant1['min']=min
plant1['hour']=hour

plant1.info()



plant_hour = plant1[plant1['min']=='00']
plant_hour.info()
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 21745 entries, 0 to 58743
Data columns (total 21 columns):
 #   Column                      Non-Null Count  Dtype  
---  ------                      --------------  -----  
 0   Unnamed: 0                  21745 non-null  int64  
 1   plant1_train_mea_ddhr       21745 non-null  object 
 2   plant1_train_tem_in_loc1    20925 non-null  float64
 3   plant1_train_hum_in_loc1    20925 non-null  float64
 4   plant1_train_tem_coil_loc1  20925 non-null  float64
 5   plant1_train_tem_in_loc2    21675 non-null  float64
 6   plant1_train_hum_in_loc2    21675 non-null  float64
 7   plant1_train_tem_coil_loc2  21675 non-null  float64
 8   plant1_train_tem_in_loc3    21650 non-null  float64
 9   plant1_train_hum_in_loc3    21650 non-null  float64
 10  plant1_train_tem_coil_loc3  21675 non-null  float64
 11  plant1_train_tem_out_loc1   21675 non-null  float64
 12  plant1_train_hum_out_loc1   21675 non-null  float64
 13  plant1_train_cond_loc1      20925 non-null  float64
 14  plant1_train_cond_loc2      21675 non-null  float64
 15  plant1_train_cond_loc3      21650 non-null  float64
 16  year                        21745 non-null  object 
 17  moth                        21745 non-null  object 
 18  day                         21745 non-null  object 
 19  min                         21745 non-null  object 
 20  hour                        21745 non-null  object 
dtypes: float64(14), int64(1), object(6)
memory usage: 3.6+ MB
'''

plant_hour.to_csv('plant1_hour.csv', index=None, encoding='utf-8')

plan_a = [1,2,3,4,11,12,13,16,17,18,19,20]
plan_b = [1,5,6,7,11,12,14,16,17,18,19,20 ]
plan_c = [1,8,9,10,11,12,15,16,17,18,19,20]

plant_a_df = plant_hour.iloc[:, plan_a]
plant_b_df = plant_hour.iloc[:, plan_b]
plant_c_df = plant_hour.iloc[:, plan_c]


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

df_2016 = plant_a_df[plant_a_df['year']=='2016']
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

# plant_a_df_2017 = plant_a_df.drop(plant_a_df.year=='2016', axis=1)

year_num = plant_a_df['year']
# year_num = int(year_num)
type(year_num)

year_num=[int(i) for i in year_num]
plant_a_df['year'] = year_num
plant_a_df.info()
'''<class 'pandas.core.frame.DataFrame'>
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
 7   year                        20925 non-null  int64  
 8   moth                        20925 non-null  object 
 9   day                         20925 non-null  object 
 10  min                         20925 non-null  object 
 11  hour                        20925 non-null  object 
 '''


plant_a_df = plant_a_df[plant_a_df.year > 2016] # 20925 -> 18839
plant_a_df.shape # (18839, 12)

plant_a_df.to_csv('plant_a_df.csv', index=None, encoding='utf-8')

plant_a_df.info()
'''<class 'pandas.core.frame.DataFrame'>
Int64Index: 18839 entries, 2842 to 58743
Data columns (total 12 columns):
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
 8   moth                        18839 non-null  object 
 9   day                         18839 non-null  object 
 10  min                         18839 non-null  object 
 11  hour                        18839 non-null  object 
 '''
 
X=plant_a_df.iloc[:, 1:6]
X.columns
'''
Index(['plant1_train_tem_in_loc1', 'plant1_train_hum_in_loc1',
       'plant1_train_tem_coil_loc1', 'plant1_train_tem_out_loc1',
       'plant1_train_hum_out_loc1'],
'''
y=plant_a_df['plant1_train_cond_loc1']



date = plant_a_df['plant1_train_mea_ddhr']

import re
date = [re.sub('-','',str(i)) for i in date]
date = [re.sub(':','',str(i)) for i in date]
date = [re.sub(' ','',str(i)) for i in date]
hour = [i[8:10] for i in date]

plant_a_df['hour']=hour

# shift() 사용
plant_a_df['24hour_after']=plant_a_df['plant1_train_mea_ddhr'].shift(-24)
plant_a_df['24hour_cond_loc1']=plant_a_df['plant1_train_cond_loc1'].shift(-24)
plant_a_df.info() # RangeIndex: 18839

a=[0,1,2,3,4,5,8]
plant_a_df = plant_a_df.iloc[:, a]


plant_a_df = plant_a_df.dropna() # [18815 rows x 7 columns]

18839-18815 # 24

plant_a_df.to_csv('plant_a_df.csv')





