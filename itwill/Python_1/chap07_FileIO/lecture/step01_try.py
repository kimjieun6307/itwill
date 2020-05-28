'''
예외 : 프로그램 실행상태에서 예기치 않은 상황(오류)
try :
    예외발생 코드
except :
    예외처리 코드
finally :          ---> (생략가능)
    항상처리 코드
'''
# 예외 발생
print('프로그램 시작')
x=[10, 20, 35.5, 15, 'num', 14.5]
for i in x :
    print(i)
    y= i**2      # 5번째 'num' 원소가 들어오는 순간 오류남==예외발생
    print('y = ', y)
print('프로그램 종료')
#@@1

# 1. 간단한 예외 처리
print('프로그램 시작')
x=[10, 20, 35.5, 15, 'num', 14.5]
for i in x :
    try :
        print(i)
        y= i**2      # 5번째 'num' 원소가 들어오는 순간 오류남==예외
        print('y = ', y)
    except :
        print('예외발생(숫자 아님) : ', i)

print('프로그램 종료')
#@@2

# 2. 유형별 예외 처리
print('유형별 예외처리')
try :
    div = 1000/2.5 # 정상
    print('div = %.3f'%div)
    div2 = 1000/0 # 1차 : 산술적 예외(분모가 0인 경우)
    print('div2 = %.3f'%div2)
    f = open('c:/text.txt') # 2차 : 파일 열기
    num = int(input("숫자 입력 : ")) # 3차 : 기타 예외발생
    print('num = ', num)
except ZeroDivisionError as e: # 분모가 0인 산술적 예외만 잡아주는 클래스(ZeroDivisionError) class as object
    print('예외 발생', e) # 예외 발생 division by zero
except FileNotFoundError as e : # file io 예외처리
    print('예외 발생', e) # 예외 발생 [Errno 2] No such file or directory: 'c:/text.txt'
except Exception as e : # 나머지 예외처리(만능)
    print('기타 예외발생 : ', e)
finally:
    print('프로그램 종료')   # 예외가 발생하던 발생하지 않던 항상 실행되는 프로그램
#@@3,#@@4, #@@5, #@@6

#-만능 예외처리 -------------------------------------------------------------
print('프로그램 시작')
x = [10, 20, 35.5, 15, 'num', 14.5]
for i in x:
    try:
        print(i)
        y = i ** 2  # 5번째 'num' 원소가 들어오는 순간 오류남==예외
        print('y = ', y)
    except Exception as e:
        print('기타 예외발생 : ', e)

print('프로그램 종료')
#@@8, #@@9


