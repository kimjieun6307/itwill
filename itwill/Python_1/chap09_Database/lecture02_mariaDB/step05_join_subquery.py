''' #@@8 : MySQL에서 dept 테이블 생성
<조인 , 서브쿼리>
emp join dept
subquery : emp(사원정보) vs dept(부서정보)
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

    # 1. ANSI inner join
    '''
    sal = int(input('join 급여 : ')) #250
    sql = f""" select e.eno, e.ename, e.sal, d.dname
    from emp e inner join dept d
    on e.dno = d.dno and e.sal >= {sal}
    """

    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row[0], row[1], row[2], row[3])
    
        <결과 값>
        1001 홍길동 300 영업부
        1002 강호동 250 영업부
        1003 유관순 220 영업부
        '''#@@9

    # 2. subquery : 부서명(dept) -> 사원정보(emp)
    '''
    dname = input("부서명 입력 : ") # 영업부
    sql = f"""select eno, ename, hiredate, dno from emp where dno = 
    (select dno from dept where dname like '%{dname}%')
    """
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row[0], row[1], row[2], row[3]) 
        #@@10
    '''

    # 3. subquery2 : 키보드(사원이름) -> 부서정보 출력
    ename = input('사원이름 :')
    sql = f"""select * from dept 
    where dno = (select dno from emp where ename like '%{ename}%')
    """
    cursor.execute(sql)
    data = cursor.fetchall()
    if data :
        for row in data:
            print(row)
            # @@11
    else:
        print('해당 사원 없음')

except Exception as e :
    print("예외 발생 : ", e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()








