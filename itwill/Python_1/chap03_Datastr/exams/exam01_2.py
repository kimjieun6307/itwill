'''
step2 관련 문제 

A형 문) vector 수를 키보드로 입력 받은 후, 입력 받은 수 만큼 
          임의 숫자를 vector에 추가하고, vector의 크기를 출력하시오.
          
<출력 예시>
vector 수 : 3
4
2
5
vector 크기 : 3

     
B형 문) vector 수를 키보드로 입력 받은 후, 입력 받은 수 만큼 
          임의 숫자를 vector에 추가한다. 
          이후 vector에서 찾을 값을 키보드로 입력한 후 
          해당 값이 vector에 있으면 "YES",  없으면 "NO"를 출력하시오. 
          
<출력 예시>
vector 수 : 5
1
2
3
4
5
3
YES

vector 수 : 3
1
2
4
3
NO
'''

# A형 문제 
size = int(input('vector 수 : ')) # vector 크기 입력 # <class 'int'>
'''
import random
vector=[]
for i in range(size):
    vector.append(random.randint(1, 9))
print(vector)
'''
# A형 문제
size = int(input('vector 수 : '))
vector=[]
for i in range(size):
    x=random.randint(1, 9)
    vector.append(x)
    print(x)
print('vector 크기 : ', len(vector))
#------------------------------------
size = int(input('vector 수 : '))
lst=[]
for i in range(size):
    lst.append(int(input())) # list에 숫지ㅏ 입력(prompt 없음)

print("vector 크기 : ", len(lst))

# B형 문제
if int(input()) in lst :
    print('Yes')
else:
    print('NO')
#-------------------------------
size = int(input('vector 수 : '))
vector=[]
for i in range(size):
    x=random.randint(1, 9)
    vector.append(x)
    print(x)
num=int(input("찾을 값 : "))
if num in vector:
    print("찾았다.!!")
else:
    print("없네..")






