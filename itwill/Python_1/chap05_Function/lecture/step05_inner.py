''''''
'''
중첩함수 (inner function)

 형식) 
 def outer_func(인수) : 
    실행문
    def inner_func(인수) :
        실행문
    return inner_func
'''

# 1. 중첩함수 예
def a() : # outer
    print('a 함수')
    def b() : # inner
        print('b함수')
    return b # inner func

a() # outer 함수 호출
'''
a 함수
<function a.<locals>.b at 0x0000018D831084C8> '''
b()  # NameError: name 'b' is not defined
b=a() # outer 호출 -> a함수 = 일급함수
b() # inner 호출 -> b함수

# 2. 중첩함수 응용
'''
inner 함수 종류
getter() : 함수내의 data를 외부 획득자
setter() : 함수내의 data를 지정자(조작) 
'''
def outer_func(data) : #outer 역할 :  데이터 저장, inner 함수 포함
    dataSet =data

    # inner : 데이터 조작
    def tot(): # 합계
        tot_val=sum(dataSet)
        return tot_val
    def avg(tot_val) : # 평균 = 합계 / n
        avg_val = tot_val / len(dataSet)
        return avg_val

    # getter
    def getData():
        return dataSet
    # setter
    def setData(newData):
        nonlocal dataSet # outer 변수
        dataSet = newData #지역변수

    return tot, avg, getData, setData

data=list(range(1,101))
tot, avg, getData, setData = outer_func(data) # 일급함수(tot, avg, get, set)
#@@4
#@@5
tot_val = tot()# 합계 계산
avg_val = avg(tot_val) # 평균 계산
print('tot = ', tot_val) # tot =  5050
print('avg = ', avg_val) # avg =  50.5
print('dataset = ', getData()) # dataset 리턴

newData = list(range(1,51))
setData(newData) # dataset 변경

# getter 이용 : dataSet 확인
print('dataSet = ', getData())


'''
3. 함수 장식자 : Tensorflow2.0에서 적용
 - 기존 함수의 시작부분과 종료부분에 기능을 추가해서 장식 역할

@함수 장식자
def 함수명():
    실행문
'''
# 함수 장식자 작성
def hello_deco(func) : # outer : 함수를 인수로 받음
    def inner() : # inner : 함수 장식하는 역할
        print('-'*20) # 함수 앞부분 데코
        func() # 외부에서 받음 함수 실행
        print('-'*20) # 함수 뒷부분 실행
    return inner

@hello_deco
def hello() :
    print('my name is 홍길동')

# 함수 호출
hello()
'''
--------------------
my name is 홍길동
--------------------
'''

#-------------------------------------------------------
def hello_deco(func) : # outer : 함수를 인수로 받음
    def inner(name) : # inner : 함수 장식하는 역할, hello 인수 받음
        print('-'*20) # 함수 앞부분 데코
        func(name) # 외부에서 받음 함수 실행
        print('-'*20) # 함수 뒷부분 실행
    return inner

@hello_deco
def hello(name) :
    print('my name is '+name)

# 함수 호출
hello('이순신')
'''
--------------------
my name is 이순신
--------------------
'''
#@@6
#-----------------------------------------------------------
# 구구단 장식하기
'''
**** 2단 ****
2 * 1 = 2
    :
2 * 9 = 18
*************
'''
# 함수 장식
def gugu_deco(func) :
    def inner (dan):
        print('**** {}단 ****'.format(dan))
        func(dan)
        print('*'*13)
    return inner

# 구구단 계산
@gugu_deco
def gugu(dan) :
    for i in range(1,10) :
        print('%d * %d = %d'%(dan, i, dan*i))

dan = int(input("구구단 입력(2~9) : "))
gugu(dan)

# 꾸밈뿐만 아니라 인증이나 보안 등의 작업을 진행할때 함수 장식 사용







