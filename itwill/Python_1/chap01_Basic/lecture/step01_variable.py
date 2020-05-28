'''
변수(Variable)
 - 형식) 변수명 = 값 or 수식 or 변수명 (R 변수와 동일)
 - 자료를 저장하는 메모리 이름
 - type 선언 없음(R 동일)
'''

# 1. 변수와 자료형
var1 = "Hello python"
var2 = 'Hello python'
print(var1) #line skip
print(var2)

# type() : 변수 자료형 확인
# -'str' 문자형, 'int' 정수, 'float' 실수형, 'bool' T/F
print(type(var1)) # <class 'str'>
print(type(var1), type(var2)) # <class 'str'> <class 'str'>

var1=100
print(var1, type(var1)) # 100 <class 'int'> --자료형이 동적으로 변경된다.

var3 = 150.25
print(var3, type(var3)) # 150.25 <class 'float'>

var4 = True # False
print(var4, type(var4)) # True <class 'bool'>

# 2. 변수명 작성규칙(p.11참조)
# 대소문자 구분
_num10 = 10
_NUM10 = 20
print(_num10, _NUM10) # 10 20
print(id(_num10), id(_NUM10)) # 140704331562336 140704331562656 -- 저장되는 주소 다름 : 서로 다른 메모리공간에 저장

# 키워드 확인 -- 변수명으로 쓰면 안됨.
import keyword # 모듈 임포트 (R에서 패키지 library 하는 것과 비슷)
py_keyword = keyword.kwlist # 키워드 반환
print("파이썬 키워드 : ", py_keyword)
#파이썬 키워드 :  ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
print('len =', len(py_keyword)) # len = 35

# 낙타체
korScore = 90 # 변수명 = 상수
matScore = 85
engScore = 75

tot = korScore + matScore + engScore # 변수명 = 수식
print("tot = ", tot)

# 3. 참조변수 : 메모리 객체(value)를 참조하는 주소 저장하는 변수
x = 150 # 150객체의 주소
y = 45.23
y2 = y # 변수 복제
x2 = 150 # 기존 객체가 있으면 새로 만들지 않고 주소 반환
# 변수 내용 출력
print(x, y, y2, x2) # 150 45.23 45.23 150
# 변수 주소 출력
print(id(x), id(y), id(y2), id(x2)) # 140704331566816 2534333374704 2534333374704 140704331566816
# 메모리 효율적으로 사용 : 기존 객체가 있으면 새로 만들지 않고 주소만 반환