import pandas as pd

election = pd.read_csv('../data/election_2012.csv', encoding='ms949')
print(election.info())
'''
cand_id : 대선 후보자 id
cand_nm : 대선 후보자 이름
contbr_nm : 후원자 이름 
contbr_occupation : 후원자 직업군 
contb_receipt_amt : 후원금 
등등
'''

# DF 객체 생성 
name = ['cand_nm', 'contbr_occupation', 'contb_receipt_amt'] 
# subset 생성 
election_df = pd.DataFrame(election, columns= name)
print(election_df.info())
print(election_df.head())
print(election_df.tail())


# 중복되지 않은 대선 후보자 추출 
unique_name = election_df['cand_nm'].unique()
print(len(unique_name)) 
print(unique_name) 

# 중복되지 않은 후원자 직업군 추출 
unique_occ =  election_df['contbr_occupation'].unique()
print(len(unique_occ)) 
print(unique_occ)

#############################################
#  Obama, Barack vs Romney, Mitt 후보자 분석 
#############################################

# 1. 두 후보자 관측치만 추출 : isin()
two_cand_nm=election_df[election_df.cand_nm.isin(['Obama, Barack','Romney, Mitt'])]
print(two_cand_nm.head())
print(two_cand_nm.tail())
print(len(two_cand_nm)) # 700975
'''
문1) two_cand_nm 변수를 대상으로 피벗테이블 생성하기 
    <조건1> 교차셀 칼럼 : 후원금, 열 칼럼 : 대선 후보자,
             행 칼럼 : 후원자 직업군, 적용함수 : sum
    <조건2> 피벗테이블 앞부분 5줄 확인   
문2) 피벗테이블 대상 필터링 : 2백만달러 이상 후원금 대상     
'''
two_cand_nm.info()

ptab=pd.pivot_table(two_cand_nm, index='contbr_occupation', columns='cand_nm', 
                    values='contb_receipt_amt', aggfunc='sum')

ptab.head()
'''
cand_nm                              Obama, Barack  Romney, Mitt
contbr_occupation                                               
   MIXED-MEDIA ARTIST / STORYTELLER          100.0           NaN
 AREA VICE PRESIDENT                         250.0           NaN
 RESEARCH ASSOCIATE                          100.0           NaN
 TEACHER                                     500.0           NaN
 THERAPIST                                  3900.0           NaN
'''

ptab.info()
'''
<class 'pandas.core.frame.DataFrame'>
Index: 33605 entries,    MIXED-MEDIA ARTIST / STORYTELLER to ZOOLOGY EDUCATION
Data columns (total 2 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Obama, Barack  29168 non-null  float64
 1   Romney, Mitt   6823 non-null   float64
 '''

# 문2) 피벗테이블 대상 필터링 : 2백만달러 이상 후원금 대상
# ptab[ptab.cand_nm >= 200] --error
# ptab[ptab[Obama, Barack] >= 200] --error
ptab2 = ptab[ptab.sum(axis = 1) >= 2000000]
ptab2.shape # (13, 2)
ptab2
'''
cand_nm                                 Obama, Barack  Romney, Mitt
contbr_occupation                                                  
ATTORNEY                                  11126932.97    5302578.82
CEO                                        2069784.79     353310.92
CONSULTANT                                 2459812.71    1404576.94
EXECUTIVE                                  1355161.05    2230653.79
HOMEMAKER                                  4243394.30    8037250.86
INFORMATION REQUESTED                      4849801.96           NaN
INFORMATION REQUESTED PER BEST EFFORTS            NaN   11173374.84
INVESTOR                                    884133.00    1494725.12
LAWYER                                     3159391.87       7705.20
PHYSICIAN                                  3732387.44    1332996.34
PRESIDENT                                  1878009.95    2403439.77
PROFESSOR                                  2163571.08     160362.12
RETIRED                                   25270507.23   11266949.23
'''

# 문) 두 후보자 모두 200만달러 이상 후원금을 지불한 직업군 필터링
# ptab[ptab['Obama, Barack']>=2000000 and ptab['Romney, Mitt']>=2000000]
import numpy as np
ptab3 = ptab[np.logical_and(ptab['Obama, Barack']>=2000000, ptab['Romney, Mitt']>=2000000)]
ptab3.shape # (3, 2)
ptab3
'''
cand_nm            Obama, Barack  Romney, Mitt
contbr_occupation                             
ATTORNEY             11126932.97    5302578.82
HOMEMAKER             4243394.30    8037250.86
RETIRED              25270507.23   11266949.23
'''

# 문) 두 후보자 중 한명 이상에게 200만 달러 이상 후원금 지불한 직업군 필터링
ptab4 = ptab[np.logical_or(ptab['Obama, Barack']>=2000000, ptab['Romney, Mitt']>=2000000)]
ptab4.shape # (12, 2)
ptab4
'''
cand_nm                                 Obama, Barack  Romney, Mitt
contbr_occupation                                                  
ATTORNEY                                  11126932.97    5302578.82
CEO                                        2069784.79     353310.92
CONSULTANT                                 2459812.71    1404576.94
EXECUTIVE                                  1355161.05    2230653.79
HOMEMAKER                                  4243394.30    8037250.86
INFORMATION REQUESTED                      4849801.96           NaN
INFORMATION REQUESTED PER BEST EFFORTS            NaN   11173374.84
LAWYER                                     3159391.87       7705.20
PHYSICIAN                                  3732387.44    1332996.34
PRESIDENT                                  1878009.95    2403439.77
PROFESSOR                                  2163571.08     160362.12
RETIRED                                   25270507.23   11266949.23
'''




