'''
사용자 정의 함수 응용
'''

# 1. 텍스트 전처리 용도 함수
def clean_text(texts) :
    from re import sub
    # 1. 소문자 변경
    texts_re = texts.lower() # 문장 1개 소문자 변경
    # 2. 숫자 제거
    texts_re2 = sub('[0-9]', '', texts_re)
    # 3. 문장부호 제거
    punc_str = '[.,;:?!]'
    text_re3 = sub(punc_str, '', texts_re2)
    # 4. 특수문자 제거
    spec_str = '[@#$%^&*()]'
    text_re4 = sub(spec_str, '', text_re3)
    # 5. 공백 제거
    text_re5 = ' '.join(text_re4.split())
    return text_re5

# 텍스트 전처리
texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']
print('텍스트 전처리 전')
print(texts)
print(len(texts)) # 5

print("텍스트 전처리 후")
texts_re =[clean_text(i) for i in texts] # --list내 for 이용해서 함수(clean_text()) 사용
print(texts_re)

#-------------------------------------------------------------------------------------------

# 2. 표본의 분산과 표준편차
from statistics import mean, variance, stdev # 통계함수
from math import sqrt # 수학함수
dataset = [2, 4, 5, 6, 1, 8]

print('mean = ', mean(dataset)) # mean =  4.333333333333333
print('var = ', variance(dataset)) #var =  6.666666666666666
print('std = ', stdev(dataset)) # std =  2.581988897471611
'''
분산 = sum((x변령 -평균)**2) / (n-1)
표준편차 = sqrt(분산)
'''

def var_std(dataset):
    avg = mean(dataset) # 산술평균
    # list + for
    diff = [(x-avg)**2 for x in dataset ]
    diff_sum = sum(diff)
    var = diff_sum / (len(dataset)-1) # 분산
    std= sqrt(var) # 표준편차
    return var, std

# 함수 호출
var, std = var_std(dataset)
print('분산 = ', var) # 분산 =  6.666666666666666
print('표준편차 = ', std) # 표준편차 =  2.581988897471611