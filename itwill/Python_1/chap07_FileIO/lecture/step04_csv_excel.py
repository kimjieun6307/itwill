'''
csv, excel file read/write
 - 칼럼 단위로 작성된 파일 유형

cmd에서 외부 라이브러리 설치
 pip install 패키지명
#@@19, #@@20
'''
import pandas as pd #as 별칭

import os
print(os.getcwd())

# 1. csv file read
spam_data = pd.read_csv("./chap07_FileIO/data/spam_data.csv", header=None, encoding='ms949')
print(spam_data.info()) # R에서 str()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4     ---> 관측치
Data columns (total 2 columns):   ---> 칼럼(0,1)
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   0       5 non-null      object
 1   1       5 non-null      object
dtypes: object(2)
memory usage: 208.0+ bytes
None
'''
print(spam_data)
'''
      0                        1
0   ham    우리나라    대한민국, 우리나라 만세
1  spam      비아그라 500GRAM 정력 최고!
2   ham               나는 대한민국 사람
3  spam  보험료 15000원에 평생 보장 마감 임박
4   ham                   나는 홍길동
'''
# 2. x, y 변수 선택
target = spam_data[0] # DataFrame[칼럼명]
texts = spam_data[1] # DF[칼럼명]
print(target)  # index data
'''
0     ham
1    spam
2     ham
3    spam
4     ham
Name: 0, dtype: object
'''
print(texts)
'''
0      우리나라    대한민국, 우리나라 만세
1        비아그라 500GRAM 정력 최고!
2                 나는 대한민국 사람
3    보험료 15000원에 평생 보장 마감 임박
4                     나는 홍길동
Name: 1, dtype: object
'''

# 3. target -> dummy
target = [1 if x=='spam' else 0 for x in target]
print(target) # [0, 1, 0, 1, 0]

# 4. text 전처리
# 텍스트 전처리 용도 함수
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
    # 영문 제거
    text_re5 = sub('[a-z]', '', text_re4)
    # 5. 공백 제거
    text_re6 = ' '.join(text_re5.split())
    return text_re6

clean_texts = [clean_text(i) for i in texts]
print('텍스트 전처리 후')
print(clean_texts)
#텍스트 전처리 후
#['우리나라 대한민국 우리나라 만세', '비아그라 정력 최고', '나는 대한민국 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동']

###################################################
## bmi.csv
###################################################
bmi = pd.read_csv("./chap07_FileIO/data/bmi.csv", encoding='utf-8')
print(bmi.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20000 entries, 0 to 19999
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   height  20000 non-null  int64   ---> 숫자형(연산가능)
 1   weight  20000 non-null  int64   ---> 숫자형
 2   label   20000 non-null  object  ---> 문자형
dtypes: int64(2), object(1)
memory usage: 468.9+ KB
None
'''
print(bmi.head()) # 앞부분 5개 관측치
'''
   height  weight   label
0     184      61    thin
1     189      56    thin
2     183      79  normal
3     143      40  normal
4     187      66  normal
'''
print(bmi.tail()) # 끝부분 5개
'''
       height  weight   label
19995     168      74     fat
19996     190      62    thin
19997     179      77  normal
19998     148      57     fat
19999     167      71     fat
'''

height = bmi['height'] # DF['칼럼명']
weight = bmi['weight']
label = bmi.label # DF.칼럼명

print(len(height)) # 20000
print(len(label)) # 20000

print('키 평균 : ', height.mean()) # 키 평균 :  164.9379
print('몸무게 평균 : ', weight.mean()) # 몸무게 평균 :  62.40995

# max(), min() --> 기본함수
max_h = max(height)
max_w = max(weight)
print("가장 큰 키 : ", max_h) # 가장 큰 키 :  190
print("가장 큰 몸무게 : ", max_w) # 가장 큰 몸무게 :  85

height_nor = height/max_h
weight_nor = weight/max_w
print(height_nor.mean()) # 0.8680942105263159
print(weight_nor.mean()) # 0.734234705882353

# 범주형 변수 : label
lab_cnt = label.value_counts() # 빈도수
print(lab_cnt)
'''
normal    7677
fat       7425
thin      4898
Name: label, dtype: int64
'''

# 2. excel file read
'''
pip install xlrd
'''
excel = pd.ExcelFile("./chap07_FileIO/data/sam_kospi.xlsx")
print(excel) # <pandas.io.excel._base.ExcelFile object at 0x000001D34B9A5048>

kospi = excel.parse('sam_kospi')
print(kospi)
'''
          Date     Open     High      Low    Close  Volume
0   2015-10-30  1345000  1390000  1341000  1372000  498776
1   2015-10-29  1330000  1392000  1324000  1325000  622336
2   2015-10-28  1294000  1308000  1291000  1308000  257374
3   2015-10-27  1282000  1299000  1281000  1298000  131144
4   2015-10-26  1298000  1298000  1272000  1292000  151996
..         ...      ...      ...      ...      ...     ...
242 2014-11-07  1218000  1218000  1195000  1206000  107688
243 2014-11-06  1198000  1210000  1193000  1204000  168497
244 2014-11-05  1215000  1225000  1194000  1202000  187182
245 2014-11-04  1219000  1242000  1205000  1217000  237045
246 2014-11-03  1250000  1252000  1216000  1235000  263940
[247 rows x 6 columns]
'''
print(kospi.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 247 entries, 0 to 246
Data columns (total 6 columns):
 #   Column  Non-Null Count  Dtype         
---  ------  --------------  -----         
 0   Date    247 non-null    datetime64[ns]
 1   Open    247 non-null    int64         
 2   High    247 non-null    int64         
 3   Low     247 non-null    int64         
 4   Close   247 non-null    int64         
 5   Volume  247 non-null    int64         
dtypes: datetime64[ns](1), int64(5)
memory usage: 11.7 KB
None
'''

# 3. csv file save
kospi['Diff'] = kospi.High - kospi.Low # 파생변수
print(kospi.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 247 entries, 0 to 246
Data columns (total 7 columns):
 #   Column  Non-Null Count  Dtype         
---  ------  --------------  -----         
 0   Date    247 non-null    datetime64[ns]
 1   Open    247 non-null    int64         
 2   High    247 non-null    int64         
 3   Low     247 non-null    int64         
 4   Close   247 non-null    int64         
 5   Volume  247 non-null    int64         
 6   Diff    247 non-null    int64         ★---> 파생변수
dtypes: datetime64[ns](1), int64(6)
memory usage: 13.6 KB
None
'''

# csv file 저장
kospi.to_csv("./chap07_FileIO/data/kospi_df.csv", index=None, encoding='utf-8')

kospi_df = pd.read_csv("./chap07_FileIO/data/kospi_df.csv", encoding='utf-8')
print(kospi_df.head())
'''
         Date     Open     High      Low    Close  Volume   Diff
0  2015-10-30  1345000  1390000  1341000  1372000  498776  49000
1  2015-10-29  1330000  1392000  1324000  1325000  622336  68000
2  2015-10-28  1294000  1308000  1291000  1308000  257374  17000
3  2015-10-27  1282000  1299000  1281000  1298000  131144  18000
4  2015-10-26  1298000  1298000  1272000  1292000  151996  26000
'''