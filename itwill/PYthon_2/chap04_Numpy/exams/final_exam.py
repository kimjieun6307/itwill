# -*- coding: utf-8 -*-
"""
Zeros Matrix -> Sparse Matrix
문) 영행렬(zero matrix) 이용하여 희소행렬(sparse matrix) 만들기
    <조건1> 단계1과 단계2는 문장과 단어를 만드는 단계(작업이 왼성되었음)
    <조건2> 단계3 부터 문제를 해결하시오.
"""

## 단계1 : 다음 texts를 대상으로 줄 단위로 5개 문장(stances) 만들기 
texts = """우리나라 대한민국 우리나라 대한민국 만세
비아그라 정력 최고
나는 대한민국 사람
보험료 평생 보장 마감 임박
나는 홍길동"""

tokens = texts.split('\n') # 줄 단위로 토큰 생성 
print(tokens)
'''
['우리나라 대한민국 우리나라 만세', '비아그라 정력 최고', '나는 대한민국 사람', '보험료 평생 보장 마감 임박', '나는 홍길동']
'''
# [해설] texts를 대상으로 줄 단위로 문자열을 생성하기 위해서 줄바꿈 기호('\n')를 이용한다.  


## 단계2 : 문장과 단어 만들기 
stentens = tokens
words = []
for st in stentens : # 문장 만들기 
    for word in st.split() : # 단어 만들기  
        words.append(word)
        
    
print('문장 개수 =', len(stentens)) # 문장 개수 = 5
print('단어 개수 =', len(words)) # 단어 개수 = 18
# [해설] 단계1에서 생성한 tokens를 대상으로 문장(stantens)과 문장을 구성하는 단어(words) 생성


## 단계3 : 영행렬(zeros matrix) 만들기
# [설명] 단계2에서 생성한 문장 개수 만큼 행 크기, '중복되지 않은' 단어 개수 만큼 열 크기로 영행렬 생성
import numpy as np
import pandas as pd

words_pd = pd.Series(words)
words_uni=words_pd.unique()
len(words_uni)

# words_arr=np.array(words)
# words_arr.unique

zero_matrix = np.zeros((len(stentens), len(words_uni)))
zero_matrix.shape

# [영행렬(5x14) 완성 결과화면] 5=문장 개수, 14=중복되지 않은(unique) 단어수
'''
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
'''



## 단계4 : 데이터프레임 만들기 
# [설명] 단계3에서 만든 영행렬을 대상으로 각 열에 중복되지 않은 단어를 열 이름으로 지정(colmns)

data = pd.DataFrame(data = zero_matrix, columns=words_uni)
data
# [데이터프레임(5x14) 결과화면] 
'''
   대한민국   만세   보장   최고  보험료   임박   나는   정력   마감  홍길동  비아그라   사람   평생  우리나라
0   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0   0.0  0.0  0.0   0.0
1   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0   0.0  0.0  0.0   0.0
2   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0   0.0  0.0  0.0   0.0
3   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0   0.0  0.0  0.0   0.0
4   0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0   0.0  0.0  0.0   0.0
'''
########################################################################################
# 단계5 : 희소행렬 만들기 
# [설명] 단계4에서 만든 DataFrame을 대상으로 각 문서에서 출현한 단어의 수 만큼 셀에 채우기
'''
words_cnt = words_pd.value_counts()
type(words_cnt) # pandas.core.series.Series

for i in words_uni:
     print(i,' 빈도수 : ', words_cnt[i])


for i in range(len(stentens)):
    for j in  words_uni:
        data[i,j] = words_cnt[j]
'''

# 객체 복사(깊은 복사) : 서로 다른 주소로 복사됨
zero_copy = data.copy()
id(zero_matrix) # 3079344676336
id(zero_copy) # 3079345201200

for doc, st in enumerate(stentens) : # 문장 위치와 문장
    for word in st.split() : #  문장 -> 단어 분리
        zero_copy.loc[doc, word] +=1 # 문장과 단어 위치 이용 카운터

zero_copy

# [희소행렬(5x14) 결과화면] 
'''
   대한민국   만세   보장   최고  보험료   임박   나는   정력   마감  홍길동  비아그라   사람   평생  우리나라
0   2.0  1.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0  0.0   0.0  0.0  0.0   2.0
1   0.0  0.0  0.0  1.0  0.0  0.0  0.0  1.0  0.0  0.0   1.0  0.0  0.0   0.0
2   1.0  0.0  0.0  0.0  0.0  0.0  1.0  0.0  0.0  0.0   0.0  1.0  0.0   0.0
3   0.0  0.0  1.0  0.0  1.0  1.0  0.0  0.0  1.0  0.0   0.0  0.0  1.0   0.0
4   0.0  0.0  0.0  0.0  0.0  0.0  1.0  0.0  0.0  1.0   0.0  0.0  0.0   0.0
'''
#[해설] 첫번째 문장에서 '대한민국'과 '우리나라' 단어는 2회씩 출현 

stentens
'''
['우리나라 대한민국 우리나라 대한민국 만세',
 '비아그라 정력 최고',
 '나는 대한민국 사람',
 '보험료 평생 보장 마감 임박',
 '나는 홍길동']
'''
for doc, st in enumerate(stentens) :
    print('doc : ', doc)
    print('st : ', st)
'''
doc :  0
st :  우리나라 대한민국 우리나라 대한민국 만세
doc :  1
st :  비아그라 정력 최고
doc :  2
st :  나는 대한민국 사람
doc :  3
st :  보험료 평생 보장 마감 임박
doc :  4
st :  나는 홍길동
'''

    


