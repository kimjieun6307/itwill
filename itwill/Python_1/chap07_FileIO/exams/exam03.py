'''
문) emp.csv 파일을 읽어와서 다음 출력 예시와 같이 처리하시오. 
 
       <<출력 예시>>
관측치 길이 :  5
전체 평균 급여 : 370.0
==============================
최저 급여 : 150, 이름 : 홍길동
최고 급여 : 500, 이름 : 강감찬
==============================
'''
import pandas as pd

# 1. file read
emp = pd.read_csv('./chap07_FileIO/data/emp.csv', encoding='utf-8')
print(emp.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   No      5 non-null      int64 
 1   Name    5 non-null      object
 2   Pay     5 non-null      int64 
dtypes: int64(2), object(1)
memory usage: 248.0+ bytes
None
'''

pay=emp['Pay']
name = emp['Name']

print("관측치 길이", len(pay))
print('전체 평균 급여 : ', pay.mean())
print('='*30)

for i in range(len(pay)):
    if pay[i] == min(pay):   # min(pay)==pay.min()
        min_name = name[i]
    elif pay[i] == max(pay):
        max_name = name[i]
print('최저 급여 : ', min(pay), '이름 : ', min_name)
print('최고 급여 : ', max(pay), '이름 : ', max_name)


for i, p in enumerate(pay):
    if p==min(pay) :
        print(f"최저 급여 : {p}, 이름 : {name[i]}")
    if p == max(pay):
        print(f"최고 급여 : {p}, 이름 : {name[i]}")
print('='*30)

'''
관측치 길이 5
전체 평균 급여 :  370.0
==============================
최저 급여 :  150 이름 :  홍길동
최고 급여 :  500 이름 :  강감찬
==============================
'''


       
