'''
제어문 : 조건물(if), 반복문(while, for)
python 블럭 : 콜론(:)과 들여쓰기

형식1)
if 조건식 :
    실행문
    실행문
'''
var = 10
if var >= 10 :
    print('var = ', var)
    print('var는 10보다 크거나 같다.')
print('항상 실행되는 영역')   # --- if문과 상관없는 영역( if 문 영역은 콜론(:)과 들여쓰기로 구분됨)
'''
형식2) 
if 조건식 : 
    실행문1
else : 
    실행문2
'''
var = 2
if var>=5 :
    print('var는 5보다 크거나 같다.')
else :
    print('var는 5보다 작다.')
# var는 5보다 작다.

# 키보드 점수 입력 -> 60점 이상 : 합격, 미만 : 불합격
score = int(input("점수입력 : "))
if score>=60 :
    print('합격')
else :
    print('불합격')

import datetime # module 임포트
today = datetime.datetime.now() # module.class.method() ---> method() : 함수라고 보면됨.
print(today) # 2020-04-07 11:09:54.567305

# 요일 반환
week=today.weekday()
print(week) # 1 --> 0~4 : 평일 (0-월, 1-화, 2-수, 3-목, 4-금, 5-토, 6-일)

if week >= 5 :
    print("오늘은 휴일")
else:
    print("오늘은 평일") #오늘은 평일

'''
if 조건식 1 :
    실행문 1
elif 조건식 2 : 
    실행문 2
else :
    실행문 3
'''
# 문제) 키보드 점수(score)입력 : A(100~90), B(80), C(70), D(60), F(59미만)
score = int(input("점수 입력(0~100) : "))
if score >=90 :
    print('A학점')
elif score >=80 :
    print('B학점')
elif score >=70 :
    print('C학점')
elif score >=60 :
    print('D학점')
else:
    print('F학점')

# 전역변수 : score, grade
score = int(input("점수 입력(0~100) : "))
if score >=90 :
    grade = 'A학점'
elif score >=80 :
    grade = 'B학점'
elif score >=70 :
    grade = 'C학점'
elif score >=60 :
    grade = 'D학점'
else:
    grade = 'F학점'
print("당신의 점수는 %d점 이고, 등급은 %s이다."%(score, grade))
# 점수 입력(0~100) : >? 78
# 당신의 점수는 78점 이고, 등급은 C학점이다.

#< 블럭 if vs 라인 if >
# 블럭 if
num =9
if num >=5 :
    result = num * 2
else :
    result = num + 2
print(result) # 18

# 라인 if
# 형식) 변수 = 참 if 조건문 else 거짓
result = num *2 if num >= 5 else num + 2
print(result) # 18