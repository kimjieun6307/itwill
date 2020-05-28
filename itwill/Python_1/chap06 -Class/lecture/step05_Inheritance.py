'''
클래스 상속(Inheritance)
 - 기존 클래스(부모)를 이용하여 새로운 클래스(자식) 생성 문법
 - 부모 클래스 정의 -> 자식 클래스 생성
 - 상속 대상 : 멤버(o) + 생성자(x) => 생성자 상속 대상 아님
 형식) class 자식클래스(부모클래스) :  # class new_class(old_class)
            멤버(변수 + 메서드)
            생성자

self vs super()
 - self.member : 현재 클래스의 멤버를 호출
 - super().member : 부모 클래스의 멤버 호출 (ex) super().__init__(변수)
'''

# 부모클래스 : old class
class Super1 :
    # 멤버변수 정의 : 데이터 저장
    name=None
    age=0

    # 생성자 : 객체 생성 + 멤버변수 초기화
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 멤버 메서드 : 데이터 처리
    def display(self):
        print("이름 : {}, 나이 : {}".format(self.name, self.age))

# object 생성
s = Super1("부모", 55)
# object.member()
s.display() # 이름 : 부모, 나이 : 55
# 3개의 멤버만 상속됨. => self.name, self.age, super.display()

del super # 메모리상의 super 라는 객체 삭제

# 자식 클래스
class Sub(Super1) :
    # name = None  # 부모 멤버
    # age = 0   # 부모 멤버
    gender = None   # 자식 멤버
    def __init__(self, name, age, gender): # 자식 생성자
        # self.name = name  # 1차 : 자식 생성자 초기화
        # self.age = age
        self.gender = gender
        # 2차 : 부모 생성자 호출
        super().__init__(name, age)
        #Super1.__init__(self, name, age) # ver 3.7

    def display(self) :  # 2개 -> 3개 확장
        print("이름 : {}, 나이 : {}, 성별 : {}".format(self.name, self.age, self.gender))

sub = Sub('자식', 22, '남자')
sub.display() #이름 : 자식, 나이 : 22, 성별 : 남자

#------------------------------------------------------------------------------
# 1. 부모클래스 정의
class Parent :
    # 멤버변수
    name = job = None
    # 생성자
    def __init__(self, name, job):
        self.name = name
        self.job = job
    #멤버 메서드
    def display(self):
        print("이름 : {}, 직업 : {}".format(self.name, self.job))

p=Parent('홍길동', '공무원')
p.display() # 이름 : 홍길동, 직업 : 공무원

# 자식 클래스 1
class Children1(Parent):
    # name = job
    gender = None

    def __init__(self, name, job, gender):
        super().__init__(name, job) # 부모생성자 호출로 초기화
        self.gender = gender # 자식멤버 초기화

    def display(self): #내용 확장
        print("이름 : {}, 직업 : {}, 성별 : {}".format(self.name, self.job, self.gender))

child1=Children1('이순신', '군인', '남자')
child1.display() # 이름 : 이순신, 직업 : 군인, 성별 : 남자

'''
Parent -> Children2
이름 : 유관순, 직업 : 독립열사, 성별 : 여자
'''
class Children2(Parent):
    gender=None
    age = 0
    def __init__(self, name, job, gender, age):
        super().__init__(name, job)
        self.gender = gender
        self.age = age

    def display(self):
        print("이름 : {}, 직업 : {}, 성별 : {}, 나이 : {}".format(self.name, self.job, self.gender, self.age))

child2 = Children2("유관순", "독립열사", "여자", 19)
child2.display() # 이름 : 유관순, 직업 : 독립열사, 성별 : 여자, 나이 : 19




