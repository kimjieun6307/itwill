'''
문자열 처리
- 문자열(string) : 문자들의 순서(index) 집함
- indexing/slicing 가능
- 문자열 = 상수 : 수정불가
'''

# 1. 문자열 처리
# 1) 문자열 유형
lineStr = "this is one ling string" # 한 줄 문자열
print(lineStr)

# 여러줄 문자열
multiStr = '''this
is multi line
string'''
print(multiStr)

multiStr2 = 'this \nis multi line\n string' # \n : 줄바꿈
print(multiStr2)

# sql문 : 부서번호
deptno = int(input('부서번호 입력 : '))
query = f"""select * from emp
where deptno = {deptno}
order by sel desc"""
print(query)
#@@8

# 2) 문자열 연산(+, *) : + 결합, * 반복
print("python" + ' program') # 결합연산자 : python program
# print('python' + 37) # TypeError: can only concatenate str (not "int") to str
print('python' + str(37)) # python37
print('-'*30) #30번 반복 : ------------------------------

'''
<object.member> or <object.member()>
int.member 
str.member
'''
#@@9 #@@10 #@@11

# 3) 문자열 처리 함수
lineStr = "this is one ling string"
print(lineStr, type(lineStr)) # 내용, 자료형 출력
# this is one ling string <class 'str'>
print('문자열 길이 : ', len(lineStr)) # 문자열 길이 :  23
print('t의 글자수 : ', lineStr.count('t')) # t의 글자수 :  2

# 접두어 : 시작문자열
print(lineStr.startswith('this')) # True
print(lineStr.startswith('that')) # False

# split(분리) : 토큰 생성
# 1) 문장 -> 단어
words = lineStr.split(sep=' ') #split 기본값 ' '
print(words) # ['this', 'is', 'one', 'ling', 'string']
print('단어 길이 : ', len(words)) #단어 길이 :  5

# join(결합) : '구분자'.join(str)
sentence = ' '.join(words) # 1) 단어 -> 문장
print(sentence) # this is one ling string

# 2)문단 -> 문장
multiStr = '''this
is multi line
string'''

sentence = multiStr.split(sep='\n')
print(sentence) # ['this', 'is multi line', 'string']
print('문장 길이 : ', len(sentence)) # 문장 길이 :  3

para = ','.join(sentence) # 2) 문장 -> 문단
print(para) # this,is multi line,string


print(multiStr. upper()) # 소문자 -> 대문자

# 4) indexing / slcing
lineStr = "this is one ling string"
print(lineStr[0]) # 첫번째 문자 : t
print(lineStr[-1]) # 마지막 문자 : g
print(lineStr[:4]) # [start : end-1] : this
print(lineStr[-6:]) # 오른쪽 끝 6개 문자열 : string
print(lineStr[-1:-6]) # 값 없음
print(lineStr[-6:-1]) # strin
print(lineStr[-11:-7]) # ling

# 2. escape 문자 처리
'''
escape 문자 : 명령어 이외 특수문자(', ", \n, \t, \b)
'''
print("\nescape 문자") # escape 문자
print("\\nescape 문자") # \nescape 문자 --- '\'더붙이거나
print(r"\nescape 문자") # \nescape 문자 --- 앞에 'r'붙이거나

# (예) c:\python\work\test
print('c:\python\work\test') # c:\python\work	est --- '\t' escape 문자로 인식됨
print('c:\\python\\work\\test') # c:\python\work\test
print(r'c:\python\work\test') # c:\python\work\test

