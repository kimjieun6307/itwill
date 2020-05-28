'''
문4) 다음 texts 객체를 대상으로 단계별로 텍스트를 전처리하시오. 

 <텍스트 전처리 후 결과> 
['우리나라 대한민국 우리나라 만세', '비아그라 정력 최고', '나는 대한민국 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동']
'''

# 전처리 전 텍스트
texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']


from re import sub

print('전처리 전 : ', texts)

# 1. 소문자 변경
text_1=[i.lower() for i in texts]
print(text_1)

# 2. 숫자 제거 
text_2 = [sub('[0-9]', '', i) for i in text_1]
print(text_2)

# 3. 문장부호 제거
bu='[,.?!]'
text_3=[sub(bu, '', i) for i in text_2]
print(text_3)
#== text_3=[sub('[,.?!]', '', i) for i in text_2]

# 4. 영문자 제거
text_4 = [sub('[a-z|A-Z]', '', i) for i in text_3]
print(text_4)

# 5. 특수문자 제거 
ss='[@#$%^&*]'
text_5 = [ sub(ss, '', i) for i in text_4]
print(text_5)
#== text_5 = [ sub('[@#$%^&*()]', '', i) for i in text_4]

# 6. 공백 제거(2칸 이상 공백 -> 1칸 공백)
# result = [ ''.join(i.split()) for i in text_5]
# print(result) # ['우리나라대한민국우리나라만세', '비아그라정력최고', '나는대한민국사람', '보험료원에평생보장마감임박', '나는홍길동']

result = [ ' '.join(i.split()) for i in text_5]
print(result) # ['우리나라 대한민국 우리나라 만세', '비아그라 정력 최고', '나는 대한민국 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동']

