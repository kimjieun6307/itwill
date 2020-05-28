'''
문1) 다음 emp '입사년도이름급여'순으로 사원의 정보가 기록된 데이터 있다.
      이 벡터 데이터를 이용하여 사원의 이름만 추출하시오. 

# <출력 결과>
 names = ['홍길동', '이순신', '유관순']
'''

from re import findall

# <Vector data>
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]

# print(findall('[가-힣]{3,}',emp)) --- error

year = [findall(r'^\d{2,}', i)[0] for i in emp]
print(year)

pay = [findall(r'\d{2,}$', i)[0] for i in emp]
print(pay)

# for문 이용한 경우
names=[]
for s in emp:
    tmp =findall('[가-힣]{3,}', s)
    if tmp :
        names.append(tmp[0])
print('names =', names) # names = ['홍길동', '이순신', '유관순']

# list + for 이용한 경우 : 변수=[실행문 for i in 열거형객체]
names1 =[findall('[가-힣]{3,}', i) for i in emp] # [['홍길동'], ['이순신'], ['유관순']]
names2 =[findall('[가-힣]{3,}', i)[0] for i in emp] # ['홍길동', '이순신', '유관순']
print(names1,'\n',names2)


