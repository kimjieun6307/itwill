'''
1. 메서드 재정의(method override)
 - 부모의 원형 메서드 -> 자식에 원형 메서드를 다시 작성하는 문법
 - 상속관계에서만 나오는 용어
 - 인수, 내용 -> 수정 대상
2. 다형성
 - 상속관계에서만 나오는 용어
 - 한가지 기능 -> 2개 이상 결과 생성(+ -> 덧셈, 결합)
 - 부모 객체 -> (자식1, 자식2) 멤버 호출
'''
# 1. 메서드 재정의(method override)

# 부모 클래스
class Super :
    data = None # 멤버변수

    # 생성자 생략 = 기본생성자 : 객체만 새성

    # 멤버 메서드 : 원형 메서드
    def superFunc(self): # 인수 없음
        pass # 내용 없음

# 자식1
class Sub1(Super) :
    # 멤버 변수 data
    # 멤버 메서드 superFunc 상속됨.
    def superFunc(self, data): # 수정 -> override
        self.data = data
        print('자식1 : data = {}'.format(self.data))

sub1 = Sub1() # 기본생성자
sub1.superFunc('20200414') # 자식1 : data = 20200414

# 자식2
class Sub2(Super) :
    # 멤버 변수 data, 멤버 메서드 superFunc 상속됨.
    def superFunc(self, data):
        self.data = data
        print('지식2 : data = {}'.format(self.data**2))

sub2 = Sub2()
sub2.superFunc(100) #지식2 : data = 10000

# 2. 다형성
sup = Super() # 부모 객체
sub1 = Sub1() # 자식1 객체
sub2 = Sub2() # 자식2 객체

sup = sub1
sup.superFunc(100) #자식1 : data = 100
sup=sub2
sup.superFunc(100) # 자식2 : data = 10000



