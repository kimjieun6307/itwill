import flask
from flask import Flask # class
print(flask.__version__) # 1.1.2

# flask application
app = Flask(__name__) # class(생성자) -> object(application)

# 함수 장식자 : 사용자 요청 url -> 함수 호출
@app.route('/') # 기본url : http://localhost/ ==> http://127.0.0.1:5000/
def hello():
    return "hello flack~~" # 반환값 - 간단한 텍스트 반환

# 프로그램 시작점
if __name__ == "__main__" :
    app.run() # application 실행


