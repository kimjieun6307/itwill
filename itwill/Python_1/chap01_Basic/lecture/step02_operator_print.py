'''
연산자(Operator
1. 변수에 값 할당(=)
2. 연산자 : 산술, 관계, 논리
3. print 형식
4. input : 키보드 입력
'''

# 1. 변수에 값 할당(=)
i = tot = 10
i += 1 # i = i+1
tot += i # tot= tot+i
print('i=', i) # i= 11
print('tot=', tot) #tot= 21

# 변수 값 교체
v1, v2 = 100, 200
print('v1=', v1, 'v2=', v2) #v1= 100 v2= 200
v1, v2 = v2, v1
'''
tmp = v1
v1 = v2
v2 = tmp
'''
print('v1=', v1, 'v2=', v2) #v1= 200 v2= 100

# 패킹(packing) 할당
lst = [1,2,3,4,5,] # (R에서 vector : 1차원)
v1, *v2 = lst
print('v1=', v1, 'v2=', v2)
# v1= 1 v2= [2, 3, 4, 5]
*v1, v2 = lst
print('v1=', v1, 'v2=', v2)
# v1= [1, 2, 3, 4] v2= 5

# 2. 연산자 : 산술, 관계, 논리
num1 = 100 # 피연산자1
num2 = 20.5 # 피연산자2

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2 # 실수 몫
div2 = num1 // num2 # 정수 몫
div3 = num1 % num2 # 나머지 계산
print(add, sub, mul) # 120.5 79.5 2050.0
print(div, div2, div3) # 4.878048780487805 4.0 18.0
square = num1**2 # pow rPtks
print(square) # 10000

print("관계연산자")  # True or False
# 1) 동등비교
bool_re = num1 == num2
print(bool_re) # False
bool_re = num1 != num2
print(bool_re) # True

# 2) 대소 관계 : >, >=, <, <=
bool_re = num1 <= num2
print(bool_re) # False

bool_re = num1 >= num2
print(bool_re) # True

print("논리 연산자") # or, and, not
bool_re = num1>=num2 or num1<=10
print(bool_re) # True

bool_re = num1>=num2 and num1<=10
print(bool_re) # False

bool_re = not(num1 <= 10)
print(bool_re) # True

# 3. print 형식
help(print) #함수 도움말
# package > module > function or class
# Help on built-in function print in module builtins:
# print(value, ..., sep=' ', end='\n') ---파라미터(기본값)
# module builtins : 기본 모듈(python 설치 시 자동으로 설치되는 모듈)
# built-in : 내장함수

'''
함수의 인수
매개변수 : 값을 넘겨 받는 변수 (value)
파라미터 : 값을 갖는 변수 (기본값)
'''

# 1) 기본 인수
print("values = ", 10+20+30) #values =  60
print("출력1", end=', ')
print('출력2') # 출력1,출력2
print("101", "111", "222", sep="-") #101-111-222

# 2) format(value, '형식')
# - 빌트인 내장함수
#@@4
print("원주율=", format(3.14159, "8.3f")) # 원주율=    3.142
print("금액 =", format(10000, "10d")) # 금액 =      10000
print("금액 =", format(125000, "3,d")) # 금액 = 125,000

# 3) print("양식문자" %(값))  # 양식문자(p.22)
num1 = 10 ; num2 = 20
tot = num1 + num2
print("%d + %d = %d"%(num1, num2, tot)) # 10 + 20 = 30
print("8진수 = %o, 16진수 = %x"%(num1, num2)) # 8진수 = 12, 16진수 = a
print("%s = %8.3f"%("PI", 3.14159)) # PI =    3.142

# 4) 외부 상수 받기
# "{}, {}".format(value1, value2)
print("name : {}, age : {}".format("홍길동", 35)) # name : 홍길동, age : 35
print("name : {1}, age : {0}".format(35, "홍길동")) # name : 홍길동, age : 35
'''
print("age : {2}, name : {1}".format("홍길동", 35))
Traceback (most recent call last):
  File "<input>", line 1, in <module>
IndexError: tuple index out of range
'''
print("age : {1}, name : {0}".format("홍길동", 35)) # age : 35, name : 홍길동

# format 축약형 : sql
# select * from emp where name = '홍길동'
name = '홍길동'
age = 35
sql = f"select * from emp where name ='{name}' and age={age}"
print(sql) # select * from emp where name ='홍길동' and age=35

# 4. input ("prompt") : 키보드 입력
a=input("첫번째 숫자 입력 : ") #10
b=input("두번째 숫자 입력 : ") #20
print("a+b = ", a+b) # a+b =  1020 --- 문자로 인식
#@@6
a=int(input("첫번째 숫자 입력 : ")) #10 string -> int
b=int(input("두번째 숫자 입력 : ")) #20 string -> int
print("a+b = ", a+b) # a+b =  30
#@@7
'''
형 변환 관련 함수
int(value) : value -> integer
fluat(value) : value -> float
str(value) : value -> string
bool(value) : value -> boolean
'''
a=float(input("첫번째 숫자 입력 : ")) # string -> float
b=float(input("두번째 숫자 입력 : ")) # string -> float
print("a+b = ", a+b) # a+b =  24.457
print('b=', b) # b= 12.0
print(type(b)) # <class 'float'>

# boolean -> int
print(int(False)) # 0
print(int(True)) # 1

# int -> boolean
print(bool(1)) # True
print(bool(0)) # False
print(bool(1245)) # True
print(bool(-1245)) # True