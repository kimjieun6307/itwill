'''
tuple 특징
 - index 사용, 순서 존재
 - 1차원 배열 구조
 - 수정 불가, 처리 속도 빠름
 - 제공 함수 없음(추가append, 삽입insert, 삭제remove 안됨)
    형식) 변수 =(원소1, 원소2, ...)
'''

# 원소가 하나인 경우 주의 사항 : ( ,) 콤마를 넣어줘야 tuple로 인식
tp = 10 #scala
tp1 = (10) #scala
tp2 = (10,) #tuple
print(tp, tp1, tp2)
print(type(tp), type(tp1), type(tp2))
#<class 'int'> <class 'int'> <class 'tuple'>

# index
tp3 = (10, 58, 4, 96, 55, 2)
print(tp3[:4]) # (10, 58, 4, 96)
print(tp3[-3:]) # (96, 55, 2)

# 수정 불가
tp3[0] = 100 # TypeError

# max/min 찾기
vmax=vmin= tp3[0] # 첫번째 원소 -> 초기화
for t in tp3 :
    if vmax < t:
        vmax = t
    if vmin > t:
        vmin = t
print("최댓값 : ", vmax) # 최댓값 :  96
print("최소값 : ", vmin) # 최소값 :  2

# list -> tuple
lst = list(range(10000))
print(len(lst))

tlst = tuple(lst)
print(type(tlst)) # <class 'tuple'>

