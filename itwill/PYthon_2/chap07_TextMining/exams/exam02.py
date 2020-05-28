# -*- coding: utf-8 -*-
'''
# 문) 2019년11월 ~ 2020년2월 까지(4개월) daum 뉴스기사를 다음과 같이 크롤링하고, 
단어구름으로 시각화 하시오.
# <조건1> 날짜별 5개 페이지 크롤링
# <조건2> 불용어 전처리 
# <조건3> 단어빈도수 분석 후 top 20 단어 단어구름 시각화 
'''
import urllib.request as req  # url 가져오기 
from bs4 import BeautifulSoup # html 파싱
import pandas as pd # 시계열 date

from konlpy.tag import Kkma
from wordcloud import WordCloud 

kkma = Kkma()


# 1. 수집 년도 생성 : 시계열 date 이용
date = pd.date_range("2019-11-01", "2020-02-01") # 시작일, 마감일
len(date) #93

date[0] # Timestamp('2019-11-01 00:00:00', freq='D')
date[-1] # Timestamp('2020-02-01 00:00:00', freq='D')


import re # sub('pattern', '교체할 문자', string)

# 문자 변환/제거 ['2015-01-01 00:00:00', freq='D'] -> [20150101]
sdate = [re.sub('-', '', str(i))[:8] for i in date]
sdate[:10]
sdate[-10:]


# 2. Crawler 함수 생성
def Crawler (date, pagse=5) : 
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
    
Crawler(20200101)

# 3. Crawler 함수 호출
year5_news_date = [Crawler(date)[0] for date in sdate]
year5_news_date[0]  #'트럼프 "\'우크라녹취록 낭독\' 노변정담"..민주 공개청문회 맞불?'


nouns_word=[]
for sent in year5_news_date :  
    for noun in kkma.nouns(sent) : 
        nouns_word.append(noun)


nouns_word[0]  #  '트럼프'

len(nouns_word)  # 1052


# 4. 전처리 : 단어 길이 제한(2음절 이상), 숫자 제외(정규표현식 사용)
from re import match

nouns_count ={} # 단어 카운트

for noun in nouns_word:
    if len(noun) > 1 and not(match('^[0-9]', noun)) :
        nouns_count[noun] = nouns_count.get(noun, 0)+1


len(nouns_count)  # 623


# 5. WordCloud

# 1) top20 word
from collections import Counter # class

word_cnt = Counter(nouns_count)
top20_word = word_cnt.most_common(20)
top20_word

# 2) 시각화 word cloud
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=600,
          max_words = 100, max_font_size= 200, background_color='white')
# 다른건 다 생략해도 "한글"은 반드시 font_path='C:/Windows/Fonts/malgun.ttf' 해야함.

wc_result = wc.generate_from_frequencies(dict(top20_word)) #dict

import matplotlib.pyplot as plt

plt.imshow(wc_result)
plt.axis('off') # 축의 눈금 감추기
plt.show()
#@@1