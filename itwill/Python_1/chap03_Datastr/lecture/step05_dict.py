'''
dict 특징
 - set 구조와 유사함 (순서 없음=index 사용 불가)
 - R의 list 유사함
 - key와 value 한 쌍으로 원소 구성
 - key를 이용해서 value 참조
 - key 중복 불가, value 중복 가능
 형식) 변수 ={key:value, key:value}
'''

# 1. dict 생성
# 방법1)
dic = dict(key1 = 100, key2 = 200, key3 = 300)
print(dic, len(dic), type(dic))
# {'key1': 100, 'key2': 200, 'key3': 300} 3 <class 'dict'>

# 방법2)
dic2 = {'name':'홍길동', 'age':35, 'addr':'서울시'}
print(dic2)

# 2. 수정, 추가, 삭제, 검색 : key 이용
dic2['age']=45 # 수정 {'name': '홍길동', 'age': 45, 'addr': '서울시'}
dic2['pay']=350 # 추가 {'name': '홍길동', 'age': 45, 'addr': '서울시', 'pay': 350}
del dic2['addr'] # 삭제 {'name': '홍길동', 'age': 45, 'pay': 350}

# 키 검색
print('age' in dic2) # True

# 3. for 이용
for k in dic2 : # == for k in dic2.keys()
    print(k) # key
''' 넘어오는 key 값은 순서 없음.
name
age
pay
'''
for k in dic2.keys() :
    print(k, end='->') # key
    print(dic2[k]) # value
'''
name->홍길동
age->45
pay->350'''

for v in dic2.values(): # 값 넘김
    print(v)
'''
홍길동
45
350'''

for k, v in dic2.items() : # 키, 값 넘김
    print(k, end='->')
    print(v)
'''
name->홍길동
age->45
pay->350'''

for d in dic2.items() : # 키, 값 넘김
    print(d) # (키, 값) ---tuple
''' tuple 자료형으로 반화됨.
('name', '홍길동')
('age', 45)
('pay', 350)'''

# 4. key -> value
print(dic2['name']) # index 형식 : 홍길동
print(dic2.get('name')) # get() : 홍길동

# 5. {'key' : [value1, value2]}
# ex) {'이름' : [급여, 수당]}
emp = {'hong':[250, 50], 'lee':[350, 80], 'yoo':[200,40]}
print(emp)
#{'hong': [250, 50], 'lee': [350, 80], 'yoo': [200, 40]}

for k, v in emp.items() :
    print(k, end='->')
    print(v)
'''
hong->[250, 50]
lee->[350, 80]
yoo->[200, 40]'''

# 급여 250 이상인 사원 정보 출력
for k, v in emp.items() :
    if v[0] >=250 :
        print(k, end='->')
        print(v)
'''
hong->[250, 50]
lee->[350, 80]'''

# 급여 250 이상인 경우 사원명, 수당 합계
su=0
for k, v in emp.items() :
    if v[0] >= 250:
        print(k)
        su +=v[1]
print('수당 합계 =', su)
'''
hong
lee
수당 합계 = 130
'''
# 급여 250 이상인 사원의 실수령액(급여 + 수당)
for k, v in emp.items() :
    if v[0] >= 250:
        print(k, sum(v))
'''
hong 300
lee 430
'''

# 6. 문자 빈도수 구하기
charset = ['love','test', 'love', 'hello', 'test', 'love']
print(len(charset)) #6

# 방법1) wc[word] = 1, wc[word] += 1
wc ={} # 빈 set
for word in charset :
    if word in wc :
        wc[word] += 1 # 2회 이상 발견 : 1씩 증가
    else:
        wc[word] = 1 # 최초발견 : 1를 초기화 ==> wc ={'love':1}
print('워드 카운트 : ', wc)
# 워드 카운트 :  {'love': 3, 'test': 2, 'hello': 1}
print(max(wc, key=wc.get)) # love --- 빈도수 가장 많은 key

# 방법2) .get(word, 0)+1
wc2 = {}
for word in charset:
    wc2[word] = wc2.get(word, 0)+1
print(wc2)
#{'love': 3, 'test': 2, 'hello': 1}

