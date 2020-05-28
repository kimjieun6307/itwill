'''
 <급여 계산 문제>
문4) Employee 클래스를 상속하여 Permanent와 Temporary 클래스를 완성하시오.     
'''

# 부모클래스 
class Employee : 
    name = None
    pay = 0
    
    def __init__(self,name):
        self.name = name

# 자식클래스 - 정규직 
class Permanent(Employee):
    def __init__(self, name, gi, bonus):
        super().__init__(name)
        self.pay = gi + bonus


# 자식클래스 - 임시직 
class Temporary(Employee):
    def __init__(self, name, time, tpay):
        super().__init__(name)
        self.pay=time * tpay

 
    
empType = input("고용형태 선택(정규직<P>, 임시적<T>) : ")
if empType == 'P' or empType == 'p' :
    name = input('이름 : ')
    gi = int(input('기본급 : '))
    bonus = int(input('상여금 : '))
    p = Permanent(name, gi, bonus)
    print('='*30)
    print('고용형태 : 정규직')
    print('이름 : ', p.name)
    print('급여 : ', format(p.pay, '3,d'))
elif empType == 'T' or empType == 't' :
    name = input('이름 : ')
    time = int(input('작업시간 : '))
    tpay = int(input('시급 : '))
    t = Temporary(name, time, tpay)
    print('='*30)
    print('고용형태 : 임시직')
    print('이름 : ', t.name)
    print('급여 : ', format(t.pay, '3,d'))
else :
    print('='*30)
    print('입력 오류')

#---연습-----------------------------------------
class Employee:
    name = None
    pay = 0

    def __init__(self, name):
        self.name = name


# 자식클래스 - 정규직
class Permanent(Employee):
    gi = bonus = 0
    def __init__(self, name, gi, bonus):
        super().__init__(name)
        self.gi = gi
        self.bonus = bonus
    def sum_pay(self):
        self.pay = self.gi + self.bonus

p = Permanent("홍길동", 1800000, 500000)
print('이름 : ', p.name)
print('급여 : ', format(p.pay, '3,d')) # 급여 :    0
p.sum_pay()
print('급여 : ', format(p.pay, '3,d')) # 급여 :  2,300,000

# 자식클래스 - 임시직
class Temporary(Employee):
    def __init__(self, name, time, tpay):
        super().__init__(name)
        self.time = time
        self.tpay = tpay
    def mul_pay(self):
        self.ttpay = self.time * self.tpay
        return self.ttpay

t = Temporary("유관순", 45, 15000)
print('이름 : ', t.name)
print('급여 : ', format(t.ttpay, '3,d')) # AttributeError: 'Temporary' object has no attribute 'ttpay'
print('급여 : ', format(t.mul_pay(), '3,d')) # 급여 :  675,000
print('급여 : ', format(t.ttpay, '3,d')) # 급여 :  675,000

#----연습-------------------------------------------
class Permanent(Employee):
    gi = bonus = 0

    def __init__(self, name, gi, bonus):
        super().__init__(name)

    def sum_pay(self):
        self.pay = gi + bonus


p = Permanent("홍길동", 1800000, 500000)
print('이름 : ', p.name)
print('급여 : ', format(p.pay, '3,d'))  # 급여 :    0
p.sum_pay()
print('급여 : ', format(p.pay, '3,d'))  # 급여 :  2,300,000