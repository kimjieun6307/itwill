'''
 문4) 패토리얼(Factorial) 계산 함수를 정의하시오.
     예) 5! -> 5*4*3*2*1 : 120
'''

def Factorial(n):
    if n==1 :
        return 1
    else:
        fac=n*Factorial(n-1)
        return fac

result_fact = Factorial(5)  
print()  
print('패토리얼 결과:', result_fact) #  패토리얼 결과: 120
#-----------------------------------
def Factorial(n):
    if n==1 :
        return 1
    else:
        fac=n*Factorial(n-1)
        return fac

Factorial(5)  # 120
print('패토리얼 결과:', Factorial(5))

#----------종료조건(n==0) 으로 하면 오류----------------------------
def Factorial(n):
    if n==0 :
        return 0
    else:
        fac=n*Factorial(n-1)
        return fac

result_fact = Factorial(5)
print('패토리얼 결과:', result_fact) # 패토리얼 결과: 0



