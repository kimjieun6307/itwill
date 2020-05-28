'''
문3) 정규표현식을 적용하여 person을 대상으로 주민번호 양식이 올바른 
     사람을 대상으로 다음과 같은 출력 예시와 같이 주민등록번호를 출력하시오.
    
   <출력 예시> 
유관순 750905-******* 
홍길동 850905-******* 
강감찬 770210-*******  
'''

import re # 정규표현식 패키지 임포트
from re import sub

person = """유관순 750905-2049118
홍길동 850905-1059119
강호동 790101-5142142
강감찬 770210-1542001"""

x = [sub(r'-[1-4]\d{6}', '-*******', i) for i in person.split('\n')]
print(x)

'''
<실패...ㅠㅠ>
for i in person.split('\n'):
    tmp =re.findall(r'^\w{3,} [0-9]{6}-[1-4]\d{6}', i)
    if tmp :
       jum = list(re.sub(r'-[0-9]{7}', '-*******', tmp[0]))
       print(jum)
       jumin=jum.extend(jum)
       print(jumin)
'''

for p in person.split(sep='\n'):
    tmp=re.findall("[가-힣]{3} [0-9]{6}-[1-4]\\d{6}",p)
    if tmp:
        result=tmp[0]
        jumin = result[:10]+'-*******'
        print(jumin)


for p in person.split(sep='\n'):
    tmp=re.findall("[가-힣]{3} [0-9]{6}-[1-4]\\d{6}",p)
    if tmp:
       print(tmp[0][:11]+'*******')



'''error
for p in person.split(sep='\n'):
...     tmp=re.findall("[가-힣]{3}[0-9]{6}-[1-4]\\d{6}",p) ---> 띄어 쓰기
...     print(tmp) 

for p in person.split(sep='\n'):
...     tmp=re.findall("[가-힣]{3} [0-9]{6}-[1-4]\\d{6}",p)
...     print(tmp)
...     if tmp:
...         tmp[0][-7:]='*******'
...         print(tmp[0])

'''
