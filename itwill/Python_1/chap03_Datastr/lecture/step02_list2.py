'''
리스트 내포
 - list 에서 for문 사용
    형식1) 변수 = [실행문 for 변수 in 열거행객체]
        실행순서 : 1. for문 -> 2. 실행문 -> 3. 변수 저장
    형식 2) 변수 = [실행문 for 변수 in 열거행객체 if 조건식]
        실행순서 : 1. for문 -> 2. if문 -> [3. 실행문 -> 4. 변수 저장]
'''
# 형식1) 변수 = [실행문 for 변수 in 열거행객체]
# x각 변량에 제곱 (x**2)
x= [2, 4, 1, 3, 7]
data=[]
for i in x :
    print(i**2)
    data.append((i**2))
print(data) # [4, 16, 1, 9, 49]

# data2=[실행문 for i in x]
data2=[i**2 for i in x]
print(data2) # [4, 16, 1, 9, 49]

# 형식 2) 변수 = [실행문 for 변수 in 열거행객체 if 조건식]
# 1~100에서 3의 배수만
num=list(range(1,101)) # 1~100
print(num)

data3=[i for i in num if i%3==0]
print(data3)
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]

# 내장함수 + 리스트 내포
print('sum = ', sum(x))  # sum =  17
data4=[[1,3,5],[4,5],[7,8,9]] # 중첩 list
result = [sum(d) for d in data4]
print(result) # [9, 9, 24]
