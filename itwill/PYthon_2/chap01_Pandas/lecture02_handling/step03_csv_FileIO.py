# -*- coding: utf-8 -*-
"""
1. csv file read : pd.read_csv('~.csv')
2. csv file write : .to_cvs('~.csv', index=None, encodint='utf-8')
3. random sampling
"""


import pandas as pd

# 1. csv file read
iris = pd.read_csv('iris.csv')
iris.info()
'''
칼럼이름에 공백이 있거나 점(.)이 있으면 객체로 잘못 인식하기 때문에
'.' 대신에 '_'로 문자 변경할 수 있음.
'''

# ● 칼럼명 변경 : 특수문자 or 공백 -> 문자 변경
iris.columns = iris.columns.str.replace('.', '_')
iris.head()
#@@1
iris.Sepal_Length
'''
0      5.1
1      4.9
2      4.7
3      4.6
4      5.0
~
145    6.7
'''

# ● 칼럼명이 없는 경우
# 기본 숫자(0~n)  => 칼럼명 변경
st = pd.read_csv('student.csv', header = None)
st
'''## 칼럼명 없으면 기본으로 숫자(0~n)##
     0     1    2   3
0  101  hong  175  65
1  201   lee  185  85
2  301   kim  173  60
3  401  park  180  70
'''
col_names = ['학번', '이름', '키', '몸무게']
st.columns = col_names
st

# 행 이름 변경
# st.index = 수정값

# 비만도 지수(BMI)
# BMI = 몸무게 / 키**2 (단위 : 몸무게 kg, 키 m)
BMI = [st.loc[i,'몸무게']/((st.loc[i,'키']*0.01)**2) for i in range(len(st))]
BMI # [21.224489795918366, 24.835646457268076, 20.04744562130375, 21.604938271604937]
type(BMI) # list

st['BMI']=BMI
st
'''
   학번   이름  키  몸무게     BMI
0  101  hong  175   65  21.224490
1  201   lee  185   85  24.835646
2  301   kim  173   60  20.047446
3  401  park  180   70  21.604938
'''

st['BMI'] = st['BMI'].round(2)
st
'''
  학번  이름   키  몸무게   BMI
0  101  hong  175   65  21.22
1  201   lee  185   85  24.84
2  301   kim  173   60  20.05
3  401  park  180   70  21.60
'''

# 2. csv file write
st.to_csv('student_df.csv', index=None, encoding='utf-8')

st_df = pd.read_csv('student_df.csv')
st_df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 5 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   학번      4 non-null      int64  
 1   이름      4 non-null      object 
 2   키       4 non-null      int64  
 3   몸무게     4 non-null      int64  
 4   BMI     4 non-null      float64
'''

# 3. random sampling
wdbc = pd.read_csv('wdbc_data.csv')
wdbc.info() 
'''
RangeIndex: 569 entries, 0 to 568
Data columns (total 32 columns):
'''
# 569개의 관측치 중에 400개 랜덤샘플링
wdbc_train = wdbc.sample(400)
wdbc_train.shape # (400, 32)

wdbc_train.head()
'''
           id diagnosis  ...  symmetry_worst  dimension_worst
523     92751         B  ...          0.2871          0.07039
557    906564         B  ...          0.2827          0.09208
533  87281702         M  ...          0.3054          0.09519
225    894047         B  ...          0.3142          0.08116
414   8912055         B  ...          0.3101          0.06688
'''






