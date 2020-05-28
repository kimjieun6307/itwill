'''
 문) login.html 웹 문서를 대상으로 다음 조건에 맞게 내용을 추출하시오. 
    조건> <tr> 태그 하위 태그인 <th> 태그의 모든 내용 출력
    
   <출력 결과>
   th 태그 내용 
    아이디 
    비밀번호 
'''

from bs4 import BeautifulSoup

# 1. 파일 읽기 
file = open("../data/login.html", mode='r', encoding='utf-8')
source = file.read()
print(source)

# 2. html 파싱
html = BeautifulSoup(source, 'html.parser')
print('html 출력 : ', html)

# 3. 태그 찾기 
ths = html.find_all('th')
print('ths 출력 : ', ths)

# 4. 태그 내용 출력
print('th 태그 내용')
for th in ths :
    print(th.string)


''' 출력 결과 1 ~ 4
1. print(source)
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>회원 로그인</title>
  <!-- 외부 스타일 시트 파일 링크 -->
  <link rel="stylesheet" href="../css/login.css">
  
  <!-- jQuery 라이브러리 링크 -->
  <script src="../js/jquery.js"></script>
  <!-- javascript 외부 파일 링크 -->
  <script src="../js/login.js"></script>
  
</head>
<body>
   <div id="login_wrap">
     <h2 class="login_title"> 회원 로그인 </h2>
     <form name="frm"  method="post" 
           action="http://www.naver.com"
           onsubmit="return login_check()">
      <table id="login_t">
         <tr> <!-- 1행 -->
            <th> 아이디 </th>
            <td> <input type="text" name ="id" id="id"
                        size="14" class="input_box"/>
            </td>                     
         </tr>
         <tr> <!-- 2행 -->
            <th> 비밀번호 </th>
            <td> <input type="password" name ="pwd" id="pwd"
                        size="14" class="input_box"/>
            </td>                     
         </tr>
      </table>
      <div id="login_btn">
        <input type="submit" value="로그인" class="login_b"/>
     	<input type="reset" value="취소" class="login_b"
                onclick="$('#id').focus()"/>
      </div>
     </form>
   </div>
</body>
</html>


2. html 출력 :  
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<title>회원 로그인</title>
<!-- 외부 스타일 시트 파일 링크 -->
<link href="../css/login.css" rel="stylesheet"/>
<!-- jQuery 라이브러리 링크 -->
<script src="../js/jquery.js"></script>
<!-- javascript 외부 파일 링크 -->
<script src="../js/login.js"></script>
</head>
<body>
<div id="login_wrap">
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
</div>
</body>
</html>

3. ths 출력 :  
[<th> 아이디 </th>, <th> 비밀번호 </th>]

4. 
th 태그 내용
 아이디 
 비밀번호 
'''

# (참고용) 다른 방법
trs = html.find_all('tr')
for tr in trs :
    th = tr.find('th')
    print(th.string)

