from flask import Flask              # 플라스크 모듈 호출

app = Flask(__name__)               # 플라스크 앱 생성        


def a() :
    return "kkk"


@app.route('/')                     # 기본('/') 웹주소로 요청이 오면                     
def a():                        #hello 함수 실행
    return 'Hello world1!!!!!'



@app.route('/abcd')
def b():                        #hello 함수 실행
    return 'Hello world2!!!!!'

if __name__ == '__main__':          # 현재 파일 실행시 개발용 웹서버 구동
    app.run(debug=True, port=99, host='172.30.1.54') 