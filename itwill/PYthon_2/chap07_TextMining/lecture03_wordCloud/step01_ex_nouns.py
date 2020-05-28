# -*- coding: utf-8 -*-
"""
1. text file 읽기
2. 명사 추출 : kkma.nouns()
3. 전처리 : 단어길이 제한, 숫자 제외 
4. WordCloud
"""
# <error>from konlpy import Kkma # 형태분석
import konlpy
from konlpy.tag import Kkma
from wordcloud import WordCloud # class
help(WordCloud)
#@@14
'''
★ 한글은 반드시 폰트 path 해야 함. 
font_path='C:/Windows/Fonts/malgun.ttf'
'''


# object 생성
kkma=Kkma()

# 1. text file 읽기 : text_data.txt
file = open('../data/text_data.txt', mode='r', encoding='utf-8') 
docs = file.read()
docs
# '형태소 분석을 시작합니다. 나는 데이터 분석을 좋아합니다. \n직업은 데이터 분석 전문가 입니다. Text mining 기법은 2000대 초반에 개발된 기술이다.'

file.close()


# docs -> sentence
ex_sent = kkma.sentences(docs)
ex_sent
'''
['형태소 분석을 시작합니다.',
 '나는 데이터 분석을 좋아합니다.',
 '직업은 데이터 분석 전문가 입니다.',
 'Text mining 기법은 2000대 초반에 개발된 기술이다.']
'''
len(ex_sent)  # 4


# docs -> nouns
ex_nouns = kkma.nouns(docs) # 유일한 명사 추출
ex_nouns
'''
['형태소',
 '분석',
 '나',
 '데이터',
 '직업',
 '전문가',
 '기법',
 '2000',
 '2000대',
 '대',
 '초반',
 '개발',
 '기술']
'''
len(ex_nouns) # 13 
# [kkma.nouns()는 유일한 명사만 추출되서 명사 빈도수 구할수 없음.]


# 2. 명사 추출 : Kkma
nouns_word = []   # 명사저장

for sent in ex_sent :   # '형태소 분석을 시작합니다.'
    for noun in kkma.nouns(sent) :  # 문장 -> 명사
        nouns_word.append(noun)


nouns_word
'''
['형태소',
 '분석',   <--★
 '데이터',
 '분석',   <--★
 '직업',
 '데이터',
 '분석',   <--★
 '전문가',
 '기법',
 '2000',
 '2000대',
 '대',
 '초반',
 '개발',
 '기술']
'''
len(nouns_word) # 15


# 3. 전처리 : 단어 길이 제한(2음절 이상), 숫자 제외(정규표현식 사용)
from re import match

nouns_count ={} # 단어 카운트

for noun in nouns_word:
    if len(noun) > 1 and not(match('^[0-9]', noun)) :
        # key 지정[noun] = value[출현빈도수]
        nouns_count[noun] = nouns_count.get(noun, 0)+1

nouns_count
'''
{'형태소': 1,
 '분석': 3,
 '데이터': 2,
 '직업': 1,
 '전문가': 1,
 '기법': 1,
 '초반': 1,
 '개발': 1,
 '기술': 1}
'''
len(nouns_count)  # 9


# 4. WordCloud

# 1) top5 word
from collections import Counter # class

word_cnt = Counter(nouns_count)
top5_word = word_cnt.most_common(5)
top5_word
# [('분석', 3), ('데이터', 2), ('형태소', 1), ('직업', 1), ('전문가', 1)]

# 2) 시각화 word cloud
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=500, height=400,
          max_words = 100, max_font_size= 150, background_color='white')
# 다른건 다 생략해도 "한글"은 반드시 font_path='C:/Windows/Fonts/malgun.ttf' 해야함.

wc_result = wc.generate_from_frequencies(dict(top5_word)) #dict

import matplotlib.pyplot as plt

plt.imshow(wc_result)
#@@16
plt.axis('off') # 축의 눈금 감추기
plt.show()


















