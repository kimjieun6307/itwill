'''
step3 관련 문제

문) word counter
   - 여러줄의 문장을 단어로 분류하고, 단어 수 출력하기
'''

multiline="""안녕하세요. Python 세계로 오신걸
환영합니다.
파이션은 비단뱀 처럼 매력적인 언어입니다."""

sents = multiline.split()
print(sents) # ['안녕하세요.', 'Python', '세계로', '오신걸', '환영합니다.', '파이션은', '비단뱀', '처럼', '매력적인', '언어입니다.']
print('단어 수: ', len(sents)) # 단어 수:  10


# <<출력 결과>> 
'''
안녕하세요.
Python
세계로
오신걸
환영합니다.
파이션은
비단뱀
처럼
매력적인
언어입니다.
단어수 : 10
'''
#(1)
for i in multiline.split():
    print(i)
print('단어수 : ', len(i))  # 단어수 :  6 ---마지막 단어 '언어입니다.' 의 글자수 6
#--------------------------------------
#(2)
sents =[]
for i in multiline.split('\n') :
    sents.append(i)
    for j in i.split():
        print(j)
print('단어수 : ', len(words)) # 단어수 :  10
print(sents) # ['안녕하세요. Python 세계로 오신걸', '환영합니다.', '파이션은 비단뱀 처럼 매력적인 언어입니다.']
#-----------------------------------
#(3)
sents =[]
words=[]
for i in multiline.split('.') :
    sents.append(i)
    for j in i.split():
        words.append(j)
print(words) #['안녕하세요', 'Python', '세계로', '오신걸', '환영합니다', '파이션은', '비단뱀', '처럼', '매력적인', '언어입니다']
print('단어수 : ', len(words)) # 단어수 :  10
print(sents) # ['안녕하세요', ' Python 세계로 오신걸\n환영합니다', '\n파이션은 비단뱀 처럼 매력적인 언어입니다', '']

