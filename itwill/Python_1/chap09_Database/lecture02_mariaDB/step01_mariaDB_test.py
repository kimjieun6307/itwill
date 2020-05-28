'''
MariaDB 연동 TEST
'''

import pymysql
print(pymysql.version_info) # (1, 3, 12, 'final', 0)

# DB 연동할때 필요한 환경변수
config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

try :
    # 1. db 연동 객체
    conn = pymysql.connect(**config) # 가변인수

    # 2. sql 실행 객체
    cursor =conn.cursor()

    ''' maria DB에 테이블 없으면 만들기
    # 테이블 생성
    sql = """
   create or replace table goods(
   code int primary key,
   name varchar(30) not null,
   su int not null,
   dan int not null 
    )"""
    cursor.execute(sql)
        
    # 레코드 추가
    cursor.execute("insert into goods values(1, '냉장고', 2, 850000)")
    cursor.execute("insert into goods values(2, '세탁기', 3, 550000)")
    cursor.execute("insert into goods values(3, '전자레인지', 2, 350000)")
    cursor.execute("insert into goods values(4, 'HDTV', 3, 1500000)")
    conn.commit()
    '''

    # 3. sql문 실행
    sql = "select * from goods"
    cursor.execute(sql)
    dataset = cursor.fetchall()

    for row in dataset :
        print(row[0], row[1], row[2], row[3])
        '''
        1 냉장고 2 850000
        2 세탁기 3 550000
        3 전자레인지 2 350000
        4 HDTV 3 1500000
        '''

    print('전체 레코드 수 : ', len(dataset)) # 전체 레코드 수 :  4

except Exception as e:
    print("db 연동 error : ", e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()

# 오류가 나면 환경변수 확인 >> 전에 설정한 id와 PW가 맞는지...

