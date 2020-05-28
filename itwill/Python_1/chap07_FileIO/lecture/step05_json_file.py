'''
JSON 파일
 - 네트워크에서 표준으로 사용되는 파일 형식
 - 파일 형식 : {key:value, key:value}, {key:value, key:value}
 - 활용 예 : 서로 다른 플랫폼(java, python)에서 파일을 공유

 - json 모듈
  1) encoding : file save : python object(list, dict) -> json file
  2) decoding : file read : json file -> python object
'''

import json

# 1. encoding : object -> 문자열(str)
'''
python object -> json 문자열 -> json_file save
형식) json.dumps(object) : json 문자열 반환
'''
user = {'id': 1234, 'name':'홍길동'} #dict 객체
print(type(user)) # <class 'dict'>

json_str = json.dumps(user, ensure_ascii=False) # unicode -> ascii 인코딩 안함
print(json_str) # {"id": 1234, "name": "홍길동"}  ---> 모양은 dict 그대로이지만 타입은 'str'문자형으로 바뀜
print(type(json_str)) # <class 'str'>  ---> 'dict -> str' json문자열로 변경됨

# 2. decoding : 문자열 -> object
'''
json 문자열 -> python object
형식) json.loads(json 문자열)
'''
py_obj = json.loads(json_str)
print(py_obj) # {'id': 1234, 'name': '홍길동'}  ---> 모양은 같지만 json 문자열 "", python object '' 차이점이 있음.
print(type(py_obj)) # <class 'dict'>

# 3. json file read/write

# 1) json file read : decoding
import os
print(os.getcwd()) # C:\ITWILL\3_Python-I\workspace\chap07_FileIO\lecture

file = open("../data/usagov_bitly.txt", mode='r', encoding='utf-8')
data = file.readlines() # 전체 내용 -> 줄단위 읽기
file.close()
print(data)
print(type(data)) # <class 'list'>

# decoding : json 문자열 -> python object
rows = [json.loads(row) for row in data] # row = {'key':value, ...}
print(len(rows)) # 3560
print(type(rows)) # <class 'list'>

for row in rows[:10] :
    print(row) # {'a': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko)...
    print(type(row)) # <class 'dict'> ---> python object

# json object -> DataFrame
import pandas as pd

row_df = pd.DataFrame(rows) # 행렬 자료 구조
print(type(row_df)) # <class 'pandas.core.frame.DataFrame'>
print(row_df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3560 entries, 0 to 3559
Data columns (total 18 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   a            3440 non-null   object 
 1   c            2919 non-null   object 
 2   nk           3440 non-null   float64
 3   tz           3440 non-null   object 
 4   gr           2919 non-null   object 
 5   g            3440 non-null   object 
 6   h            3440 non-null   object 
 7   l            3440 non-null   object 
 8   al           3094 non-null   object 
 9   hh           3440 non-null   object 
 10  r            3440 non-null   object 
 11  u            3440 non-null   object 
 12  t            3440 non-null   float64
 13  hc           3440 non-null   float64
 14  cy           2919 non-null   object 
 15  ll           2919 non-null   object 
 16  _heartbeat_  120 non-null    float64
 17  kw           93 non-null     object 
dtypes: float64(4), object(14)
memory usage: 500.8+ KB
None
'''
print(row_df.head())
print(row_df.tail())
#@@1


# 2. json file write : json encoding
file = open("../data/json_text.txt", mode='w', encoding='utf-8')
print(type(rows)) # python object : <class 'list'>

for row in rows[:100] : # row = {'key':value, ...} :  <class 'dict'>
    josn_str = json.dumps(row) # dict -> json str
    file.write(josn_str)
    file.write('\n') # 줄바꿈

print('file 저장 완료')


# 3. json file read : json decoding
file = open("../data/json_text.txt", mode='r', encoding='utf-8')
data = file.readlines()
print(len(data)) # 100

# json decoding
rows = [json.loads(row) for row in data] # json 문자열 -> python object

rows_df = pd.DataFrame(rows)
print(rows_df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 18 columns):
'''

