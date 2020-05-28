'''
문) emp 테이블을 대상으로 사원명을 조회하는 application 을 구현하시오.
  조건1> index 페이지에서 사원명을 입력받아서 post 방식 전송
  조건2> 해당 사원이 있으면 result 페이지에 사번, 이름, 직책, 부서번호 칼럼 출력
  조건3> 해당 사원이 없으면 result 페이지에 '해당 사원 없음' 이라고 출력
'''

from flask import Flask, render_template, request
# app생성, 템플릿(html) 호출, 파라미터 받을수 있는 method

app = Flask(__name__) # object -> app object

# 함수 장식자
@app.route('/') # 기본 url요청 -> 함수 호출
def index() :
    return render_template('/exam01/index.html')

@app.route('/search', methods=['GET', 'POST'])
def search() :
    if request.method == 'POST' :
        name = request.form['name']
        print('name = ', name)

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
            # 레코드 조회
            sql = "select * from emp"
            cursor.execute(sql)
            data = cursor.fetchall()
            if data:  # 레코드 검색
                cursor.execute(f"select * from emp where ename like '%{name}%'")
                data2 = cursor.fetchall()
                if data2:
                    for row in data2:
                        eno = row[0]
                        ename = row[1]
                        job = row[5]
                        dno = row[6]
                        print(eno, ename, job, dno)
                    print(f'{name} 레코드 수 : ', len(data2))
                    size = len(data2)
                else:
                    print('해당 사원 없음')
                    size = 0

        except Exception as e:
            print('예외 발생', e)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
        return render_template("/exam01/result.html", name = name, data = data2, eno=eno, ename = ename, job= job, dno= dno, size = size)


# 프로그램 시작점
if __name__ == "__main__" :
    app.run() # application 실행