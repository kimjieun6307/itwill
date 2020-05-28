'''
정규 표현식
[함수] -- re모듈
findall, match, sub

[주요 메타문자]
. : 임의의 한 문자
.x : 임의의 한 문자 뒤에 x가 오는 문자열(ex : abc, mbc -> .bc)
^x : x로 시작하는 문자열(접두어 추출)
x$ : x로 끝나는 문자열(접미어 추출)
x. : x 다음에 임의의 한 문자가 오는 문자열(ex : t1, t2, ta -> t.)
x* : x가 0번 이상 반복
x+ : x가 1개 이상 반복
x? : x가 0 또는 1개 존재
x{m, n} : x가 m~n 사이 연속
x{m, } : x가 m 이상 연속
x{,n} : x가 n 이하 연속
[x] : x문자 한 개 일치
'''

st1 = '1234 abc홍길동 ABC_555_6 이사도시'
st2 = 'test1abcABC 123mbc 45test'
st3 = 'test^홍길동 abc 대한*민국 123$tbc'

# 방법1) 정규 표현식 모듈
import re
# 방법 ) from 모듈 import 함수 ---> 주로 많이 씀(사용할 함수만 import하기 때문에 메모리 효율적 사용
from re import findall, match, sub # re 모듈에서 3개 함수만 사용함.
'''
re.findall() # 방법1
findall() # 방법2
'''

'''
1. finadall : 찾기
 - findall(pattern='메타문자 패턴', string='문자열')
 - 숫자 : [0-9] = \\d =  r'd'
 - 문자열 : [가-힣], [a-z], [a-z|A-Z]
'''
# 1) 숫자 찾기 : [0-9] = \\d =  r'd'
print(re.findall('1234', st1)) # ['1234'] ---list 타입으로 반환
print(findall('[0-9]{3}',st1)) # ['123', '555']
print(findall('[0-9]{3,}',st1))  # ['1234', '555']
print(findall('\\d{3,}',st1)) # ['1234', '555'] ---'\\d{3,}' = r'd{3,} = '[0-9]{3,}'

# 2) 문자열 찾기 : [가-힣], [a-z], [a-z|A-Z]
print(findall('[가-힣]{3,}',st1)) # ['홍길동', '이사도시']
print(findall('[a-z]{3,}',st1)) # ['abc']
print(findall('[a-z|A-Z]{3,}',st1)) # ['abc', 'ABC']

#(실습) 이름만 찾아서 names 변수에 list타입으로 저장
st1 = '1234 abc홍길동 ABC_555_6 이사도시'
str_list = st1.split(sep=' ')
print(str_list) # ['1234', 'abc홍길동', 'ABC_555_6', '이사도시']

names = [] # 빈 list
for s in str_list :
    tmp = findall('[가-힣]{3,}', s)
    print(tmp)
''' 결과-->빈 list도 같이 출력됨..
[]
['홍길동']
[]
['이사도시']'''
for s in str_list :
    tmp = findall('[가-힣]{3,}', s)
    if tmp : # []->False, ['값']->Ture
        names.append(tmp[0]) #  names.append(tmp) => [['값']]--중첩 list 됨
print(names) # ['홍길동', '이사도시']

# 3) 접두어(^)/접미어($) 문자열 찾기
st2 = 'test1abcABC 123mbc 45test'
print(findall('^test', st2)) #['test'] ---[ ^x : x로 시작하는 문자열(접두어 추출)]
print(findall('st$',st2)) # ['st'] ---[ x$ : x로 끝나는 문자열(접미어 추출)]

# 종료 문자 찾기
print(findall('.bc', st2)) # ['abc', 'mbc'] ---[ .x : 임의의 한 문자 뒤에 x가 오는 문자열(ex : abc, mbc -> .bc) ]
# 시작 문자 찾기
print(findall('t.', st2)) # ['te', 't1', 'te'] ---[x. : x 다음에 임의의 한 문자가 오는 문자열(ex : t1, t2, ta -> t.)]

# 4. 단어 찾기(\\w) : 한글, 영문자, 숫자
st3 = 'test^홍길동 abc 대한*민국 123$tbc'

word = findall('\\w{3,}', st3)
print(word) # ['test', '홍길동', 'abc', '123', 'tbc']

# 5. 특정 문자열 제외
print(findall('[^t]+', st3)) # ['es', '^홍길동 abc 대한*민국 123$', 'bc'] ---[ x+ : x가 1개 이상 반복]
print(findall('[^t]', st3))#['e', 's', '^', '홍', '길', '동', ' ', 'a', 'b', 'c', ' ', '대', '한', '*', '민', '국', ' ', '1', '2', '3', '$', 'b', 'c']

# 특수문자(^,*,$) 제외
print(findall('[^^*$]+', st3)) # ['test', '홍길동 abc 대한', '민국 123', 'tbc']

'''
2. match
 match(pattern='패턴', string='문자열')
 - 패턴 일치 여부 반환(일치 : object 반환, 불일치 : NULL반환)
 - findall과 반환값에서 차이가 있다.
'''
jumin = "123456-1234567"
result = match('[0-9]{6}-[1-4]\\d{6}', jumin)
print(result) # <re.Match object; span=(0, 14), match='123456-1234567'>
if result :
    print('정상 주민번호')
else:
    print('비정상 주민번호')
# 정상 주민번호

jumin = "123456-5234567"
result = match('[0-9]{6}-[1-4]\\d{6}', jumin)
print(result) # None
if result :
    print('정상 주민번호')
else:
    print('비정상 주민번호')
# 비정상 주민번호

# 3. sub('pattern', 'rep', 'string') : 찾아 바꾸기
st3 = 'test^홍길동 abc 대한*민국 123$tbc'
print(sub('[\^*$]', '', st3)) # test홍길동 abc 대한민국 123tbc
print(sub('[\^*$]', '@', st3)) # test@홍길동 abc 대한@민국 123@tbc

