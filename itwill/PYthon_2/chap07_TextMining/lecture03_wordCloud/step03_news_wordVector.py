# -*- coding: utf-8 -*-
"""
★ WordVector => 희소행렬 만들기 위한 과정

news crawling data -> word vector
     문장 -> 단어 벡터(word vector) -> 희소행렬(Sparse matrix)
     ex) '직업은 데이터 분석가 입니다.' -> '직업 데이터 분석가'
    : 명사만 추출한 다음 공백으로 묶기


# 수업때 만든 'new_data.pck' 희소행렬 만들기
    1. pickle file 읽기
    2. 명사 추출 : kkma.nouns()이용해서 word vector (전처리 : 단어길이 제한, 숫자 제외)
    3.  
    4. WordCloud
"""

from konlpy.tag import Kkma
from wordcloud import WordCloud
import pickle

# object 생성
kkma=Kkma()

# 1. pickle file 읽기 : news_data.pck
file = open('../data/new_data.pck', mode='rb')
news_data = pickle.load(file)
file.close()

news_data[:5]
type(news_data) # list
len(news_data) # 11600


# 2. docs -> sentence
ex_sent = [kkma.sentences(sent)[0]  for sent in news_data]
ex_sent

len(ex_sent) # 11600


# 3. sentence -> word vector
from re import match

sentence_nouns=[] # 단어 벡터 제공
for sent in ex_sent : 
    word_vec = ""
    for noun in kkma.nouns(sent) : # 문장 -> 명사 추출
        if len(noun) > 1 and not(match('^[0-9]', noun )) :   # 음절 2개 이상, 숫자 제외
            word_vec += noun + " " # 명사 누적(한 칸씩 띄워서)
    
    print(word_vec)
    sentence_nouns.append(word_vec)
    
len(sentence_nouns) # 11600

# 문장번호 1(첫번째)
ex_sent[0]        # '의협 " 감염병 위기 경보 상향 제안.. 환자 혐오 멈춰야"'
sentence_nouns[0] # '의협 감염병 위기 경보 상향 제안 환자 혐오 ' => 명사만 추출

# 문장번호 11600(마지막)
ex_sent[-1]         # '미, 인건비 우선 협의 제안에 " 포괄적 SMA 신속 타결 대단히 손상"'
sentence_nouns[-1]  #  '인건비 우선 협의 제안 포괄적 신속 타결 손상 '


# 4. file save
file = open('../data/sentence_nouns.pickle', mode='wb')
pickle.dump(sentence_nouns, file)
print('file save')
file.close()


#  file load
file = open('../data/sentence_nouns.pickle', mode='rb')
word_vector = pickle.load(file)
word_vector[0]
file.close()






































