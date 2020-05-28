'''
 문) login.html 웹 문서를 대상으로 다음 조건에 맞게 내용을 추출하시오. 
    조건1> id="login_wrap" 선택자의  하위 태그  전체 출력 
    조건2> id="login_warp" 선택자  > form > table 태그 내용 출력 
    조건3> find_all('tr') 함수 이용  th 태그 내용 출력  
'''
#@@5, 6
from bs4 import BeautifulSoup

# 1. html source 가져오기 
file = open('../data/login.html', encoding='utf-8')
src = file.read()

# 2. html 파싱
html = BeautifulSoup(src, 'html.parser')
#print(html)

# 3. 선택자 이용 태그 내용 가져오기
divs = html.select('#login_wrap')
#print(divs)
'''
[<div id="login_wrap">
<h2 class="login_title"> 회원 로그인 </h2>
<form action="http://www.naver.com" method="post" name="frm" onsubmit="return login_check()">
<table id="login_t">
<tr> <!-- 1행 -->
<th> 아이디 </th>
<td> <input class="input_box" id="id" name="id" size="14" type="text"/>
</td>
</tr>
<tr> <!-- 2행 -->
<th> 비밀번호 </th>
<td> <input class="input_box" id="pwd" name="pwd" size="14" type="password"/>
</td>
</tr>
</table>
<div id="login_btn">
<input class="login_b" type="submit" value="로그인"/>
<input class="login_b" onclick="$('#id').focus()" type="reset" value="취소"/>
</div>
</form>
</div>]
'''

table = html.select('#login_wrap > form > table')
print(table)
#@@7
'''
[<table id="login_t">
<tr> <!-- 1행 -->
<th> 아이디 </th>
<td> <input class="input_box" id="id" name="id" size="14" type="text"/>
</td>
</tr>
<tr> <!-- 2행 -->
<th> 비밀번호 </th>
<td> <input class="input_box" id="pwd" name="pwd" size="14" type="password"/>
</td>
</tr>
</table>]
'''

trs = html.find_all('tr')
#print(trs)
for tr in trs :
    tds = tr.find_all('td')
    for td in tds:
        print(td)
'''
<td> <input class="input_box" id="id" name="id" size="14" type="text"/>
</td>
<td> <input class="input_box" id="pwd" name="pwd" size="14" type="password"/>
</td>
'''











