'''
재귀호출(recursive call)
 - 함수 내에서 자신의 함수를 반복적으로 호출하는 기법
 - 반복적으로 변수의 값을 조정해서 연산 수행
 ex) 1~n 누적 합(1+2+3+4+..n)
 - 반드시 종료조건 필요
'''

# 1. 카운터 : 1~n
def Counter(n) :
    if n==0 : # 종료조건
        return  0 # 함수종료
    else:
        Counter(n-1) #재귀호출
        '''
        1. stack : [5(first), 4(5-1), 3(4-1), 2(3-1), 1(2-1)]
        2. stack 역순으로 출력
        '''
        print(n, end=' ') # 2. 카운트 : 1 2 3 4 5

Counter(0) #0
Counter(5) #  1 2 3 4 5
Counter(1) #1

#--------종료 조건(n==1) 일때 오류-------------------------------
def Counter(n) :
    if n==1 : # 종료조건
        return 1 # 함수종료
    else:
        Counter(n-1) #재귀호출
        '''
        1. stack : [5(first), 4(5-1), 3(4-1), 2(3-1), 1(2-1)]
        2. stack 역순으로 출력
        '''
        print(n, end=' ') # 2. 카운트 : 1 2 3 4 5

Counter(5) # 2 3 4 5 ---> 1 없음!!
Counter(1) #1
Counter(0) #error
#-----------------------------------------

# 2. 누적(1+2+3+... +n)
def Adder(n):
    if n== 1 : # 종료조건
        return 1 # 종료
    else:
        result= n+Adder(n-1) # 1. 재귀호출 -> 2. 누적
        '''
        stack : LIFO(후입선출)
        1. stack[5(first), 4(5-1), 3(4-1), 2(3-1)] 1(2-1)
        2. stack 역순으로 누적 : 1+[2+3+4+5] = 15
        '''
        print(result, end=' ') # 3 6 10 15
        return result


Adder(1) #1
Adder(2) # 3 3
Adder(5) # 3 6 10 15 15



def Adder(n):
    if n== 0 : # 종료조건
        return 0 # 종료
    else:
        result= n+Adder(n-1) # 1. 재귀호출 -> 2. 누적
        return result

Adder(1) #1
Adder(2) #3
Adder(5) #15
