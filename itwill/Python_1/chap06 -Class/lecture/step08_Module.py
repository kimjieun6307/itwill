'''
패키지(package) = 폴더 유사함
 - 유사한 모듈 파일을 저장하는 공간
모듈(module) = 파일 유사함
 - 파이썬 파일(*.py)
클래스, 함수
 - 모듈에 포함되는 단위
'''

'''
# from 패키지명.모듈명 import 클래스 or 함수
from ..package_test.module01 import sub # class
from ..package_test.module01 import Adder # funcion

sub = sub(10,20) # 생성자 -> 객체
print('sub = ', sub.calc()) # sub =  -10

print('add = ', Adder(10,20)) # add =  30
add=Adder(20,20)
print('add = ', add) # add =  40
'''

# from 패키지명.모듈명 import 클래스 or 함수
from package_test.module01 import sub
from package_test.module01 import Adder

sub = sub(10,20) # 생성자 -> 객체
print('sub = ', sub.calc()) # sub =  -10

print('add = ', Adder(10,20)) # 함수 호출  # add =  30