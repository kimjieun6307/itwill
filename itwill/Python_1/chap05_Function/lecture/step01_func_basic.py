'''
함수(Function)
 - 중복 코드 제거
 - 재사용 가능
 - 특정 기능 1개 정의
 - 유형) 사용자 정의 함수, 라이브러리 함수
'''

# 1. 사용자 정의 함수
'''
형식)
def 함수명(매개변수) :
    실행문1
    실행문2
    return 값1, 값2, ...
'''

# 1) 인수가 없는 함수
def userFunc1():
    print('인수가 없는 함수')
    print('userFunc1')
userFunc1() # 인수가 없는 함수 userFunc1

# 2) 인수가 있는 함수
def userFunc2(x,y):
    adder = x+y
    print('adder =', adder)
userFunc2(10,20) # adder = 30

re=userFunc2(100, 20)
print(re) # None

#3) 리턴 있는 함수
def userFunc3 (x,y):
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y
    return add, sub, mul, div
a, s, m, d = userFunc3(100, 20)
print('add = ', a) # add =  120
print('sub = ', s) # sub =  80
print('mul = ', m) # mul =  2000
print('div = ', d) # div =  5.0

# 2. 라이브러리 함수
'''
1) built-in :  기본함수
2) import : '모듈.함수()' 이런 형식의 함수는 모듈을 import해야 사용할 수 있다. 
'''
# 1) built-in :  기본함수
# - 특별한 행위 없이 바로 사용할 수 있는 함수
dataset = list(range(1,6))
print(dataset) # [1, 2, 3, 4, 5]

print('sum = ', sum(dataset)) # sum =  15
print('max = ', max(dataset)) # max =  5
print('min = ', min(dataset)) # min =  1
print('len = ', len(dataset)) # len =  5
print('mean = ', mean(dataset)) # NameError: name 'mean' is not defined --- 기본 함수 아님.

# 2) import : 모듈.함수()
import statistics  # 방법1) 통계관련 함수 제공
#@@1
'''
(1) ctrl + 클릭 : module of function source 보기
(2) print(dir(statistics)) # 해당 모듈의 정보
 ['Decimal', 'Fraction', 'StatisticsError', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_coerce', '_convert', '_counts', '_exact_ratio', '_fail_neg', '_find_lteq', '_find_rteq', '_isfinite', '_ss', '_sum', 'bisect_left', 'bisect_right', 'collections', 'groupby', 'harmonic_mean', 'math', 'mean', 'median', 'median_grouped', 'median_high', 'median_low', 'mode', 'numbers', 'pstdev', 'pvariance', 'stdev', 'variance']
'''
print(dir(statistics))
from statistics import mean  # 방법2)

avg1 = statistics.mean(dataset) # 방법1
avg2 = mean(dataset) # 방법2
print('mean1 = ', avg1) # mean1 =  3
print('mean2 = ', avg2) # mean2 =  3








