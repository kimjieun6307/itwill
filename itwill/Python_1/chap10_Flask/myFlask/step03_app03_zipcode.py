'''
<작업순서>
1. index 페이지 작성 -> 동 입력
2. flask server(app.py파일)에서 동(파라미터) 받기
3. db연동 -> 주소 조회
4. 조회 결과 -> result 페이지 출력
'''

from flask import Flask, render_template, request
# app생성, 템플릿(html) 호출, 파라미터 받을수 있는 method

app = Flask(__name__) # object -> app object

# 함수 장식자
@app.route('/') # 기본 url요청 -> 함수 호출
def index() :
    return render_template('/app03/index.html') # <form method="post" action="/search">

@app.route('/search', methods=['GET', 'POST'])
def search() :
    if request.method == 'POST' :
        dong = request.form['dong'] # index.html에서 name으로 지정된 변수명 'dong' / 사용자가 지정한 동을 파라미터 받는것.
        print('dong = ', dong)

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
            sql = "select * from zipcode_tab"
            cursor.execute(sql)
            data = cursor.fetchall()
            if data:  # 레코드 검색
                '''
                for row in data :
                    print("[%s]   %s   %s   %s   %s"%row)
                print('전체 레코드 수 : ', len(data))
                '''
                # 동(dong)으로 검색
                #dong = input('검색 할 동 입력 : ')
                cursor.execute(f"select * from zipcode_tab where dong like '%{dong}%'")
                data2 = cursor.fetchall()
                if data2:
                    for row in data2:
                        print("[%s]   %s   %s   %s   %s" % row)
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

        return render_template("/app03/result.html", dong= dong, data=data2, size= size)


# 프로그램 시작점
if __name__ == "__main__" :
    app.run() # application 실행
    # app.run(host='본인 아이피 addr', port=80) # host, port 변경



