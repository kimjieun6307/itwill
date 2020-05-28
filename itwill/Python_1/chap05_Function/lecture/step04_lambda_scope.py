'''
lambda : 한줄짜기 함수
scopr : 변수의 범위
'''

'''
1. 축약함수(lambda)
 - 한 줄 함수
  형식) 변수 = lambda 인수 : 리턴값
  ex) lambda x, y : x+y
  
2. scope
 - 전역변수, 지역변수(함수)   
'''

# 1. 축약함수
'''
def adder(x, y) :
    add = x + y
    return add'''
add = lambda x, y : x + y
# [lambda x, y : x + y for 변수 in 열거형객체] : 리스트내포 실행문에 사용

result = add(10, 20)
print(result) # 30

# 2. scope
'''
전역변수 : 전지역에서 사용되는 변수
지역변수 : 특정 지역(함수)에서만 사용되는 변수
'''
x= 50 # 전역변수
def local_func(x) :
    x +=50 # x=100 : 지역변수
    # 해당 함수가 종료되면 자동으로 소멸
local_func(x) # x=50
print('x= ',x) # x=  50
print('x= ',local_func(x)) #x=  None

def local_func(x) :
    x +=50
    return x
local_func(x) # x=50
print('x= ',x) # x=  50
print('x= ',local_func(x)) # x=  100

# --------global 키워드 사용-----------------

def global_func():
    global x # 전역변수
    x += 50 # x= 100

global_func() # 함수 호출
print('x= ', x) # x=  100





