'''
1. pickle file load
2. 텍스트 전처리
3. word count
'''
import pickle

# 1. pickle file load
file = open('../data/new_crawling.pickle', mode='rb')
news_crawling = pickle.load(file)
print(type(news_crawling))
print(news_crawling) #@@14

# 2. 텍스트 전처리
def clean_text(texts) : # chap05 > step02 참고
    from re import sub
    # 1. 소문자 변경
    texts_re = texts.lower() # 문장 1개 소문자 변경
    # 2. 숫자 제거
    texts_re2 = sub('[0-9]', '', texts_re)
    # 3. 문장부호 제거
    punc_str = '[.,;:?!"]'
    text_re3 = sub(punc_str, '', texts_re2)
    # 4. 특수문자 제거
    spec_str = '[@#$%^&*()]'
    text_re4 = sub(spec_str, '', text_re3)
    # 5. 공백 제거
    text_re5 = ' '.join(text_re4.split())

    return text_re5

clean_news = [clean_text(news) for news in news_crawling]
print(clean_news) #@@15

# 3. word count -- 공백을 단위로 나누는 것으로 가정
word_count = {}
for texts in clean_news:
    for word in texts.split() :
        word_count[word] = word_count.get(word, 0) + 1

print(word_count)
#{'김용태': 1, '윤석열': 2, '거취': 2, '거론은': 1, '오만방자': 1, 'vs': 1, '우희종': 3, '개인': 3, ..}

word_count2 = word_count.copy()  # 객체 복제

# 2음절 이상 단어 선택
for word in word_count.keys() :
    if len(word) < 2 :
        del word_count2[word] # 2음절 미만 key값은 제거

print(word_count2) #@@16

# 단어 빈도수 top10 or top5
''' 패키지 설치 필요 #@@17
pip install collections-extended
'''
from collections import Counter
count = Counter(word_count2)

top5 = count.most_common(5)
print('top5')
print(top5) # [('none', 19), ('코로나', 4), ('[바로잡습니다]', 4), ('우희종', 3), ('개인', 3)]

# 불용어 제거
del count['none']
del count['[바로잡습니다]']

top5 = count.most_common(5)
print('top5')
print(top5) # [('코로나', 4), ('우희종', 3), ('개인', 3), ('부산', 3), ('확진', 3)]

top10 = count.most_common(10)
print('top10')
print(top10)
# [('코로나', 4), ('우희종', 3), ('개인', 3), ('부산', 3), ('확진', 3), ('수출', 3), ('소득', 3), ('기여도는', 3), ('정부', 3), ('윤석열', 2)]

# list[(), () ]
import pandas as pd
top10_df = pd.DataFrame(top10)
print(top10_df)
'''
      0  1
0   코로나  4
1   우희종  3
2    개인  3
3    부산  3
4    확진  3
5    수출  3
6    소득  3
7  기여도는  3
8    정부  3
9   윤석열  2
'''

top10_df = pd.DataFrame(top10, columns=['word', 'count'])
print(top10_df)
'''
   word  count
0   코로나      4
1   우희종      3
2    개인      3
3    부산      3
4    확진      3
5    수출      3
6    소득      3
7  기여도는      3
8    정부      3
9   윤석열      2
'''

# 시각화
'''
pip install matplotlib
'''
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 선 그래프 : plt.plot(x축, y축)
plt.plot(top10_df['word'], top10_df['count'])
plt.title('top10 word count')
plt.show()

# 막대 그래프 : plt.bar(x축, y축)
plt.bar(top10_df['word'], top10_df['count'])
plt.title('top10 word count')
plt.show()
