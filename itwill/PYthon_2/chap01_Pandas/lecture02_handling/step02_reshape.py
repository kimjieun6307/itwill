# -*- coding: utf-8 -*-
"""
DataFrame 모양 변경
- .stack / .unstack
- .T (전치행렬)

"""

import pandas as pd

buy = pd.read_csv('buy_data.csv')
buy.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 22 entries, 0 to 21
Data columns (total 3 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   Date         22 non-null     int64
 1   Customer_ID  22 non-null     int64
 2   Buy          22 non-null     int64
 '''
 
type(buy) # pandas.core.frame.DataFrame

buy.shape  # (22, 3) : 2차원

# 1. stack : row -> column(wide -> long) : 2차원 -> 1차원
buy.head()
'''
       Date  Customer_ID  Buy
0  20150101            1    3
1  20150101            2    4
2  20150102            1    2
3  20150101            2    3
4  20150101            1    2
'''
buy_long = buy.stack()
buy_long.head()
'''
0  Date           20150101
   Customer_ID           1
   Buy                   3
1  Date           20150101
   Customer_ID           2
'''
buy_long.shape # (66,) : 1차원

# 2. unstack : column -> row(long->wide) 
# stack 했던 것만 가능함.
buy_wide = buy_long.unstack()
buy_wide.head()
'''
       Date  Customer_ID  Buy
0  20150101            1    3
1  20150101            2    4
2  20150102            1    2
3  20150101            2    3
4  20150101            1    2
'''
buy_wide.shape # (22, 3)

# 3. 전치행렬 .T : R에서 t()
wide_t = buy_wide.T
wide_t.head()
'''
                   0         1         2   ...        19        20        21
Date         20150101  20150101  20150102  ...  20150106  20150107  20150107
Customer_ID         1         2         1  ...         3         1         5
Buy                 3         4         2  ...         6         9         7

[3 rows x 22 columns]
'''
wide_t.shape # (3, 22)

# 4. 중복 행 제거
buy_df = buy.drop_duplicates()
buy_df.shape # (20, 3) : 2개의 행 제거됨.(22->20)
















