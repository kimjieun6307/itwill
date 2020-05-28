'''
get vs post
 - 파라미터 전송 방식
 - get : url에 노출(소량)
 - post : body에 포함되어 전송(대량)

< 작업 순서 >
 1. index 페이지 : 메뉴 선택할 수 있는 화면 구현(radio or select) -> get 방식
 2. flask sever에서 파라미터 받기(메뉴 번호)
 3. 각 메뉴 번호에 따라서 각 페이지로 이동
'''

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

# db 조회 함수
def select_func() :
    sql = "select * from goods"
    conn, cursor = db_conn() # db 연동 객체
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row[0], row[1], row[2], row[3])
    print('전체 레코드 수 : ', len(data))
    cursor.close(), conn.close()
    return data



from flask import Flask, render_template, request

app = Flask(__name__)

# 함수 장식자
@app.route('/')
def index() :
    return render_template('/app04/index.html')

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

# 프로그램 시작점
if __name__ == "__main__" :
    app.run() # application 실행














