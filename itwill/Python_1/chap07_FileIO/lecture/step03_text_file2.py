'''
우편번호 검색
[우편번호]tab[도/시]tab[구]tab[동]
135-806	서울	강남구	개포1동 경남아파트		1
[우편번호]tab[도/시]tab[구]tab[동]tab[세부주소]
135-807	서울	강남구	개포1동 우성3차아파트	(1∼6동)	2
'''

import os
print(os.getcwd()) # C:\ITWILL\3_Python-I\workspace\chap07_FileIO\lecture

# 동 검색
try :
    dong = input("동을 입력하세요 : ")
    file = open("./chap07_FileIO/data/zipcode.txt", mode='r', encoding='utf-8')
    line = file.readline() # 첫번째 줄 읽음

    print(line) # 한줄 출력  => ﻿135-806	서울	강남구	개포1동 경남아파트		1
    print(line.split(sep='\t')) # 토큰(구분자 단위)단위로 쪼갬 
    # ['\ufeff135-806', '서울', '강남구', '개포1동 경남아파트', '', '1\n']

    while line : # null == False
        addr=line.split(sep='\t')
        if addr[3].startswith(dong) :
            print('['+addr[0]+']', addr[1], addr[2], addr[3], addr[4])
        line = file.readline() # 두번째 줄 읽음 ~ n번째 줄 읽음(주소가 없을때(null)까지 while문 반복)

except  Exception as e:
    print('예외발생 : ', e)
finally:
    pass
#@@18


