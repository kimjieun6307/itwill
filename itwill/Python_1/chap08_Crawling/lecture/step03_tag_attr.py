'''
tag 속성과 내용 가져오기
- element : tag + 속성 + 내용
- element : <시작태그 속성명='값'> 내용 </종료태그>
ex) <a href="www.naver.com">네이버</a>
a : tag
href : 속성(attribute)
네이버 : 내용(content)
'''

from bs4 import BeautifulSoup

# 1. local file 가져오기
file = open("../data/html02.html", encoding='utf-8')
src = file.read()

# 2. html 파싱
html = BeautifulSoup(src, 'html.parser')
print(html)
#@@9

# 3. a 태그 엘리먼트 가져오기
links = html.find_all('a')
print(links) # [<a href="www.naver.com">네이버</a>, <a href="http://www.naver.com">네이버</a>, ...]
print(len(links)) # 5

# 4. a 태그 -> 속성(href(5), target(1))
urls=[]
for link in links :
    print(link.string)  # 태그 내용(string) : 네이버
    attr=link.attrs
    print(attr)   # 태그 속성(attrs) : {'href': 'www.naver.com'} ---> dict 타입
    # {'href': 'http://www.naver.com', 'target': '_blank'} ---> 속성이 1개 이상인 경우
    # print(attr['href']) # value : www.naver.com
    urls.append(attr['href'])
    try:
        print(attr['target']) # _blank
        # target 라는 속성이 a 태그 총 5건 중에 1건 있어서 에러 발생(href 속성은 5건 모두 있어서 에러 없었음.)
    except Exception as e :
        print('예외 발생 : ', e)

print(urls)
# ['www.naver.com', 'http://www.naver.com', 'http://www.naver.com', 'www.duam.net', 'http://www.duam.net']
print(len(urls)) # 5
'''
첫번째 url 들어가서 정보 수집하고, 두번째 url 들어가서 정보 수집하고...

url = "http://www.naver.com/index.html"
# 1. 원격서버 url 요청
req = res.urlopen(url)   # 요청 -> 응답
print(req)  # <http.client.HTTPResponse object at 0x000002595575DB88> ---객체정보(object info) 출력
data = req.read() # source
print(data) # b'<!doctype html>.... ---> source

# 2. source(문자열) -> html 형식 : 파싱
src = data.decode('utf-8') # 디코딩 -> 소스
html = BeautifulSoup(src, 'html.parser') # 생성자 : source -> html
'''

# urls -> 정상 url -> new_urls
from re import findall, match, sub

new_url =[]

for url in urls :
    url= findall('^[a-z]{4}://[w]{3}.\w{1,}.\w{1,}', url)  
    if url :
        new_url.append(url[0])

'''
for url in urls :
    tmp = findall('^http://', url)  
    if tmp :
        new_url.append(url)

# match 사용
for url in urls :
    tmp = match('^http://', url)
    if tmp :
        new_url.append(url)
'''
print(new_url) # ['http://www.naver.com', 'http://www.naver.com', 'http://www.duam.net']




