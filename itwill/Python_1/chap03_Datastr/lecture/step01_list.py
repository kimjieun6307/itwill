'''
list 특징
 - 1차원 배열 구조
    형식) 변수 = [값1, 값2, ...]
 - 다양한 자료형 저장 가능(str, int, float, bool..)
 - index 사용, 순서 존재
    형식) 변수[index], index=0 부터 시작
 - 값 수정(추가, 삽입, 수정, 삭제)
'''

# 1. 단일 list
lst=[1, 2, 3, 4, 5]
print(lst, type(lst), len(lst)) # [1, 2, 3, 4, 5] <class 'list'> 5

print(f"{lst} \n {type(lst)} \n {len(lst)}")
print(f"(lst) \n (type(lst)) \n (len(lst))")
print(str(lst)+'\n'+str(type(lst))+'\n'+str(len(lst)))
#@@1

for i in lst :
    # print(i, end=' ') # 1 2 3 4 5
    print(lst[i-1: ]) # 변수[start:stop]
'''
[1, 2, 3, 4, 5]
[2, 3, 4, 5]
[3, 4, 5]
[4, 5]
[5]'''

for i in lst :
    print(lst[ :i]) # 변수[:stop-1]
'''
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]'''

'''
처음/마지막 데이터 추출
'''
x=list(range(1, 101)) # 1~100
print(x)
print(x[:5]) # 앞부분 5개 원소 : [1, 2, 3, 4, 5]
print(x[-5:]) # 마지막 5개 원소 : [96, 97, 98, 99, 100]

'''
index 형식
변수 [start=0 : stop-1: step=1]
'''
print(x[:]) # 전체 1~100
print(x[::2]) # [::step=2] : 홀수 [1, 3, 5, 7, 9, 11, 13, 15,..., 99]
print(x[1::2]) # 짝수 [2, 4, 6, 8, 10, 12, 14, 16, 18,..., 100]

# 2. 중첩 list : [[], []] -> 1차원
a=['a', 'b', 'c']
b=[10, 20, 5, True, "hong"] # ---> 서로 다른 type
print(b) # [10, 20, 5, True, 'hong']

b=[10, 20, 5, a, True, "hong"] # a list 추가
print(b) # [10, 20, 5, ['a', 'b', 'c'], True, 'hong']
print(b[3]) # ['a', 'b', 'c'] ---> b의 index 4번째 내용은 'a list 내용'
print(b[3][2]) # c ---> a list 안에서 세번째 값
print(b[3][1:]) # ['b', 'c']

print(type(a), type(b)) # <class 'list'> <class 'list'>
print(id(a), id(b)) # 1775121288584 1775127336776 ---> a가 b 안에 있는 것처럼 보이지만, 각각 메모리에 따로 저장 되어 있다.

# 3. 값 수정(추가, 삽입, 수정, 삭제) : 메소드 사용(.append, .remove, .insert), 수정은 별도 메소드 없음.
num = ['one', 'two', 'three', 'four']
print(len(num)) # 4

num.append('five') # 원소 추가 : index 맨뒤에 추가
print(num) # ['one', 'two', 'three', 'four', 'five']
num.remove('five') # 원소 삭제
print(num) # ['one', 'two', 'three', 'four']
num.insert(0, 'zero') # 원소 삽입 : insert(self, index, object)
print(num) # ['zero', 'one', 'two', 'three', 'four']
num[0] = 0 # 원소 수정
print(num) # [0, 'one', 'two', 'three', 'four']

# 4. list 연산(+, *)(.extend vs .append)
x = [1, 2, 3, 4]
y = [1.5, 2.5]

# 1) list 결합(+) : list+list = 새로은 list 생성
z = x + y # list 결합 new object
print(z) # [1, 2, 3, 4, 1.5, 2.5]
print(type(z)) # <class 'list'>
print(id(x), id(y), id(z)) # 1775121302088 1775121384328 1775121301768

# 2) list 확장(.extend(list)) --- 단일 list
x.extend(y) # 기존 object
print(x) # [1, 2, 3, 4, 1.5, 2.5]

# 3) list 추가(.append(list)) --- 중첩 list
x.append(y) # 기존 object
print(x) # [1, 2, 3, 4, [1.5, 2.5]]

# 4) list 곱셈(*) : 반복(n배 확장)
lst =[1, 2, 3, 4]
result = lst *2 # 2번 반복
print(result) # [1, 2, 3, 4, 1, 2, 3, 4]

# 5. list 정렬 : .sort(selt, key, reverse)
result.sort() # 오름차순
print(result) # [1, 1, 2, 2, 3, 3, 4, 4]
result.sort(reverse=True) # 내림차순
print(result) # [4, 4, 3, 3, 2, 2, 1, 1]

# 6. scala vs vector
'''
scala 변수 : 한 개의 상수(값)를 갖는 변수(크기)
vector 변수 : 다수의 값을 갖는 변수(크기, 방향)
'''
dataset =[] # 빈 list : vector 변수
size = int(input("vector size : ")) # scala 변수
for i in range(size):
    dataset.append(i+1) # vector 변수
print(dataset) # [1, 2, 3, 4, 5]

# 7. list에서 원소 찾기
'''
if 값 in list : 
    참 실행문
else : 
    거짓 실행문
'''
if 5 in dataset :
    print("5가 있음")
else:
    print("5가 없음")
# 5가 있음