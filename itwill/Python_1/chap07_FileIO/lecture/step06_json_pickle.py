'''
1. json 파일 2가지 형식
 1) 중괄호 : {key : value, ...}
    -> json.loads(row)
 2) 대괄호 : [{key : value, ...},  {key : value, ...}, ... ]
    -> json.load(row)

2. pickle
'''

import json
import pandas as pd

# 1번 형식 - 중괄호 : {key : value, ...} -> json.loads(row)

# 2번 형식 - 대괄호 : [{key : value, ...},  {key : value, ...}, ... ]  -> json.load(row)
file = open("../data/labels.json", mode='r', encoding='utf-8')
# print(file.read()) # [{row}, {row}, ...]
#@@3

rows = json.load(file) # json 문자열 -> python object
print(len(rows)) # 30
print(rows) # [{'id': 76811, 'url': 'https://api.github.com/repos/pandas-dev/pandas/labels/Bug', 'name': 'Bug', 'color': 'e10c02', 'default': False},
print(type(rows)) #<class 'list'>

for row in rows : # [{row}, {row}, ...]
    print(row)
    print(type(row)) #<class 'dict'>

file.close()

#list -> DataFrame
rows_df = pd.DataFrame(rows)
print(rows_df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 30 entries, 0 to 29
Data columns (total 5 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   id       30 non-null     int64 
 1   url      30 non-null     object
 2   name     30 non-null     object
 3   color    30 non-null     object
 4   default  30 non-null     bool  
dtypes: bool(1), int64(1), object(3)
memory usage: 1.1+ KB
None
'''
print(rows_df.head())
'''
       id                                                url  ...   color default
0   76811  https://api.github.com/repos/pandas-dev/pandas...  ...  e10c02   False
1   76812  https://api.github.com/repos/pandas-dev/pandas...  ...  4E9A06   False
2  127681  https://api.github.com/repos/pandas-dev/pandas...  ...  FCE94F   False
3  129350  https://api.github.com/repos/pandas-dev/pandas...  ...  75507B   False
4  134699  https://api.github.com/repos/pandas-dev/pandas...  ...  3465A4   False
'''

'''
2. pickle
: 광범위하게 사용(binary)
python object(list, dict) -> file(binary) -> python object(list, dict)

import pickle
save : pickle.dump(data, file)
load : pickle.load(file)
'''
import pickle

# 1) pickle save
file = open('../data/row_data_binary.pik', mode='wb') # wb : write binary
pickle.dump(rows, file) # list -> binary
print('pickle file save')
file.close()

# 2) pickle load
file2 = open('../data/row_data_binary.pik', mode='rb') # # rb : read binary
rows_data = pickle.load(file2)
print(rows_data) # [{'id': 76811, 'url': 'https://api.github.com/repos/pandas-dev/pandas/labels/Bug', 'name': 'Bug', 'color': 'e10c02',
print(type(rows_data)) # <class 'list'>
