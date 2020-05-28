'''
 문) 동적 멤버 변수 생성으로 다음과 같은 산포도를 구하는 클래스를 정의하시오.
 
class Scattering :         
        
        생성자  : 객체 + 동적멤버생성
        
        분산 함수(var_func)
        var = sum((x-mu)**2)/(n-1)
        
        표준편차 함수(std_func)
        std = sqrt(var)
        
        
   << 출력 결과 >>
 분산 : 7.466666666666666
 표준편차 :  2.7325202042558927
'''

from statistics import mean
from math import sqrt

x = [5, 9, 1, 7, 4, 6]

# (1)
class Scattering :
    def __init__(self, x):
        self.x =x
    def var_func(self):
        temp = [(i-mean(self.x))**2 for i in x]
        self.var = sum(temp) / (len(self.x)-1)
    def std_func(self):
        self.std = sqrt(self.var)

result = Scattering(x)
result.var_func()
print(result.var) # 매서드 실행해야 결과 값 나옴.
result.std_func()
print(result.std)

#---------------------------------------------------
# (2)
class Scattering:
    def __init__(self, x):
        self.x = x

    def var_func(self):
        temp = [(i - mean(self.x)) ** 2 for i in x]
        var = sum(temp) / (len(self.x) - 1)
        return var

    def std_func(self):
        std = sqrt(self.var_func())
        return std


sca_obj = Scattering(x)
print(sca_obj.var_func())  # 7.466666666666666
sca_obj.std_func()  # 2.7325202042558927


''' error
class Scattering :  
    def __init__(self, x):
        self.x = x
        
    def var_func(self):
        var = sum((self.x-mean(self.x))**2)/(len(self.x)-1)
        return var
    def std_func(self):
        std = sqrt(self.var_func())
        return std
    
sca = Scattering(x)

print(sca.var_func())
print(sca.std_func())
'''





 
        
    
    



