'''
문제2) 서울 지역을 대상으로 '동' 이름만 추출하여 다음과 같이 출력하시오.
  단계1 : 'ooo동' 문자열 추출 : 예) '개포1동 경남아파트' -> '개포1동'
  단계2 : 중복되지 않은 전체 '동' 개수 출력 : list -> set -> list
  
  <출력 예시>  
서울시 전체 동 개수 =  797
'''

import os
print(os.getcwd())

try :
    file = open("./chap07_FileIO/data/zipcode.txt", mode='r', encoding='utf-8')
    lines = file.readline() # 첫줄 읽기 
    dong = [] # 서울시 동 저장 list
    while lines :
        addr=lines.split(sep='\t')
        if addr[1] == '서울' :
             tmp =  addr[3].split()
             dong.append(tmp[0])
        lines = file.readline()

    dongs=list(set(dong)) # list -> set -> list

    print('서울시 전체 동 개수 ', len(dongs))
    print(dongs)

except Exception as e :
    print('예외발생 :', e)
    
    
    
    