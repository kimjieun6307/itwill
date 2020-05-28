'''
반복문 (while)

while 조건식 :
    실행문
    실행문
'''

# 카운터 , 누적 변수
cnt = tot = 0 #  변수 초기화
while cnt < 5 : # Tru -> loop(명령문 집합) 실행
    cnt += 1 # 카운터 변수
    tot += cnt # 누적 변수
    print(cnt, tot)
'''
1 1
2 3
3 6
4 10
5 15
'''

# 1~100까지 합 출력
cnt = tot = 0
while cnt < 100 :
    cnt += 1
    tot += cnt
print("1~100까지 합 : %d"%(tot)) # 1~100까지 합 : 5050

cnt = tot = 0
data=[] # 빈 list(짝수 저장)
while cnt < 100 :
    cnt += 1
    tot += cnt
    if cnt % 2==0 :
        data.append(cnt) # 짝수 값 추가
print("1~100까지 짝수 값 : ", data)
# 1~100까지 짝수 값 :  [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]

# 문제) 1~100 사이에서 5의 배수이면서 3의 배수가 아닌 값만 append하기
cnt = 0
data= [] # 5의 배수이면서(and) 3의 배수가 아닌 값 저장

while cnt < 100 :
    cnt += 1
    if (cnt % 5 == 0) and not(cnt % 3==0) :
        data.append(cnt)
print('1~100 사이에서 5의 배수이면서 3의 배수가 아닌 값')
print(data) # [5, 10, 20, 25, 35, 40, 50, 55, 65, 70, 80, 85, 95, 100]

cnt = 0
data= []
while cnt < 100 :
    cnt += 1
    if (cnt % 5 == 0) and cnt % 3!=0 :
        data.append(cnt)
print('1~100 사이에서 5의 배수이면서 3의 배수가 아닌 값')
print(data) # [5, 10, 20, 25, 35, 40, 50, 55, 65, 70, 80, 85, 95, 100]

# 무한loop -> 종료 조건 (break)
while True :
    num = int(input("숫자 입력 : "))
    if num==0 :
        print("프로그램 종료")
        break # 탈축(exit) : 종료조건
    print("num = ", num)
#@@1

# random : 난수 생성
import random # 난수 생성 모듈 import
help(random.random) #random(...) method of random.Random instance : 0~1 난수 생성
help(random.choice) # choice(seq) method of random.Random instance
help(random.randint) # s난수 정수

r = random.random() # 모듈.함수(0~1 난수)
print('r=', r) #r= 0.30419180199602325

# 문제 ) 난수 0.01 미만이면 종료, 아니면 난수 개수 출력
#       종료 조건 : 0.01미만
cnt=0
while True :
    r= random.random()
    cnt += 1
    if r < 0.01 :
        break
print('r = ', r)
print('cnt=', cnt)
#----------------------------------
cnt = 0
while True :
    r = random.random()
    if r < 0.01 :
        break
    else :
        cnt += 1
print('난수 개수 = ', cnt)

r= random.randint(1, 5) # 1~5 난수 정수
print(r) # 5

print(">>>숫지 맟주기 게임<<<")
'''
myInput == computer : 성공(exit) -> 종료조건
myInput > computer : ' 더 작은 수 입력'
myInput <computer : ' 더 큰 수 입력'
'''
computer = random.randint(1, 10)
while True :
    myInput = int(input("예상 숫자 입력 : ")) # 사용자 입력
    if myInput == computer :
        print('~~성공~~')
        break
    elif myInput > computer :
        print('~~더 작은 수 입력~~')
    elif myInput < computer :
        print('~~더 큰수 입력~~')
#@@2

'''
continue vs break
 - 반복문에서 사용되는 명령어
 - continue : 반복을 지속하되 다음 문장 skip
 - break : 반복 멈춤
'''
i = 0
while i < 10 :
    i += 1
    if i == 3 :
        continue # 다음 문장 skip
    if i == 6 :
        break
    print(i, end=' ') # 1 2 4 5

