# db 연결 객체 생성 함수 (필요할때마다 호출해서 사용하기 위해)
def db_conn():
    import pymysql
    config = {
        'host': '127.0.0.1',
        'user': 'scott',
        'password': 'tiger',
        'database': 'work',
        'port': 3306,
        'charset': 'utf8',
        'use_unicode': True}

    # db 연결 객체 생성
    conn = pymysql.connect(**config)
    # SQL 실행 객체 생성
    cursor = conn.cursor()
    return conn, cursor


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index() :
    return render_template('/app05/main.html')

@app.route('/docForm')
def docForm() :
    return render_template("/app05/docForm.html")

@app.route('/docPro', methods=['GET','POST'])
def docPro():
    if request.method == 'POST' :
        doc_id = int(request.form['id'])
        major = request.form['major']

        conn, cursor = db_conn()
        sql = f""" select * from doctors where doc_id = {doc_id}
        and major_treat = '{major}'"""  # major_treat like '%{major}%'
        cursor.execute(sql)
        row = cursor.fetchone()

        if row : # login 성공
            # print('로그인 성공') : 601, 내과
            sql = f"""select d.doc_id, t.pat_id, t.treat_contents, t.tread_date
            from doctors d inner join treatments t
            on d.doc_id = t.doc_id and d.doc_id = {doc_id}"""
            cursor.execute(sql)
            data = cursor.fetchall()
            if data :
                for row in data:
                    print(row)
                size = len(data)
            else :
                size = 0
            return render_template("/app05/docPro.html", dataset = data, size= size)

        else: # login 실패
            # print('로그인 실패')
            return render_template("/app05/error.html", info = 'id 또는 진료과목 확인')

@app.route('/nurseForm')
def nurseForm() :
    return render_template("/app05/nurseForm.html")

@app.route('/nursePro', methods =['GET','POST'])
def nursePro() :
    # 파라미터(id) 받기 -> id 유무 파악 -> 있으면 간호사 join 환자 / 없으면 error.html
    if request.method == 'POST':
        nur_id = int(request.form['id'])

        conn, cursor = db_conn()
        sql = f"select * from nurses where nur_id = {nur_id}"
        cursor.execute(sql)
        row = cursor.fetchone()
        if row:  # login 성공
            sql = f"""select n.nur_id, p.doc_id, p.pat_name, p.pat_phone
            from nurses n inner join patients p
            on n.nur_id = p.nur_id and n.nur_id = {nur_id}"""
            cursor.execute(sql)
            data = cursor.fetchall()
            if data:
                for row in data:
                    print(row)
                size = len(data)
            else:
                size = 0
            return render_template("/app05/nursePro.html", dataset=data, size=size)

        else:  # login 실패
            # print('로그인 실패')
            return render_template("/app05/error.html", info='id 확인해 주세요.')





'''
@app.route('/select', methods = ['GET','POST']) # http://127.0.0.1:5000/select?menu=1
def select():
    if request.method == 'GET':
        menu = int(request.args.get('menu')) # get방식으로 넘어오는 파라미터 받는 방법(post와 차이 있음)
        # name = request.args.get('name')
        print('munu : ', menu)

    if menu == 1 : # 전체 레코드 조회
        data = select_func()
        size = len(data)
        return render_template("/app04/select.html", data=data, size=size)

    if menu ==2 : # 레코드 추가
        return render_template("/app04/insert_form.html")

    if menu ==3 : # 레코드 수정
        return render_template("/app04/update_form.html")

    # delete_form(code) -> get -> flask server(파라미터) -> delete
    if menu ==4 : # 레코드 삭제
        return render_template("/app04/delete_form.html")

@app.route("/insert", methods=['GET','POST'])
def insert() :
    try :
        if request.method == 'POST':
            code = int(request.form['code'])
            name = request.form['name']
            su = int(request.form['su'])
            dan = int(request.form['dan'])

            # 레코드 삽입
            conn, cursor = db_conn()
            sql = f"insert into goods values({code}, '{name}', {su}, {dan})"
            cursor.execute(sql)
            conn.commit()
            cursor.close(); conn.close()

            # 레코드 조회
            data = select_func()
            size = len(data)
            return render_template("/app04/select.html", data=data, size=size)
    except Exception as e :
        return render_template("/app04/error.html", error_info = e)

@app.route("/update", methods=['GET','POST'])
def update() :
    try :
        if request.method == 'POST':
            code = int(request.form['code'])
            su = int(request.form['su'])
            dan = int(request.form['dan'])

            # 레코드 수정
            conn, cursor = db_conn()
            sql = f"update goods set su={su}, dan={dan} where code={code}"
            cursor.execute(sql)
            conn.commit()
            cursor.close(); conn.close()

            # 레코드 조회
            data = select_func()
            size = len(data)
            return render_template("/app04/select.html", data=data, size=size)
    except Exception as e :
        return render_template("/app04/error.html", error_info=e)

@app.route('/delete', methods=['GET','POST'])
def delete():
    try :
        if request.method == 'GET':
            code = int(request.args.get('code'))

            # 레코드 수정
            conn, cursor = db_conn()
            sql = f"delete from goods where code={code}"
            cursor.execute(sql)
            conn.commit()
            cursor.close(); conn.close()

            # 레코드 조회
            data = select_func()
            size = len(data)
            return render_template("/app04/select.html", data=data, size=size)
    except Exception as e:
        return render_template("/app04/error.html", error_info=e)
'''

# 프로그램 시작점
if __name__ == "__main__" :
    app.run() # application 실행

