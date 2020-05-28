'''
중첩함수 -> 클래스(data + function)

# chap05_exams 03 중첩함수
def bank_account(bal):
    balance = bal  # 잔액(balance) : outer변수

    def getBalance():  # 잔액확인(getter)
        return balance

    def deposit(money):  # 입금하기(setter)
        nonlocal balance
        balance += money

    def withdraw(money):  # 출금하기(setter)
        nonlocal balance
        if balance >= money:
            balance -= money
        else:
            print('잔액이 부족합니다.')

    return getBalance, deposit, withdraw  # 클로저 함수 리턴
'''

class bank_account: # outer -> class
    # outer 변수 -> 멤버변수
    balance = 0  # 잔액(balance) ---> 생략가능

    # 생성자
    def __init__(self, bal):
        self.balance = bal # 멤버변수 초기화

    #inner -> 멤버메서드
    def getBalance(self):  # 잔액확인(getter)
        return  self.balance

    def deposit(self, money):  # 입금하기(setter)
        self.balance += money

    def withdraw(self, money):  # 출금하기(setter)
        if self.balance >= money:
            self.balance -= money
        else:
            print('잔액이 부족합니다.')

acc=bank_account(1000)
print('잔액 : ', acc.getBalance()) # 잔액 :  1000
acc.deposit()# TypeError: deposit() missing 1 required positional argument: 'money'
acc.deposit(20000) # 2만원 입금
print('잔액 : ', acc.getBalance()) # 잔액 :  21000
acc.withdraw(5000) # 5천원 인출
print('잔액 : ', acc.getBalance()) # 잔액 :  16000

'''
1. 예금주(accName), 계좌번호(accNo) 동적 멤버변수 추가하기
 -> 예금주 : 홍길동, 계좌번호 : 012-125-41520
2. getBalance() 메서드를 이용하여 잔액, 예금주, 계좌번호 출력하기
'''
class Account:
    balance = 0

    def __init__(self, bal, name, no):
        self.balance = bal
        self.accName = name
        self.accNo =  no

    def getBalance(self):
        return  self.balance, self.accName, self.accNo

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        if self.balance >= money:
            self.balance -= money
        else:
            print('잔액이 부족합니다.')

acc2=Account(1000, '홍길동','012-125-41520')
print('잔액 : {}, 예금주 : {}, 계좌번호 : {}'.format(acc2.getBalance())) # IndexError: tuple index out of range
print('잔액 : {}, 예금주 : {}, 계좌번호 : {}', format(acc2.getBalance())) # 잔액 : {}, 예금주 : {}, 계좌번호 : {} (1000, '홍길동', '012-125-41520')

bal, name, no = acc2.getBalance()
print('잔액 : {}, 예금주 : {}, 계좌번호 : {}'.format(bal, name, no)) # 잔액 : 1000, 예금주 : 홍길동, 계좌번호 : 012-125-41520