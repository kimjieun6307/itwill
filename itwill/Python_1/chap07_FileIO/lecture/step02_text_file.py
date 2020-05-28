'''
텍스트 파일 입출력
형식)
    open(file, mode='r', 'w', 'a') # 기본값 'r'
'''

import os # 파일 경로 확일할때 사용하는 모듈 os

try:
    #print('현재 경로 : ', os.getcwd()) # R의 getwd()와 같음 기능
    #현재 경로 :  C:\ITWILL\3_Python-I\workspace

    # file open : 절대 경로
    file = open( os.getcwd()+'/chap07_FileIO/data/ftest.txt', mode='r') 
    print(file.read()) # file 사용
    file.close() #file 닫기


    # file open : 상대 경로 (. : 현재 디렉터리, .. : 상위 디렉터리)
    file = open('./chap07_FileIO/data/ftest.txt', mode='r')
    print(file.read())  # file 사용
    file.close()  # file 닫기

    # 2. 파일 쓰기(mode = 'w')
    file2 = open('./chap07_FileIO/data/ftest2.txt', mode='w')
    file2.write("my first text~~")
    file2.close()

    # 3. 파일 쓰기 (내용 추가 : mode = 'a')
    file3 = open('./chap07_FileIO/data/ftest2.txt', mode='a')
    file3.write("\nmy second text~~")
    file3.close()
    '''
    file.read() : 전체 문서 전부 한번에 읽기
    file.readline() : 전체 문서에서 한 줄만 읽기
    file.readlines() : 전체 문서를 전부를 줄 단위 읽기
    '''


    # 4. readline() : 한 줄만 읽기
    file4 = open('./chap07_FileIO/data/ftest2.txt')
    row_a = file4.read()
    print(row_a)
    row = file4.readline()
    print('row = ', row) # row =  my first text~~
    file4.close()

    # readline() 반복문으로 읽기
    file4 = open('./chap07_FileIO/data/ftest2.txt')
    for i in range(2) :       # for i in range(len(file4)) ---error
        row = file4.readline()
        print('row = '+ str(i), row) # row =  my first text~~
    file4.close()

    # 5. readlines() : 전체 문장을 줄단위 읽기
    file5 = open('./chap07_FileIO/data/ftest2.txt')
    rows = file5.readlines()
    print('readlines = ', rows) # readlines =  ['my first text~~\n', 'my second text~~']

    for row in rows : #  ['my first text~~\n', 'my second text~~']
        for sent in row.split('\n'): # 'my first text~~\n' ---> 불용어 제거(\n)
            if sent :
                print(sent)

    # string.strip() : 문장 끝 불용어(공백, \n\t 기타) 제거
    print('strip 함수')
    for row in rows :
        print(row.strip())
    file5.close()
    '''
    strip 함수
    my first text~~
    my second text~~ 
    '''

    str_text = "agsgs234 \n \t\r"
    print('str_text : ', str_text.strip()) # str_text :  agsgs234
    '''
    row = 0 my first text~~
    row = 1 my second text~~ 
    '''

    # 6. with
    with open('./chap07_FileIO/data/ftest3.txt', mode='w', encoding="utf-8") as file6 :
        file6.write("파이썬 파일 작성 연습")
        file6.write("\n파이썬 파일 작성 연습2")

    with open('./chap07_FileIO/data/ftest3.txt', mode='r', encoding="utf-8") as file7:
        print(file7.read())

except FileNotFoundError as e:
    print('예외정보 : ', e)
finally :
    pass
#@@ 10, #@@ 11 ~ 15
