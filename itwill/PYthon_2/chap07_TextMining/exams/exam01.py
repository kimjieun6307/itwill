'''
 문) 아래 url을 이용하여 어린이날(20200505)에 제공된 뉴스 기사를 
   1~5페이지 크롤링하는 크롤러 함수를 정의하고 크롤링 결과를 확인하시오.
   
   base_url = "https://news.daum.net/newsbox?regDate="   
   
   <조건1> 크롤러 함수의 파라미터(page번호, 날짜)
   <조건2> 크롤링 대상  : <a> 태그의 'class=link_txt' 속성을 갖는 내용 
   <조건3> 크롤링 결과 확인  : news 갯수와  문장 출력(한글 깨짐 확인)  
'''

import urllib.request as req  # url 가져오기 
from bs4 import BeautifulSoup

base_url = "https://news.daum.net/newsbox?regDate="

# 클로러 함수(페이지, 검색날자) 
def crawler_func(pages, date):
    crawling_news = [] # news 저장 
    
    date_url = base_url + str(date)
    final_url = [date_url + '&page='+str(i) for i in list(range(1, pages+1))]
    
    for url in final_url:
        # 1. url 요청
        res = req.urlopen(url) # url 요청
        src = res.read()  # source 읽기
            
        # 2. html 파싱(decode)
        src = src.decode('utf-8')
        html = BeautifulSoup(src, 'html.parser')
        
        # 3. tab[속성 = '값'] -> a[class="link_txt"]
        links = html.select('a[class="link_txt"]')
        
        open_page_data = [] # 빈 list
        cnt=0
        for link in links :
            link_str = str(link.string) # 내용추출
            cnt += 1
            print('cnt : ', cnt)
            print('news : ', link_str)
            open_page_data.append(link_str.strip()) # 문장 끝 불용어 처리(\n, 공백 등)
        
    crawling_news.extend(open_page_data[:40]) # 유효한 주소만 반환(40번째 까지)
    
    return crawling_news 


# 클로러 함수 호출 
crawling_news = crawler_func(5, 20200505)


# 크롤링 결과 확인
print('크롤링 news 수 =', len(crawling_news)) 
print(crawling_news)
    