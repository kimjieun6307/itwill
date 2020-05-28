'''
반복문(for)

형식)
for 변수 in 열거형객체 :
    실행문
    실행문

열거형객체(iterable) : string, list, tuple, set/dict ---> 반복가능하다
제너레이터 식 : 변수 in 열거형객체(객체에 있는 원소를 순회 -> 변수 넘김)
'''

# 1. string 열거형 객체 이용
string = "나는 홍길동 입니다."
print(len(string)) # 11

for s in string : # 11회(문자)
    print(s, end='/') # 나/는/ /홍/길/동/ /입/니/다/./

for s in string.split() : # split(sep=' ') : 3회(단어)
    print(s, end='/') # 나는/홍길동/입니다./

# 2. list 열거형 객체 이용
help(list)
'''
class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
'''
lst = [1,2,3,4,5] # lst object
print(lst) # object 내용 : [1, 2, 3, 4, 5] --- vector
print(type(lst)) # object type : <class 'list'>
print(len(lst)) # 5

for i in lst :
    print(i, end= '/') # 1/2/3/4/5/

lst2 = []
for i in lst :
    print(i, end= '/')
    lst2.append(i**2) # 원소 추가(순서 보장)
print("\nlst2 : ", lst2)
'''
1/2/3/4/5/
lst2 :  [1, 4, 9, 16, 25]
'''
lst3=lst**2 # Error

# 1~100 원소를 갖는 list 객체 생성  [1, 2, 3, ..., 100]
# range(start, stop:n+1, step:1)
lst3 = list(range(1, 101))
print(lst3) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ..., 100]


# 3. range 열거형 객체 이용
'''
range(n) : 0 ~ n-1 정수
range(start, stop) : start ~ stop-1 정수
range(start, stop, step) : start ~ stop-1, step 정수
'''
num1 = range(10) # 0~9
num2 = range(1, 10) # 1~9
num3 = range(1, 10, 2) # 1 3 5 7 9
print(num1) # range(0, 10)
print(num2) # range(1, 10)
print(num3) # range(1, 10, 2)

for i in num1 :
    print(i, end= ' ') # 0 1 2 3 4 5 6 7 8 9
print()
for i in num2 :
    print(i, end= ' ') # 1 2 3 4 5 6 7 8 9
print()
for i in num3:
    print(i, end=' ') # 1 3 5 7 9

# 4. list + range 열거형 객체 이용
idx = range(5) # 0~4
print(idx) # range(0, 5)

idx = list(range(5)) # 0~4 : range object -> list object
print(idx) # [0, 1, 2, 3, 4]

for i in idx :
    print(i, end= ' ')
    print(i**2)
'''
 문제) lst1에 1~100 까지 100개의 원소를 갖는 vector를 생성하고,
       lst2에 3의 배수만 저장하기 
'''
lst1=list(range(1, 101))
print(lst1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
print(len(lst1)) # 100

lst2=list(range(3,101,3))
print(lst2)
#[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]

lst2=[]
for i in lst1 :
    if i%3==0:
        lst2.append(i)
print(lst2) # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]

# index 이용 : 분류정확도
y = [1, 0, 2, 1, 0] # 범주형(0, 1, 2)
y_pred = [1, 0, 2, 0, 0] # 예측치

size = len(y) #5
acc = 0
for i in range(size) : # range(5) : 0~4
    fit = int(y[i]==y_pred[i]) # int(True/False) -> 1/0
    acc += fit * 20 # 누적변수

print("분류정확도 = ", acc) # 분류정확도 =  80


# 5. 이중 for문
# 1) 구구단
for i in range(2, 10) : # i = 단수
    print('*** %d단 ***'%(i))
    for j in range(1, 10) : # j = 곱수
        print('%d * %d = %d'%(i, j, (i*j)))
    print() # line skip
#@@3
for i in range(2, 10) : # i = 단수
    print('*** {}단 ***'.format(i)) # print(' ', format(i))와 다름 >>> *** {}단 *** 2
    for j in range(1, 10) : # j = 곱수
        print('%d * %d = %d'%(i, j, (i*j)))
    print()

# 2) 문자열 처리 : for 변수 in 문장
para ="""나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다."""

sents = []
words = []
for sent in para.split('\n') :  # 문단 -> 문장
    sents.append(sent) # 문장 저장
    for word in sent.split() : # 문장 -> 단어
        words.append(word) # 단어 저장

print(sents) #['나는 홍길동 입니다.', '주소는 서울시 입니다.', '나이는 35세 입니다.']
print('문장길이 : ', len(sents)) # 문장길이 :  3
print(words) # ['나는', '홍길동', '입니다.', '주소는', '서울시', '입니다.', '나이는', '35세', '입니다.']
print('단어길이 : ', len(words)) # 단어길이 :  9

# 제너레이터 식 : 변수 in 열거형 객체
'''
for 변수 i 열거형객체 :
    -> 객체의 원소 수 만큼 반복
if 값 in 열거형객체 :
    -> 객체의 원소 중에서 값이 있으면 True, 아니면 False
'''
if '홍길동' in words :
    print("해당 단어 있음")
else :
    print("해당 단어 없음")
# 해당 단어 있음

search = input("검색 단어 입력 : ")
if search in words :
    print("해당 단어 있음")
else :
    print("해당 단어 없음")
#@@5
