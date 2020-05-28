'''
함수의 가변인수
 - 한개의 가인수로 여러개의 실인수를 받는 인수
  형식) def 함수명(*인수)
'''

# 1. tuple형으로 받는 가변인수 : *매개변수
def Func1(name, *names):
    print(name)
    print(names)
    print(names[0])

Func1('홍길동', '이순신', '유관순')
'''<반환값>
홍길동
('이순신', '유관순') ---> 열거형으로 tuple타입
'''
def Func1(name, *names):
    print(names[0]) # tuple타입이라서 순서 있음. 첫번째 인텍스만 사용할수도 있음.
Func1('홍길동', '이순신', '유관순') # 이순신

# 방법1) import 패키지.모듈
import scatter.scatter_module
# 방법2) from 패키지.모듈 import 함수1, 함수2, 클래스1, 클래스2
from scatter.scatter_module import Avg, var_std

datas =[2, 3, 5, 6, 7, 8.5]
avg1 =scatter.scatter_module.Avg(datas) # 방법1
avg2 = Avg(datas) # 방법2
print(avg1) # 5.25
print(avg2) # 5.25

var, std = var_std(datas)
print('var =', var) # var = 5.975
print('std = ', std) # std =  2.444381312316063

from statistics import variance, stdev
print(variance(datas)) # 5.975
print(stdev(datas)) # 2.444381312316063

def statis(func, *data) :
    if func == 'sum' :
        return sum(data) # 함수 실행 종료(반복문에서 exit와 같은 의미)
    elif func == 'avg' :
        return Avg(data)
    elif func == 'var' :
        return var_std(data)
    elif func == 'std' :
        return var_std(data)
    else:
        return '해당 함수 없음'

print('sum= ', statis('sum',1,2,3,4,5)) # sum=  15
#statis 함수에서 'sum' -> func으로 받고, 나머지 값은 가변수(*data)로 받아서 함수 실행

print('avg= ', statis('avg',1,2,3,4,5)) # avg=  3
var, _ = statis('var', 1,2,3,4,5) # 2개 값이 반환되기 때문데 하나는 사용하지 않는 다는 의미로 ' _ '사용
print(var) # 2.5
_ , std = statis('std', 1, 2, 3, 4, 5,)
print(std) # 1.5811388300841898

''' <ERROR>
a=[1,2,3,4,5]
print('sum= ', statis('sum',a))'''

# 2. dic형 가변인수 : **매개변수
def person(w, h, **other) :
    print('w = ', w)
    print('h = ', h)
    print(other)

person(65, 175, name='홍길동', age = 35)
'''<반환값>
w =  65
h =  175
{'name': '홍길동', 'age': 35}'''

# 3. 함수를 인수로 받기
def square(x):
    return x**2

def my_func(func, datas) :
    result = [func(d) for d in datas]
    return result

datas =[1,2,3,4,5]
print(my_func(square, datas)) # (함수, 데이타셋)
# [1, 4, 9, 16, 25]




