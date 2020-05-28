''' 
step02 관련문제 
문1) score.csv 파일을 읽어와서 다음과 같이 처리하시오.
   조건1> tv 칼럼이 0인 관측치 2개 삭제 (for, if문 이용)
   조건2> score, academy 칼럼만 추출하여 DataFrame 생성
   조건3> score, academy 칼럼의 평균 계산 
   - <<출력 결과 >> 참고    
   
<<출력 결과 >>
   score  academy
1     75        1
2     77        1
3     83        2
4     65        0
5     80        3
6     83        3
7     70        1
9     79        2
score      76.500
academy     1.625   
'''

import pandas as pd

score = pd.read_csv("C:\\ITWILL\\4_Python-II\\data\\score.csv")

score.info()
'''<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 6 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   name     10 non-null     object
 1   score    10 non-null     int64 
 2   iq       10 non-null     int64 
 3   academy  10 non-null     int64 
 4   game     10 non-null     int64 
 5   tv       10 non-null     int64 
 '''
 
score.head()

# 조건1> tv 칼럼이 0인 관측치 2개 삭제 (for, if문 이용)
dir(score)
tv = score['tv']
for i in range(len(tv)):
    if tv[i]==0 :
        score = score.drop(i)
'''
for i, c in enumerate(tv) :
    if c == 0 :
        score = score.drop(i)
'''

score
'''
  name  score   iq  academy  game  tv
1    B     75  125        1     3   3
2    C     77  120        1     0   4
3    D     83  135        2     3   2
4    E     65  105        0     4   4
5    F     80  123        3     1   1
6    G     83  132        3     4   1
7    H     70  115        1     1   3
9    J     79  131        2     2   3
'''


score_df=score[score.tv >0]
score_df
'''  name  score   iq  academy  game  tv
1    B     75  125        1     3   3
2    C     77  120        1     0   4
3    D     83  135        2     3   2
4    E     65  105        0     4   4
5    F     80  123        3     1   1
6    G     83  132        3     4   1
7    H     70  115        1     1   3
9    J     79  131        2     2   3
'''

df=score_df[['score', 'academy']]
df
'''
   score  academy
1     75        1
2     77        1
3     83        2
4     65        0
5     80        3
6     83        3
7     70        1
9     79        2
'''

df.mean()
'''
score      76.500
academy     1.625
'''

df.mean(axis=0)
df['score'].mean() # 76.5
df['academy'].mean() # 1.625

