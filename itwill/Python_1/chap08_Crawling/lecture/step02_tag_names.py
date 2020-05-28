'''
tag명으로 찾기
 형식)
 html.find('tag') : 최초로 발견됨 tag 1개 수집
 html.find_all('tag') : 해당 tab 전체 수집

 tag.string : 태그 내용
'''
from bs4 import BeautifulSoup   # html 파싱

# 1. local file 불러오기
file = open("../data/html01.html", mode='r', encoding='utf-8')
src = file.read()
print(src)
#@@6

# 2. source -> html 파싱
html = BeautifulSoup(src, 'html.parser')
print(html)
#@@7

# 3. tag 찾기 -> 내용 추출
# 1) tag 계층적 구조
h1 = html.html.body.h1
print(h1) # element : <h1> 시멘틱 태그 ?</h1>
print(h1.string) # 내용 :  시멘틱 태그 ?

# 2) find('tag')
h2 = html.find('h2')
print(h2) # <h2> 주요 시멘틱 태그 </h2>
print(h2.string) #  주요 시멘틱 태그

# 3) find_all('tag') # list 타입으로 반환
lis = html.find_all('li')
print(lis) # [<li> header : 문서의 머리말(사이트 소개, 제목, 로그 )</li>, <li> nav : 네이게이션(메뉴) </li>, ...]
print(len(lis)) # 5
for li in lis :
    print(li.string)
'''
 header : 문서의 머리말(사이트 소개, 제목, 로그 )
 nav : 네이게이션(메뉴) 
 section : 웹 문서를 장(chapter)으로 볼 때 절을 구분하는 태그
 aside : 문서의 보조 내용(광고, 즐겨찾기, 링크) 
 footer : 문서의 꼬리말(작성자, 저작권, 개인정보보호) 
'''
li_cont = [li.string for li in lis]
print(li_cont)
# [' header : 문서의 머리말(사이트 소개, 제목, 로그 )', ' nav : 네이게이션(메뉴) ', ...]





