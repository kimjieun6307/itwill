'''
group by 집단변수(범주형
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

    # 1. 부서별 or 직책별 그룹
    print('[ 그룹 항목 선택 ]')
    gcol = int(input("1.부서, 2.직책 : "))

    if gcol > 2 or gcol <1 :
        print('그룹 불가')
    else:
        if gcol == 1: # dno 그룹
            sql="""select dno, sum(sal), round(avg(sal),2) from
            emp group by dno
            order by dno"""
        elif gcol ==2 : # job 그룹
            sql = """select job, sum(sal), round(avg(sal),2) from
            emp group by job
            order by job"""
        # sql 실행 검색 결과 출력하기
        cursor.execute(sql)
        data = cursor.fetchall()
        gtitle = "부서" if gcol==1 else "직책"
        print(gtitle, ' 합계', ' 평균')
        for row in data:
            print(row[0],   row[1],   row[2])
            # @@12

except Exception as e :
    print('예외 발생 : ', e)
finally:
    cursor.close()
    conn.close()
