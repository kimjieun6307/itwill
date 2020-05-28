# -*- coding: utf-8 -*-
"""
 오전 수업때 만든 'new_data.pck' word cloud
 
1. pickle file 읽기
2. 명사 추출 : kkma.nouns()
3. 전처리 : 단어길이 제한, 숫자 제외 
4. WordCloud
"""
import konlpy
from konlpy.tag import Kkma
from wordcloud import WordCloud # class


# object 생성
kkma=Kkma()

# 1. pickle file 읽기 : news_data.pck
file = open('../data/new_data.pck', mode='rb')
news_data = pickle.load(file)
news_data

file.close()

len(news_data) # 11600
type(news_data) # list


# docs -> sentence
# <error> news_sent = kkma.sentences(news_data)
news_sent = [kkma.sentences(sent)[0]  for sent in news_data]
news_sent

len(news_sent) # 11600



# 2. 명사 추출 : Kkma
nouns_word = []   # 명사저장

for sent in news_sent :   # '형태소 분석을 시작합니다.'
    for noun in kkma.nouns(sent) :  # 문장 -> 명사
        nouns_word.append(noun)


nouns_word

len(nouns_word)  # 120939


# 3. 전처리 : 단어 길이 제한(2음절 이상), 숫자 제외(정규표현식 사용)
from re import match

nouns_count ={} # 단어 카운트

for noun in nouns_word:
    if len(noun) > 1 and not(match('^[0-9]', noun)) :
        # key 지정[noun] = value[출현빈도수]
        nouns_count[noun] = nouns_count.get(noun, 0)+1


len(nouns_count)  # 12194


# 4. WordCloud

# 1) top5 word
from collections import Counter # class

word_cnt = Counter(nouns_count)
top50_word = word_cnt.most_common(50)
top50_word
'''
[('코로나', 2539),
 ('종합', 2008),
 ('신종', 659),
 ('진자', 626),
 ('중국', 554),
 ('환자', 536),
 ('정부', 402),
 ('한국', 383),
 '''
 

# 2) 시각화 word cloud
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=600,
          max_words = 100, max_font_size= 200, background_color='white')
# 다른건 다 생략해도 "한글"은 반드시 font_path='C:/Windows/Fonts/malgun.ttf' 해야함.

wc_result = wc.generate_from_frequencies(dict(top50_word)) #dict

import matplotlib.pyplot as plt

plt.imshow(wc_result)
plt.axis('off') # 축의 눈금 감추기
plt.show()
#@@17

# word cloud 결과 확인후 수정 사항 : 진자 -> 확진자 
nouns_count['확진자'] = nouns_count['진자']
del nouns_count['진자']
# 다시 반복~





























