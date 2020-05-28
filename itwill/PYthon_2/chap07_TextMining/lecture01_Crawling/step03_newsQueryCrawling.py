# -*- coding: utf-8 -*-
"""
방법2) url query  이용 : 년도별 뉴스 자료 수집
    예) 2015.01.01 ~ 2020.01.01
        page : 1~5
"""

import urllib.request as req  # url 가져오기 
from bs4 import BeautifulSoup # html 파싱
import pandas as pd # 시계열 date

# 1. 수집 년도 생성 : 시계열 date 이용
date = pd.date_range("2015-01-01", "2020-01-01") # 시작일, 마감일
len(date) # 1827

date[0] # Timestamp('2015-01-01 00:00:00', freq='D')
date[-1] #  Timestamp('2020-01-01 00:00:00', freq='D')
type(date) # pandas.core.indexes.datetimes.DatetimeIndex


import re # sub('pattern', '교체할 문자', string)

# 문자 변환/제거 ['2015-01-01 00:00:00', freq='D'] -> [20150101]
sdate = [re.sub('-', '', str(i))[:8] for i in date]
sdate[:10]
'''
['20150101',
 '20150102',
 '20150103',
 '20150104',
 '20150105',
 '20150106',
 '20150107',
 '20150108',
 '20150109',
 '20150110']
'''
sdate[-10:]
'''
['20191223',
 '20191224',
 '20191225',
 '20191226',
 '20191227',
 '20191228',
 '20191229',
 '20191230',
 '20191231',
 '20200101']
'''


# 2. Crawler 함수 
def newDrawler (date, pagse=5) : 
    one_day_data =[]
    for page in range(1, pagse+1) : 
        url = f"https://news.daum.net/newsbox?regDate={date}&page={page}"
        
        try : 
            # 1. url 요청
            res = req.urlopen(url) # url 요청
            src = res.read()  # source 읽기
                
            # 2. html 파싱(decode)
            src = src.decode('utf-8')
            html = BeautifulSoup(src, 'html.parser')
            
            # 3. tab[속성 = '값'] -> a[class="link_txt"]
            links = html.select('a[class="link_txt"]')
            
            one_page_data = [] # 빈 list
            
            for link in links :
                link_str = str(link.string) # 내용추출
                print('news : ', link_str)
                one_page_data.append(link_str.strip()) # 문장 끝 불용어 처리
            # 1day news
            one_day_data.extend(one_page_data[:40])
        except Exception as e:
            print('오류발생 : ', e)
    return one_day_data
    
newDrawler(20200101)

# 3. Crawler 함수 호출
year5_news_date = [newDrawler(date)[0] for date in sdate]
# [1day(1~5page), 2day(1~5page), ....]
# HTTPError: 500 -> try ~ except 구문 사용

















