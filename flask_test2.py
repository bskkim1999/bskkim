from flask import Flask              # 플라스크 모듈 호출
import RPi.GPIO as GPIO

app = Flask(__name__)               # 플라스크 앱 생성        

ledpin1 =21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledpin1, GPIO.OUT)


@app.route('/')                     # 기본('/') 웹주소로 요청이 오면                     
def hello():                        #hello 함수 실행
    return 'Hello LED !!!!!'


@app.route('/on')
def on():                        #hello 함수 실행
    GPIO.output(ledpin1, 1)

@app.route('/off')
def off():                        #hello 함수 실행
    GPIO.output(ledpin1, 0)

if __name__ == '__main__':          # 현재 파일 실행시 개발용 웹서버 구동
    app.run(debug=True, port=99, host='192.168.0.32') 