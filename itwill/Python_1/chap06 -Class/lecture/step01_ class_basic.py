'''
클래스(class)
 - 함수의 모임
 - 역할 : 다수의 함수와 공유 자료를 묶어서 객체(object)를 생성
 - 유형 : 사용자 정의 클래스, 라이브러리 클래스(python)
 - 구성요소 : 멤버(member) + 생성자
 - 멤버(member) : 변수(자료 저장) + 메서드(자료 처리-(함수))
 - 생성자 : 객체 생성
 형식)
 class 클래스명 :
    멤버변수=자료
    def 멤버메서드() :
        자료처리
    생성자 : 객체 생성
'''

# 1. 중첩함수
def calc_func(a, b) : # outer 함수 : 자료 저장, inner함수 포함
    # 자료 저장 (inner함수가 자료를 처리할 수 있게 끔 자료 저장)
    x = a
    y = b

    # inner 함수 : 자료 처리(조장)
    def plus () :
        return  x + y
    def minus() :
        return  x - y
    return plus, minus

p, m = calc_func(10, 20) # 일급함수 : 함수가 객체로 저장되는 것.
print('plus = ', p()) # plus =  30
print('minus = ', m()) # minus =  -10

print('plus = ', p) # plus =  <function calc_func.<locals>.plus at 0x000001EA3E2DC948>
print('minus = ', m) # minus =  <function calc_func.<locals>.minus at 0x000001EA3E2DCAF8>
# 함수 이름을 호출해서 데이터 실행
# class 차이점은 생성자가 있다는 것.

# 2. 클래스 정의
class clac_class : # 괄호()가 없음.
    # 멤버 변수(전역변수) : 자료 저장
    x = y = 0 # 0으로 초기화

    # 생성자  : 객체 생성 + 멤버 변수 값 초기화     --->함수 이름 정해져 있음.(def __init__(self))
    # 클래스 내의 함수는 'self' 매개 변수를 가지고 있고, 'self'는 객체와 멤버 변수를 이어주는 매개체 역할
    def __init__(self, a, b): # 외부에서 받을 인수 a, b
        # 멤버변수 초기화
        # self.멤버변수 = 지역변수
        self.x = a
        self.y = b
     #@@1
    # 멤버 메서드 : 클래스에서 정의한 함수 (일반함수와 동일한데 self변수 가진다는 차이점 있음.)
    def plus(self):
        return self.x +self.y
    def minus(self):
        return self.x - self.y

# 클래스(1) -> 객체(n)
# 생성자 -> 객체1(object)
obj1 = clac_class(10, 20) # 클래스명() : 생성자 -> 객체1(obj1) 생성
# object.member() : 메서드 호출
obj1.plus() # 30
obj1.minus() # -10
#@@2
# object.member : 멤버변수 호출
obj1.plus # <bound method clac_class.plus of <__main__.clac_class object at 0x000001EA3DF4B308>>
obj1.x # 10
obj1.y # 20

# 생성자 -> 객체2(obj2)
obj2 = clac_class(100, 200)

print(obj2) # <__main__.clac_class object at 0x000001EA3DF4BDC8>

print('plus = ', obj2.plus()) # plus =  300
print('minus = ', obj2.minus()) # minus =  -100
print('x =',obj2.x) #: x = 100
print('y =',obj2.y) #: y = 200

# 객체 주소 확인
print(id(obj1), id(obj2)) # 2105573421832 2105573424584  --- 서로 다른 주소(저장 위치가 다르다)

# 3. 라이브러리 클래스
# 함수인지 클래스 인지 확인은 ctrl + 클릭해서 소스 확인해야 함.
from datetime import date # from 모듈 import 클래스
#@@5
today = date(2020, 4, 13) # 생성자 -> 객체

print(today) # 2020-04-13

# object. member
print('year : ', today.year) # year :  2020
print('month : ', today.month) # month :  4
print('day : ', today.day) # day :  13

#object. method()
week = today.weekday()
print('week : ', week) # week :  0 (-> 0=월요일)
#@@6


