'''
 <급여 계산 문제>
문) Employee 클래스를 상속하여 Permanent와 Temporary 클래스를 구현하시오.
    <조건> pay_pro 함수 재정의     
'''

# 부모클래스 
class Employee : 
    name = None
    pay = 0
    
    def __init__(self,name):
        self.name = name
    
    # 원형 함수 : 급여 계산 함수     
    def pay_pro(self):
        pass

# 자식클래스 - 정규직 
class Permanent(Employee):
    
    # 함수 재정의 : 인수+내용 추가      
    def pay_pro(self, gi, bounus):
        self.pay = gi + bounus # pay = 기본급 + 상여

   
# 자식클래스 - 임시직 
class Temporary(Employee):
    
    # 함수 재정의 : 인수+내용 추가      
    def pay_pro(self, time, tpay):
        self.pay = time*tpay # pay = 시간*시급

p=Permanent("홍길동")
p.pay_pro(1800000, 500000)
# print(p.pay_pro(1800000,500000)) # None
print('이름 : {}, 급여 : {}'.format(p.name, p.pay)) # 이름 : 홍길동, 급여 : 2300000

t=Temporary('유관순')
t.pay_pro(45, 15000)

