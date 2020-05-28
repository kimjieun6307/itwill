'''
문2-1) 다음 벡터(emp)는 '입사년도이름급여'순으로 사원의 정보가 기록된 데이터 있다.
      이 벡터 데이터를 이용하여 사원의 이름만 추출하는 함수를 정의하시오. 

# <출력 결과>
 names = ['홍길동', '이순신', '유관순']
'''

from re import findall

# <Vector data>
emp = ["2014홍길동220", "2002이순신300", "2010유관순260", "2007 250"]

# 함수 정의 : 이름 추출
def name_pro(emp):
    # 내용 채우기
    names = [] # 빈 list
    for e in emp:
        tmp = findall('[가-힣]{3}',e)
        if tmp :
            names.append(tmp[0])
    return names
# 함수 호출
names = name_pro(emp)
print('names =', names) # names = ['홍길동', '이순신', '유관순']

#-------------------------------------------------------------

# <결측값 있을때 한줄로 처리하는거 모르겠음..>
name = [findall('[가-힣]{2,}', i) for i in emp]
def b(name) :
    if name:
        return(name[0])
    return


result=filter(b, name)
print(list(result)) # [['홍길동'], ['이순신'], ['유관순']]