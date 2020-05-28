'''
선택자(selector)
 - 웹 문서 디자인(css)에서 사용
 - 선택자 : id(#)--중복 불가, class(.)--중복 가능
 - html.select('선택자') : 여러개의 element 수집       cf) find('태그')
 - html.select_one('선택자') : 한 개 element 수집      cf) find_all('태그')
'''

from bs4 import BeautifulSoup

file = open('../data/html03.html', encoding='utf-8')
#@@2 #@@1
src = file.read()
print(src)

html = BeautifulSoup(src, 'html.parser')

# 태그 & 선택자 -> element 수집

# 1) id 선택자(#)
table = html.select_one('#tab') # id = "tab"
#@@3
print(table) # <table> ~ </table>
'''
<table border="1" id="tab">
<tr> <!-- 1행 -->
<!-- 제목 열 : th -->
<th id="id"> 학번 </th>
<th id="name"> 이름 </th>
<th id="major"> 학과 </th>
<th id="email"> 이메일 </th>
</tr>
<tr> <!-- 2행 -->
<td> 201601 </td>
<td> 홍길동 </td>
<td> 체육학과 </td>
<td> hong@naver.com </td>
</tr>
<tr class="odd"> <!-- 3행(홀수) -->
<td> 201602 </td>
<td> 이순신 </td>
<td> 해양학과 </td>
<td> lee@naver.com </td>
</tr>
<tr> <!-- 4행 -->
<td> 201603 </td>
<td> 강감찬 </td>
<td> 정치외교 </td>
<td> kang@naver.com </td>
</tr>
<tr class="odd"> <!-- 5행 -->
<td> 201604 </td>
<td> 유관순 </td>
<td> 유아교육 </td>
<td> you@naver.com </td>
</tr>
</table>

Process finished with exit code 0
'''

# <table> <tr> <th> or <tb>
# table : 테이블, tr : 행, th : 제목 열, tb : 열

ths = html.select('#tab>tr>th') # list타입으로 반환됨. '>' 기호를 통해 계층적으로 접근해서 high element 추출
print(ths)
# [<th id="id"> 학번 </th>, <th id="name"> 이름 </th>, <th id="major"> 학과 </th>, <th id="email"> 이메일 </th>]
print(len(ths)) # 4

for th in ths:
    print(th.string) # tag 내용
'''
 학번 
 이름 
 학과 
 이메일 
'''

# 2) class 선택자 (.)
trs = html.select('#tab > .odd') # class="odd" # <tr> 5개 -> <tr> 2개
print(trs)
'''
[<tr class="odd"> <!-- 3행(홀수) -->
<td> 201602 </td>
<td> 이순신 </td>
<td> 해양학과 </td>
<td> lee@naver.com </td>
</tr>, <tr class="odd"> <!-- 5행 -->
<td> 201604 </td>
<td> 유관순 </td>
<td> 유아교육 </td>
<td> you@naver.com </td>
</tr>]
'''
for tr in trs : # 상위 element
    # print(tr)
    tds = tr.find_all('td')
    for td in tds : # 하위 element
        print(td.string)
'''
 201602 
 이순신 
 해양학과 
 lee@naver.com 
 201604 
 유관순 
 유아교육 
 you@naver.com 
'''
# 3) tag[속성='값'] 찾기
trs = html.select("tr[class='odd']") # <tr class="odd"> 계층적으로 접근하지 않고 다이렉트로 접근
print(trs)
#@@4 -error
'''
[<tr class="odd"> <!-- 3행(홀수) -->
<td> 201602 </td>
<td> 이순신 </td>
<td> 해양학과 </td>
<td> lee@naver.com </td>
</tr>, <tr class="odd"> <!-- 5행 -->
<td> 201604 </td>
<td> 유관순 </td>
<td> 유아교육 </td>
<td> you@naver.com </td>
</tr>]
'''

for tr in trs :
    tds = tr.find_all('td')
    for td in tds :
        print(td.string)
'''
 201602 
 이순신 
 해양학과 
 lee@naver.com 
 201604 
 유관순 
 유아교육 
 you@naver.com 
'''

#(정리) 세가지 유형으로 elemet 수집하는 방법 다룸.
# 태그로 수집할 것이냐, 선택자로 수집할 것이냐는 그때그때 html 소스에 맞게 선택하면 됨.


