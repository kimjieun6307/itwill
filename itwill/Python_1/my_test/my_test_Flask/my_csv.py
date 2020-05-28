import pandas as pd #as 별칭

import os
# print(os.getcwd())

# 1. csv file read
# chemistry_data = pd.read_csv("../my_data/chemistry.csv", encoding='ms949')
# print(chemistry_data.info())
'''
a1=chemistry_data['시군명']
a2=chemistry_data['연번']
a3=chemistry_data['사업장명']
a4=chemistry_data['소재지도로명주소']
a5=chemistry_data['소재지지번주소']
a6=chemistry_data['취급사고대비물질명']
a7=chemistry_data['연간취급량하한선(톤)']
a8=chemistry_data['연간취급량상한선(톤)']
a9=chemistry_data['주민대피시설명칭']
a10=chemistry_data['주민대피시설주소']
a11=chemistry_data['사업장과주민대피시설간이격거리(m)']
a12=chemistry_data['위도']
a13=chemistry_data['경도']
'''
# print(chemistry_data.head())
# print(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13)

#bicycles_data = pd.read_csv("../my_data/bicycles.csv", encoding='ms949')
#print(bicycles_data.info())
'''
b1=bicycles_data['자전거대여소명'] 
b2=bicycles_data['자전거대여소구분'] 
b3=bicycles_data['소재지도로명주소'] 
b4=bicycles_data['소재지지번주소'] 
b5=bicycles_data['위도']
b6=bicycles_data['경도']
b7=bicycles_data['운영시작시각']
b8=bicycles_data['운영종료시각'] 
b9=bicycles_data['휴무일']
b10=bicycles_data['요금구분']
b11=bicycles_data['자전거이용요금']
b12=bicycles_data['자전거보유대수']
b13=bicycles_data['거치대수']
b14=bicycles_data['공기주입기비치여부'] 
b15=bicycles_data['공기주입기유형']
b16=bicycles_data['수리대설치여부']
b17=bicycles_data['관리기관전화번호'] 
b18=bicycles_data['관리기관명']
b19=bicycles_data['데이터기준일자']
'''

AED_data = pd.read_csv("../my_data/AED.csv", encoding='ms949')
print(AED_data.info())

'''
 0   시군명          7538 non-null   object 
 1   설치기관명(설치장소)  7538 non-null   object 
 2   전화번호         7294 non-null   object 
 3   소재지우편번호      6898 non-null   float64
 4   소재지도로명주소     7216 non-null   object 
 5   소재지지번주소      7538 non-null   object 
 6   WGS84위도      6887 non-null   float64
 7   WGS84경도      6887 non-null   float64
'''
'''
import pymysql

config = {
    'host': '127.0.0.1',
    'user': 'scott',
    'password': 'tiger',
    'database': 'work',
    'port': 3306,
    'charset': 'utf8',
    'use_unicode': True}

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    sql = """create table AED_table(
     시군명 varchar(20), 
     설치기관명 varchar(30), 
     전화번호 varchar(20), 
     소재지우편번호 varchar(20),
     소재지도로명주소 varchar(50), 
     소재지지번주소 varchar(50), 
     WGS84위도 float,
     WGS84경도 float
        )"""
    cursor.execute(sql)
    print('table 작성 완료!!')

except Exception as e :
    print("예외 발생 : ", e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
'''

'''
import pymysql

config = {
    'host': '127.0.0.1',
    'user': 'scott',
    'password': 'tiger',
    'database': 'work',
    'port': 3306,
    'charset': 'utf8',
    'use_unicode': True}

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    sql = """create table bicycles_table(
    자전거대여소명 varchar(30),
    자전거대여소구분 varchar(30),
    소재지도로명주소 varchar(50),
    소재지지번주소 varchar(50),
    위도 float,
    경도 float,
    운영시작시각 varchar(10), 
    운영종료시각 varchar(10),
    휴무일 varchar(20),
    요금구분 varchar(20),
    자전거이용요금 varchar(30),
    자전거보유대수 int,
    거치대수 float,
    공기주입기비치여부 varchar(30), 
    공기주입기유형 varchar(30),
    수리대설치여부 varchar(30),
    관리기관전화번호 varchar(20),
    관리기관명 varchar(30),
    데이터기준일자 varchar(30)
        )"""
    cursor.execute(sql)
    print('table 작성 완료!!')

except Exception as e :
    print("예외 발생 : ", e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
'''

'''
import pymysql
config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

try :
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    
    sql = """create table chemistry_table(
        시군명 varchar(50),
        연번 varchar(50), 
        사업장명 varchar(50), 
        소재지도로명주소 varchar(50) , 
        소재지지번주소 varchar(50), 
        취급사고대비물질명 varchar(50), 
        연간취급량하한선 bigint default 0, 
        연간취급량상한선 bigint default 0,
        주민대피시설명칭 varchar(30) default 0, 
        주민대피시설주소 varchar(50) default 0,
        사업장과주민대피시설간이격거리 float default 0.0,
        위도 float default 0.0,
        경도 float default 0.0
        )"""
    cursor.execute(sql)
    print('table 작성 완료!!')
    

    #레코드 추가 에러=>예외 발생 :  (1054, "Unknown column 'nan' in 'field list'")
    for i in range(len(a1)):
        sql = f"""insert into chemistry_table values(
        '{a1[i]}', '{a2[i]}', '{a3[i]}', '{a4[i]}', '{a5[i]}', '{a6[i]}',
        {a7[i]}, {a8[i]}, '{a9[i]}', '{a10[i]}', {a11[i]}, {a12[i]}, {a13[i]})"""
        cursor.execute(sql)
        conn.commit()
    print('레코드 추가 완료!!')

except Exception as e:
    print('예외 발생 : ', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
'''
