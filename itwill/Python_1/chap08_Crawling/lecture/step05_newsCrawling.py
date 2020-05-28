'''
1. news Crawling
 url : http://media.daum.net
2. pickle save
 binary file save -- 객체 그대로 유지해서 저장
'''

import urllib.request as req    # url 요청
from bs4 import BeautifulSoup   # html 파싱

url = 'http://media.daum.net'
#@@8

# 1. url 요청
res = req.urlopen(url) # url 요청
src = res.read()  # source 읽기
print(src)

# 2. html v파싱
src = src.decode('utf-8')
html = BeautifulSoup(src, 'html.parser')
print(html)
#@@10
# 3. tab[속성 = '값'] -> a[class="link_txt"]
#@@11
links = html.select('a[class="link_txt"]')
print(len(links)) # 62
print(links) #@@12

crawling_data = [] # 빈 list
for link in links :
    link_string = str(link.string) # 내용추출
    crawling_data.append(link_string.strip()) # 문장 끝 불용어 처리(\n, 공백 등)

print(crawling_data)
#['김용태 "윤석열 거취 거론은 오만방자" vs 우희종 "개인 의견까지 검열하나"', '우희종 "윤석열 거취 언급, 개인 의견 말한 게 오만한 것이냐"',..]
print(len(crawling_data)) # 62

# 4. pickle file save
# -- pickle 타입으로 저장하는 이유는 다음에 다시 파일을 불렀을때 list 타입으로 불러올수 있어서
import pickle

# save
file = open('../data/new_crawling.pickle', mode='wb')
pickle.dump(crawling_data, file)
print('pickle file saved') #@@13






