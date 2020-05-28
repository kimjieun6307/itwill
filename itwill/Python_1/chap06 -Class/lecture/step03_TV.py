'''
기본(default) 생성자
 - 생성자를 생략하면 기본 생성자가 만들어진다.
 - 묵시적 생성자
 - 객체만 생성하는 역할
'''

class default_cost :
    # 생성자 생략(def __init__(self):)

    def data(self, x, y):
        self.x = x
        self.y = y
    def mul(self):
        re = self.x * self.y
        return re

obj = default_cost() # 기본 생성자
obj.data(10, 20) # data 생성
obj.mul() # 200


# TV class 정의
class TV : # class = 변수(명사, 자료) + 메서드(동사, 자료처리)
    # 멤버 변수 : 자료 저장
    channel = volume = 0
    power = False # 전원 off 상태
    color = None

    # 기본생성자 --->생략해도됨.
    def __init__(self):
        pass
    # 멤버메서드
    def volumUp(self):
        self.volume += 1
    def volumDown(self):
        self.volume -= 1
    def channelUp(self):
        self.channel += 1
    def channelDown(self):
        self.channel -= 1
    def changePower(self):
        self.power = not(self.power) # 반전(T<->F)
    # TV 생성 메서드 : 멤버 변수 초기화 메서드  (---> 생성자가 없다보니깐..)
    def data(self, channel, volume, color):
        self.channel = channel
        self.volume = volume
        self.color = color
    # TV 정보 출력 메서드
    def display(self):
        print("전원 : {}, 채널 : {}, 볼륨 : {}, 색상 : {}".format(self.power, self.channel, self.volume, self.color))

# 객체 생성
tv1 = TV() # 기본 생성자 -> 객체
tv1.display() # 전원 : False, 채널 : 0, 볼륨 : 0, 색상 : None (---> 초기값)
tv1.changePower() # off -> on
tv1.display() # 전원 : True, 채널 : 0, 볼륨 : 0, 색상 : None (---> 초기값)

tv1.data(5, 10, '검정색')
tv1.display() # 전원 : True, 채널 : 5, 볼륨 : 10, 색상 : 검정색
tv1.channelDown() #채널 :  5 -> 4
tv1.volumUp() # 볼륨 : 10 -> 11
tv1.display() # 전원 : True, 채널 : 4, 볼륨 : 11, 색상 : 검정색

'''
문제) tv2 객체를 다음과 같이 생성하시오.
    단계 1) 전원 : False, 채널 : 1, 볼륨 : 1, 색상 : 파랑색
    단계 2) 전원 : True, 채널 : 10, 볼륭 : 15
    단계 3) tv2 객체 정보 출력
'''
tv2 = TV()
tv2.data(1, 1, '파랑색')
tv2.changePower()

''' <error>
for i in (1:9):
    tv2.channelUp()
'''
for i in range(1,15) : # =range(14)
    tv2.volumUp()

for i in range(1,10): # = range(9)
    tv2.channelUp()

tv2.display() # 전원 : True, 채널 : 10, 볼륨 : 15, 색상 : 파랑색

#--------------------------------------------------------------------------------------------------
# TV class 정의 - 생성자 있음.
class TV_class : # class = 변수(명사, 자료) + 메서드(동사, 자료처리)
    # 멤버 변수 : 자료 저장
    channel = volume = 0
    power = False # 전원 off 상태
    color = None

    # 기본생성자
    def __init__(self, channel, volume, color):
        self.channel = channel
        self.volume = volume
        self.color = color

    # 멤버메서드
    def volumUp(self):
        self.volume += 1
    def volumDown(self):
        self.volume -= 1
    def channelUp(self):
        self.channel += 1
    def channelDown(self):
        self.channel -= 1
    def changePower(self):
        self.power = not(self.power) # 반전(T<->F)

    # TV 정보 출력 메서드
    def display(self):
        print("전원 : {}, 채널 : {}, 볼륨 : {}, 색상 : {}".format(self.power, self.channel, self.volume, self.color))

tv3 = TV_class(1,10,'빨강색')
tv3.display() # 전원 : False, 채널 : 1, 볼륨 : 10, 색상 : 빨강색

tv4=TV(5,15,'녹색') # TypeError: __init__() takes 1 positional argument but 4 were given
# ---> 생성자 생략한 기본생성자 class 이기때문에 값 지정 못함.


