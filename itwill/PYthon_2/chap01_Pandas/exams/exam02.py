'''
step02 관련문제
문2) wdbc_data.csv 파일을 읽어와서 단계별로 x, y 변수를 생성하시오.
     단계 1 : 파일 가져오기, 정보 확인 
     단계 2 : y변수 : diagnosis 
         x변수 : id 칼럼 제외  나머지 30개 칼럼
'''
import pandas as pd

# 단계 1 : 파일 가져오기, 정보 확인 
wdbc_data = pd.read_csv("C:\\ITWILL\\4_Python-II\\data\\wdbc_data.csv")
wdbc_data.info()
wdbc_data.head()
'''
         id diagnosis  ...  symmetry_worst  dimension_worst
0  87139402         B  ...          0.2827          0.06771
1   8910251         B  ...          0.2940          0.07587
2    905520         B  ...          0.2998          0.07881
3    868871         B  ...          0.2102          0.06784
4   9012568         B  ...          0.2487          0.06766
'''

# 단계 2 : y변수, x변수 선택
wdbc_col=list(wdbc_data.columns)
wdbc_col
wdbc_y = wdbc_col[1]
wdbc_y # 'diagnosis'

wdbc_x = wdbc_col[2:]
len(wdbc_x) # 30

x = wdbc_data[wdbc_x]
y = wdbc_data[wdbc_y]
x
y
