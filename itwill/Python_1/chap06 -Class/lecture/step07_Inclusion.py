'''
1. private 변수 = 클래스 내의 은닉변수 (보안목적)
    object.member : 객체 -> 은닉변수(x)
    getter()/setter() -> 은닉변수(o)

2. class 포함관계 (inclusion)
 - 특정 객체가 다른 객체를 포함하는 클래스 설계 기법
 - 두 객체 간의 통신 지원
 - ex) class A(a) -> class B(b)
'''

# 1. private 변수
class Login : # uid, pwd -> db 저장
    # 생성자
    def __init__(self,uid, pwd):
        # self.__private
        self.__dbId = uid
        self.__dbPwd = pwd

# object
login=Login('hong', '1234')
#object.member
print(login.__dbId) # AttributeError: 'Login' object has no attribute '__dbId'

#-----------------------------------------------------------
class Login:  # uid, pwd -> db 저장
    # 생성자
    def __init__(self, uid, pwd):
        # self.__private
        self.__dbId = uid
        self.__dbPwd = pwd

    # getter() : 획득자(return)
    def getIdPwd(self):
        return self.__dbId, self.__dbPwd

    # setter() : 지정자(인수)
    def setIdPwd(self, uid, pwd):
        self.__dbId = uid
        self.__dbPwd = pwd

# object
login = Login('hong', '1234')
# object.member
print(login.__dbId) # AttributeError: 'Login' object has no attribute '__dbId'

# object.getter()
uid, pwd = login.getIdPwd()
print(uid, pwd, sep=',') # hong,1234

# object.setter()
login.setIdPwd('lee', '2345') # 변수 수정

uid, pwd = login.getIdPwd() # 변수 확인
print(uid, pwd, sep=',') # lee,2345

# Server <-> Login
class Server :
    # 기본 생성자

    # 멤버 메서드
    def send(self, obj): #object 인수로 받음
        self.obj = obj # 멤버 변수 생성

    # 인증 메서드
    def cert(self, uid, upwd): # 사용자(id/pwd)
        dbId, dbPwd = self.obj.getIdPwd() # getter 메서드 호출
        if dbId == uid and dbPwd ==upwd:
            print('로그인 성공!')
        else:
            print('로그인 실패..')

server=Server()
server.send(login) # objet 넘심
server.cert('hong', '1234') # 로그인 실패..
server.cert('lee','2345') # 로그인 성공!






