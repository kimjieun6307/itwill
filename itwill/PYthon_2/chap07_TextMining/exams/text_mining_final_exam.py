'''
TextMining 최종문제  

문) movies.dat 파일의 자료를 이용하여 다음과 같이 단계별로 단어의 빈도수를 구하고,
    단어 구름으로 시각화하시오.
'''

import pandas as pd
import numpy as np

# [단계1] 영화 dataset 가져오기  
name = ['movie_id', 'title', 'genres']
movies = pd.read_csv('../data/movies.dat', sep='::', header=None, names=name )
print(movies.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3883 entries, 0 to 3882
Data columns (total 3 columns):
movie_id    3883 non-null int64 -> 각 영화 구분자 
title       3883 non-null object -> 영화 제목 
genres      3883 non-null object -> 영화 장르 : 한 개 이상의 장르(genres) 구성됨  
'''
print(movies.head())
'''
   movie_id                               title                        genres
0         1                    Toy Story (1995)   Animation|Children's|Comedy
1         2                      Jumanji (1995)  Adventure|Children's|Fantasy
2         3             Grumpier Old Men (1995)                Comedy|Romance
3         4            Waiting to Exhale (1995)                  Comedy|Drama
4         5  Father of the Bride Part II (1995)                        Comedy
'''
print('전체 영화수 : ', len(movies)) # 전체 영화수 :  3883


# [단계2] zero 행렬 만들기[행수 : 전체 영화수, 열수 : 중복되지 않은 장르 수]  
# 힌트 : 중복되지 않은 장르 수 구하기
# 각 영화의 장르는 구분자(|)에 의해서 1개 이상의 장르로 구성된 문자열이다.
# 따라서 중복되지 않은 장르 수를 구하기 위해서 구분자(|)를 기준으로 split하여 
# 토큰을 생성한 후 중복을 제거한다.
genres = movies.genres
type(genres) # pandas.core.series.Series
genres[:5]
'''
0     [Animation, Children's, Comedy]
1    [Adventure, Children's, Fantasy]
2                   [Comedy, Romance]
3                     [Comedy, Drama]
4                            [Comedy]
'''

genres = [i.split(sep='|')[0] for i in genres]
genres[:5]
'''
['Animation', 'Adventure', 'Comedy', 'Comedy', 'Comedy']
'''

uni_genres = np.unique(genres)
len(uni_genres) # 18

row=len(movies) # 3883
col=len(uni_genres) # 18

zero_matrix = np.zeros((row, col))





# [단계3] zero 행렬 -> DataFrame 변환(열 제목 = 장르명) 
# 설명 : zero 행렬을 대상으로 열 이름에 장르명을 지정하여 DataFrame을 생성한다.

data = pd.DataFrame(data=zero_matrix, columns=uni_genres)
data
'''
      Action  Adventure  Animation  Children's  ...  Sci-Fi  Thriller  War  Western
0        0.0        0.0        0.0         0.0  ...     0.0       0.0  0.0      0.0
1        0.0        0.0        0.0         0.0  ...     0.0       0.0  0.0      0.0
2        0.0        0.0        0.0         0.0  ...     0.0       0.0  0.0      0.0
3        0.0        0.0        0.0         0.0  ...     0.0       0.0  0.0      0.0
4        0.0        0.0        0.0         0.0  ...     0.0       0.0  0.0      0.0
     ...        ...        ...         ...  ...     ...       ...  ...      ...
3878     0.0        0.0        0.0         0.0  ...     0.0       0.0  0.0      0.0
3879     0.0        0.0        0.0         0.0  ...     0.0       0.0  0.0      0.0
3880     0.0        0.0        0.0         0.0  ...     0.0       0.0  0.0      0.0
3881     0.0        0.0        0.0         0.0  ...     0.0       0.0  0.0      0.0
3882     0.0        0.0        0.0         0.0  ...     0.0       0.0  0.0      0.0

[3883 rows x 18 columns]
'''


# [단계4] 희소행렬(Sparse matrix) 생성 
# 설명 : 각 영화별로 해당 장르에 해당하는 교차 셀에 0 -> 1 교체하여 희소행렬을 만든다.
# 힌트 : index와 내용을 반환하는 enumerate() 함수 이용 

zero_copy = data.copy()

genres = movies.genres

for inx, gen in enumerate(genres) :
    for g in gen.split(sep='|') : 
        zero_copy.loc[inx, g] +=1 

zero_copy[:5]
'''
   Action  Adventure  Animation  Children's  ...  Sci-Fi  Thriller  War  Western
0     0.0        0.0        1.0         1.0  ...     0.0       0.0  0.0      0.0
1     0.0        1.0        0.0         1.0  ...     0.0       0.0  0.0      0.0
2     0.0        0.0        0.0         0.0  ...     0.0       0.0  0.0      0.0
3     0.0        0.0        0.0         0.0  ...     0.0       0.0  0.0      0.0
4     0.0        0.0        0.0         0.0  ...     0.0       0.0  0.0      0.0
'''



# [단계5] 단어문서 행렬(TDM) 만들기 
# 설명 : 희소행렬(Sparse matrix)에 전치행렬을 적용하여 장르명과 영화 축을 교체한다. 
# 힌트 : 전치행렬 -> 형식) 데이터프레임객체.T 
tdm = zero_copy.T
'''
             0     1     2     3     4     ...  3878  3879  3880  3881  3882
Action        0.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Adventure     0.0   1.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Animation     1.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Children's    1.0   1.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Comedy        1.0   0.0   1.0   1.0   1.0  ...   1.0   0.0   0.0   0.0   0.0
Crime         0.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Documentary   0.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Drama         0.0   0.0   0.0   1.0   0.0  ...   0.0   1.0   1.0   1.0   1.0
Fantasy       0.0   1.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Film-Noir     0.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Horror        0.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Musical       0.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Mystery       0.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Romance       0.0   0.0   1.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Sci-Fi        0.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Thriller      0.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   1.0
War           0.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0
Western       0.0   0.0   0.0   0.0   0.0  ...   0.0   0.0   0.0   0.0   0.0

[18 rows x 3883 columns]
'''
title = movies.title

tdm.columns = title
'''
title        Toy Story (1995)  ...  Contender, The (2000)
Action                    0.0  ...                    0.0
Adventure                 0.0  ...                    0.0
Animation                 1.0  ...                    0.0
Children's                1.0  ...                    0.0
Comedy                    1.0  ...                    0.0
Crime                     0.0  ...                    0.0
Documentary               0.0  ...                    0.0
Drama                     0.0  ...                    1.0
Fantasy                   0.0  ...                    0.0
Film-Noir                 0.0  ...                    0.0
Horror                    0.0  ...                    0.0
Musical                   0.0  ...                    0.0
Mystery                   0.0  ...                    0.0
Romance                   0.0  ...                    0.0
Sci-Fi                    0.0  ...                    0.0
Thriller                  0.0  ...                    1.0
War                       0.0  ...                    0.0
Western                   0.0  ...                    0.0

[18 rows x 3883 columns]
'''


# [단계6] 장르 빈도수(word count)
# 설명 : 단어문서 행렬(TDM)를 대상으로 행 단위 합계를 계산하여 장르별 출현빈도수를 계산한다. 
# 힌트 : dict() 이용하여 장르명과 빈도수를 key : value 형식으로 만든다.
gen_sum = tdm.sum(axis = 1)
'''
Action          503.0
Adventure       283.0
Animation       105.0
Children's      251.0
Comedy         1200.0
~~
'''

gen_dict = dict(gen_sum)
'''
{'Action': 503.0,
 'Adventure': 283.0,
 'Animation': 105.0,
 "Children's": 251.0,
 'Comedy': 1200.0,
 ~~
 '''

# [단계7] 단어 구름 시각화
# 설명 : 장르 빈도수를 Counter 객체를 생성하고, WordCloud 클래스를 이용하여 단어 구름으로 시각화한다.
from collections import Counter
word_cnt = Counter(gen_dict)
'''Counter({'Action': 503.0,
         'Adventure': 283.0,
         'Animation': 105.0,
         "Children's": 251.0,
         'Comedy': 1200.0,
~~
'''


top5_word = word_cnt.most_common(5)
'''
[('Drama', 1603.0),
 ('Comedy', 1200.0),
 ('Action', 503.0),
 ('Thriller', 492.0),
 ('Romance', 471.0)]
'''

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=800, height=600,
          max_words = 100, max_font_size= 200, background_color='white')

wc_result = wc.generate_from_frequencies(word_cnt) 

​

import matplotlib.pyplot as plt
plt.imshow(wc_result)
plt.axis('off') # 축의 눈금 감추기
plt.show()
#@@4



















