''''''
'''
step02 문제

문1) message에서 'spam' 원소는 1 'ham' 원소는 0으로 dummy 변수를 생성하시오.
      <조건> list + for 형식1) 적용   
      
  <출력결과>      
[1, 0, 1, 0, 1]   
'''

message = ['spam', 'ham', 'spam', 'ham', 'spam']
dummy = [int(i=='spam') for i in message]
print(dummy) # [1, 0, 1, 0, 1]

'''
line if 문
변수 = 참 if 조건문 else 거짓
dummy = [ 1 if m=='spam' else 0 for m in message]
'''


'''
문2) message에서 'spam' 원소만 추출하여 spam_list에 추가하시오.
      <조건> list + for + if 형식2) 적용   
      
  <출력결과>      
['spam', 'spam', 'spam']   

'''
message = ['spam', 'ham', 'spam', 'ham', 'spam']
spam_list=[i for i in message if i=='spam']
print(spam_list) # ['spam', 'spam', 'spam']