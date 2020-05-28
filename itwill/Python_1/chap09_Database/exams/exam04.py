'''
문제4) emp.csv 파일을 읽어서 다음과 같이 db 테이블에 저장하시오.
 <조건1> 테이블명 : emp_table
 <조건2> 사원 이름으로 레코드 조회(sql문 작성)
 
 <작업순서>
 1. table 생성 : emp_table(no(int), name(varchar(20)), pay(int))
 2. python code : 레코드 추가 
 3. python code : 레코드 조회(사원이름)  
'''

import pandas as pd 


# 칼럼 단위 읽기
'''
emp = pd.read_csv("../data/emp.csv", encoding='utf-8')
print(emp)
# No Name  Pay
no = emp.No
name = emp.Name
pay = emp.Pay
print(no, name, pay)
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
    ''' # table 생성
    sql = """create table emp_table(
    no int, 
    name varchar(20), 
    pay int
    )"""
    cursor.execute(sql)
    print('table 작성 완료!!')
    '''
    ''' # 레코드 추가
    for i in range(len(no)):
        sql = f"insert into emp_table values({no[i]}, '{name[i]}', {pay[i]})"
        cursor.execute(sql)
        conn.commit()
    print('레코드 추가 완료!!')
    '''
    '''
    # 전체 레코드 조회
    sql = "select * from emp_table"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)
         (101, '홍길동', 150)
         (102, '이순신', 450)
         (103, '강감찬', 500)
         (104, '유관순', 350)
         (105, '김유신', 400)
    '''
    # 사원 이름으로 레코드 조회(sql문 작성)
    name = input('사원 이름 : ')
    sql2 = f"select * from emp_table where name like '%{name}%'"
    cursor.execute(sql2)
    data2 = cursor.fetchall()
    if data2 :
        for row in data2:
            print(row)
    else :
        print('해당 사원이 없습니다.')

except Exception as e :
    print('예외 발생 : ', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()

    
    
    











