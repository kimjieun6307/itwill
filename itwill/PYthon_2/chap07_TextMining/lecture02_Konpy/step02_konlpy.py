# -*- coding: utf-8 -*-
"""
Konlpy : 한글 형태소 분석을 제공하는 패키지

Anaconda prompt에서 패키지 인스톨 : pip install konlpy
"""

import konlpy
from konlpy.tag import Kkma # class


kkma = Kkma() # class 생성자 -> object 생성 : 원하는 형태로 형태소 분석

# (1) 문단 -> 문장
para = "나는 홍길동 입니다. 나이는 23세 입니다. 대한민국 만세 입니다." 
ex_sent = kkma.sentences(para)
ex_sent # list
#  ['나는 홍길동 입니다.', '나이는 23세 입니다.', '대한민국 만세 입니다.']
len(ex_sent)  # 3


# (2) 문단 -> 단어(명사)
ex_nouns = kkma.nouns(para)
ex_nouns
# ['나', '홍길동', '나이', '23', '23세', '세', '대한', '대한민국', '민국', '만세']

#@@13 -> 형태소

# (3) 문단 -> 품사(형태소) : "형태소 분석"
ex_pos = kkma.pos(para)
ex_pos
'''
[('나', 'NP'),
 ('는', 'JX'),
 ('홍길동', 'NNG'),
 ('이', 'VCP'),
 ('ㅂ니다', 'EFN'),
 ('.', 'SF'),
 ~~
'''
type(ex_pos) # list [('word', '품사기호'), ( , ), ...]

#▶ NNG 일반 명사 NNP 고유 명사 NP 대명사 => 원하는 품사만 선택
nouns = [] # 명사 저장

for word, wclass in ex_pos:
    if wclass == 'NNG' or wclass == 'NNP' or wclass == 'NP' :
        nouns.append(word)

nouns   
# ['나', '홍길동', '나이', '대한민국', '만세']






