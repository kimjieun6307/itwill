'''
sqlite 3
 - 내장형 DBMS : 기기 내부에서만 사용가능
 - 외부 접근 허용 안됨.
'''

import sqlite3

print(sqlite3.version_info) # (2, 6, 0)
print(sqlite3.sqlite_version_info) # (3, 31, 1)

# 파일 입출력 하거나 DB 입출력 할때 예외처리 구문이용

try :
    # 1. database 생성 & db 연동 객체
    conn = sqlite3.connect('../data/sqlite.db') # sqlite.db
    # sql문 실행 객체
    cursor = conn.cursor()

    # 2.  table 생성
    '''
    sql = """ 
    create table if not exists test_tab(
    name text(10),
    phone text(10), 
    addr text(50) )"""
    cursor.execute(sql) # table 생성
    '''

    # 3. 레코드 추가
    '''
    cursor.execute("insert into test_tab values('홍길동', '010-111-1111', '서울시')")
    cursor.execute("insert into test_tab values('이순신', '010-111-1111', '해남시')")
    cursor.execute("insert into test_tab values('유관순', '010-111-1111', '충남시')")
    conn.commit # DB반영
    '''

    # 4. 레코드 조회
    cursor.execute("select*from test_tab")
    dataset = cursor.fetchall()# 객체 레코드  -> 레코드 가져오기
    for row in dataset :
        print(row) # tuple 타입
        '''
        ('홍길동', '010-111-1111', '서울시')
        ('이순신', '010-111-1111', '해남시')
        ('유관순', '010-111-1111', '충남시')
        '''
    print('이름\t\t전화번호\t\t주소')
    for row in dataset :
        print(row[0]+'\t'+row[1]+'\t'+row[2])
        '''
        이름		전화번호		주소
        홍길동	010-111-1111	서울시
        이순신	010-111-1111	해남시
        유관순	010-111-1111	충남시
        '''

except Exception as e :
    print("db 연동 오류 : ", e)
    conn.rollback() # 이전 쿼리 실행 취소
finally:
    cursor.close()
    conn.close()







