'''
table 전체 조회 -> 생성 및 조회
 1. 없는 경우 : table 생성
 2. 있는 경우 : table 조회
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

    # 1. 전체 table 조회
    cursor.execute("show tables")
    tables = cursor.fetchall()

    # table 유무 검색
    sw = False
    if tables : # 검색 테이블이 존재하는 경우
        for table in tables :
            #print(table) # ('emp_table',)
            #@@6
            #print(table[0]) # emp_table
            if table[0] == 'emp' :
                sw=True

    if sw == False:
        print("emp 테이블 없음")
        # @@7

        sql = """create or replace table emp(
        eno int auto_increment primary key,
        ename varchar(20) not null,
        hiredate date not null,
        sal int,
        bonus int default 0,
        job varchar(20) not null,
        dno int
        )"""
        cursor.execute(sql)

        sql2 = "alter table emp auto_increment = 1001" # 초기값
        cursor.execute(sql2)

        sql3 = """insert into emp(ename, hiredate, sal, bonus, job, dno)
        values('홍길동', '2010-10-20', 300, 35, '관리자', 10)"""
        cursor.execute(sql3)
        sql3 = """insert into emp(ename, hiredate, sal, job, dno)
                values('강호동', '2015-09-20', 250, '사원', 20)"""
        cursor.execute(sql3)
        sql3 = """insert into emp(ename, hiredate, sal, job, dno)
                values('유관순', '2020-10-20', 220, '사원', 10)"""
        cursor.execute(sql3)
        conn.commit()
        print('emp 테이블 작성 완료~~')

    else:
        print("emp 테이블 있음")

        # 전체 조회
        sql = "select * from emp"
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data  :
            print(row)
        print('전체 레코드 수 : ', len(data))
        '''
        # 사원 조회 : 키보드(이름) -> 사번, 이름, 부서, 칼럼 출력
        ename = input('사원 이름 :')
        sql = f"select eno, ename, dno from emp where ename like '%{ename}%'"
        cursor.execute(sql)
        data = cursor.fetchall()
        if data :
            for row in data:
                print(row)
        else:
            print('해당 사원 없음')

        # 사원 수정 : 키보드(사번, 급여, 보너스) -> 급여, 보너스 수정
        eno = int(input("사번 :"))
        sal = int(input('급여 수정: '))
        bonus = int(input('보너스 수정:'))
        sql =  f"update emp set sal={sal}, bonus={bonus} where eno={eno}"
        cursor.execute(sql)
        conn.commit()

        cursor.execute(f"select * from emp where eno={eno}")
        row = cursor.fetchone()
        print(row)

        # 레코드 삭제 : 키보드(사번) -> 검색(유무) -> 레코드 삭제
        eno = int(input('삭제할 사번 : '))
        sql = f"select * from emp where eno = {eno}"
        cursor.execute(sql)
        data = cursor.fetchone()
        if data :
            cursor.execute(f"delete from emp where eno = {eno}")
            conn.commit()
            print(str(eno) +'레코드 삭제됨')
        else:
            print('해당 사번이 없습니다.')
        '''

except Exception as e :
    print("예외 발생 : ", e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
