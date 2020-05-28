'''
set 특징
 - 순서 없음(index 사용불가)
 - 중복 허용 불가
    형식) 변수 ={값1, 값2, ...}
 - 집합 개념 : 합집합, 차집합, 교집합
 - 원소 추가(.add) /삭제(.discard)
'''

s = {1, 3, 5}
print(len(s)) # 3

s1 = {1, 3, 5, 1, 5}
print(len(s1)) # 3  ---> 1, 5 중복

for d in s1 :
    print(d, end=' ') # 1 3 5

s2 = {3,6}
print(s.union(s2)) #합집합 : {1, 3, 5, 6}
print(s.difference(s2)) # 차집합 : {1, 5}
print(s.intersection(s2)) # 교집합 : {3}

# list : gender
gender = ['남자', '여자', '남자', '여자'] # 중복 허용
# list -> set
sgender = set(gender) # 중복 불가
print(sgender) # {'여자', '남자'}
print(sgender[0]) #TypeError

# set -> list
lgender = list(sgender)
print(lgender[0]) # 여자

# 원소 추가/삭제
s3 ={1, 3, 5, 7}
print(s3, type(s3)) # {1, 3, 5, 7} <class 'set'>

s3.add(9) # 원소 추가
print(s3) # {1, 3, 5, 7, 9}

s3. discard(3) #원소 삭제
print(s3) # {1, 5, 7, 9}
