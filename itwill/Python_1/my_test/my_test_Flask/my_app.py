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

    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    return conn, cursor


from flask import Flask, render_template, request
import urllib

url = "https://data.gg.go.kr/portal/mainPage.do"
app = Flask(__name__) # object -> app object

# 함수 장식자
@app.route('/') # 기본 url요청 -> 함수 호출
def index() :
    return render_template('/index.html')

@app.route('/select', methods = ['GET','POST'])
def select():
    if request.method == 'GET':
        menu = int(request.args.get('menu')) # get방식으로 넘어오는 파라미터 받는 방법(post와 차이 있음)
        print('munu : ', menu)

    if menu == 1 : # 화학물질
        return render_template("/chemistry_form.html")

    if menu == 2 : # 자전거 대여소
        return render_template("/bicycles_form.html")

    if menu == 3 : # 자동제세동기(AED)
        return render_template("/AED_form.html")

    if menu == 4 : # 경기데이터드림 사이트 들어가기
        return render_template("/data.html")


@app.route('/chemistry', methods=['GET', 'POST'])
def chemistry() :
    if request.method == 'POST' :
        dong = request.form['dong']
        print('dong = ', dong)

        try:
            conn, cursor = db_conn()
            sql = "select * from chemistry_table"
            cursor.execute(sql)
            data = cursor.fetchall()

            if data:  # 레코드 검색
                cursor.execute(f"select * from chemistry_table where 소재지지번주소 like '%{dong}%'")
                data2 = cursor.fetchall()
                if data2:
                    for row in data2:
                        print(row)
                    print(f'{dong} 레코드 수 : ', len(data2))
                    size = len(data2)
                else:
                    print('해당 동 없음')
                    size = 0

        except Exception as e:
            print('예외 발생', e)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

        return render_template("/chemistry.html", data=data2, size= size)

@app.route('/bicycles', methods=['GET', 'POST'])
def bicycles() :
    if request.method == 'POST' :
        dong = request.form['dong']
        print('dong = ', dong)

        try:
            conn, cursor = db_conn()
            sql = "select * from bicycles_table"
            cursor.execute(sql)
            data = cursor.fetchall()

            if data:  # 레코드 검색
                cursor.execute(f"select * from bicycles_table where 소재지지번주소 like '%{dong}%'")
                data2 = cursor.fetchall()
                if data2:
                    for row in data2:
                        print(row)
                    print(f'{dong} 레코드 수 : ', len(data2))
                    size = len(data2)
                else:
                    print('해당 동 없음')
                    size = 0

        except Exception as e:
            print('예외 발생', e)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

        return render_template("/bicycles.html", data=data2, size= size)

@app.route('/AED', methods=['GET', 'POST'])
def AED() :
    if request.method == 'POST' :
        dong = request.form['dong']
        print('dong = ', dong)

        try:
            conn, cursor = db_conn()
            sql = "select * from AED_table"
            cursor.execute(sql)
            data = cursor.fetchall()

            if data:  # 레코드 검색
                cursor.execute(f"select * from AED_table where 소재지지번주소 like '%{dong}%'")
                data2 = cursor.fetchall()
                if data2:
                    for row in data2:
                        print(row)
                    print(f'{dong} 레코드 수 : ', len(data2))
                    size = len(data2)
                else:
                    print('해당 동 없음')
                    size = 0

        except Exception as e:
            print('예외 발생', e)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

        return render_template("/AED.html", data=data2, size= size)

# 프로그램 시작점
if __name__ == "__main__" :
    app.run(host='192.168.12.10', port=80)