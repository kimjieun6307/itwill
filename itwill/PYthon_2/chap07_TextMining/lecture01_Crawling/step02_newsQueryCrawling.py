# -*- coding: utf-8 -*-
"""
news Crawling : url query 이용
    url : http://media.daum.net -> [배열이력] 클릭
    url : https://news.daum.net/newsbox -> base url -> [특정 날짜] 클릭
    url : https://news.daum.net/newsbox?regDate=20200505 -> [특정 페이지]
    url : https://news.daum.net/newsbox?regDate=20200505&page=2
#@@3~5
"""

import urllib.request as req    # url 요청
from bs4 import BeautifulSoup   # html 파싱

# 1. url query 만들기
'''
date : 2020.02.01 ~ 2020.02.29
page : 1 ~ 10
각 날짜 별로 10page까지 crawling
'''

# base_url + date 
base_url = "https://news.daum.net/newsbox?regDate="
date = list(range(20200201, 20200230)) # 20200229+1 = 20200230
date
#@@6
len(date) # 29

# 문자열 이용 결합 연산자 : base_url+str(i)
url_list = [base_url+str(i) for i in date]
url_list
# ['https://news.daum.net/newsbox?regDate=20200201', ~~ ]
 

# base_url + date + page 
page = list(range(1, 11)) # 1~10
page # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pages = ['&page='+str(i) for i in page]
pages
'''
['&page=1',
 '&page=2',
 '&page=3',
 '&page=4',
 '&page=5',
 '&page=6',
 '&page=7',
 '&page=8',
 '&page=9',
 '&page=10']
'''

final_url = []
for url in url_list : # base_url + date
    for page in pages :  # page 1 ~ page 10
        final_url.append(url+page)

len(final_url) # 290
final_url[0] # 'https://news.daum.net/newsbox?regDate=20200201&page=1'
final_url[-1] # 'https://news.daum.net/newsbox?regDate=20200229&page=10'


# Crawlier 함수 정의
def Crawlier(url) : # 1page news
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
        #print('cnt : ', cnt)
        #print('news : ', link_str)
        open_page_data.append(link_str.strip()) # 문장 끝 불용어 처리(\n, 공백 등)
        
    return open_page_data[:40] # 유효한 주소만 반환(40번째 까지)



one_page_data = Crawlier(final_url[0]) # 20200201 -> page 1
#@@7

len(one_page_data) # 134
type(one_page_data) # list

one_page_data[0] # '의협 "감염병 위기경보 상향 제안..환자 혐오 멈춰야"'
one_page_data[-1] # "'공인구 합격이라는데' 왜 홈런은 펑펑 터질까"
one_page_data[:5]
'''
['의협 "감염병 위기경보 상향 제안..환자 혐오 멈춰야"',
 "'신종코로나 진원' 중국 후베이성 춘제연휴 13일까지 재연장",
 '높아진 국가청렴도..제도개혁이 관건',
 '"독일 공군기, 중국 우한서 100여명 태우고 본국으로"',
 '이견 여전한 방위비 협상..이달 타결될까']
'''

# 해당 기사 추출 : 40번까지가 해당 날짜 기사(나머지는 실시간 뉴스로 추정됨)
one_page_data[:40]


# 2월(1개원) 전체 news 수집
month_news = []
page_cnt = 0

# 3. Crawlier 함수 호출
for url in final_url :
    page_cnt += 1
    print('page : ', page_cnt)
    one_page_news = Crawlier(url) # 1page news
    print('one page news')
    print(one_page_news)
    
    # 단일 리스트 vs 중첩 리스트 => 사용자가 선택
    #month_news.append(one_page_news)  # [[1page], [2page]] : 중첩리스트
    month_news.extend(one_page_news)  # [ 1page ~ 290page ] : 단일리스트
#@@8

len(final_url) # 290
len(month_news) #  11600
29*10*40 # 11600
# >> 2월(1개월)동안 뉴스 10페이지 crawling 결과 : 총11,600문장


# 4. binary file save
import pickle # list -> file save -> load(list)

# file save
# 현재 위치 C:\ITWILL\4_Python-II\workspace\chap07_TextMining\lecture01_Crawling
file = open('../data/new_data.pck', mode='wb', ) # wb=write binary
pickle.dump(month_news, file)
#@@9

# file load
file = open('../data/new_data.pck', mode='rb')
moth_news2 = pickle.load(file)

moth_news2
file.close()


# Crawlier 함수 호출에서 예외 처리 (try ~ except문)
for url in final_url :
    page_cnt += 1
    print('page : ', page_cnt)
    try : # 에외처리 - url 없는 경우
        one_page_news = Crawlier(url) # 1page news
        print('one page news')
        print(one_page_news)
        
        #month_news.append(one_page_news)  # [[1page], [2page]] : 중첩리스트
        month_news.extend(one_page_news)  # [ 1page ~ 290page ] : 단일리스트
    except :
        print('해당 url 없음 : ', url)

























