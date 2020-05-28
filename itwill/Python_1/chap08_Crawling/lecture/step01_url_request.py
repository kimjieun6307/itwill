'''
원격 서버의 웹문서 수집

install beautifulsoup4
'''
from bs4 import BeautifulSoup    # source -> html 파싱
import urllib.request as res     # 별칭 : 원격 서버 파일 요청

url = "http://www.naver.com/index.html"

# 1. 원격서버 url 요청
req = res.urlopen(url)   # 요청 -> 응답
print(req)  # <http.client.HTTPResponse object at 0x000002595575DB88> ---객체정보(object info) 출력
data = req.read() # source
print(data) # b'<!doctype html>.... ---> source
# 원격서버에서 소스(문자열) 가져오는 것 까지 함.

# 2. source(문자열) -> html 형식 : 파싱
src = data.decode('utf-8') # 디코딩 -> 소스
html = BeautifulSoup(src, 'html.parser') # 생성자 : source -> html
print(html)

# 3. Tag 내용 가져오기
link = html.find('a')  # <a href='url'> 내용 </a>
print(link) # 가장 최초로 발견한 앵커태그
#<a href="#news_cast" onclick="document.getElementById('news_cast2').tabIndex = -1;document.getElementById('news_cast2').focus();return false;"><span>연합뉴스 바로가기</span></a>
'''
element : <시작태그 속성명='값'> 내용 </종료태그>
'''
print('a 태그 내용 : ', link.string) # 태그 내용 추출
# a 태그 내용 :  연합뉴스 바로가기


