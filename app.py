from flask import Flask, render_template, request
from decouple import config
from bs4 import BeautifulSoup
import requests
import random

app = Flask(__name__)

token=config("TELEGRAM_BOT_TOKEN")
chat_id=config('CHAT_ID')
url = "https://api.telegram.org/bot"

@app.route('/')
def hello():
    return "hello world!"

#write.html에서 form태그로 데이터를 받아 /send로 넘김
@app.route('/write')
def write():
    return render_template('write.html')

#write.html에서 form태그로 데이터받음
@app.route('/send')
def send():
    text = request.args.get('text')
    # /sendmessage를 통해 내 텔레그램으로 메시지를 보냄
    requests.get(f'{url}{token}/sendmessage?chat_id={chat_id}&text={text}')
    return render_template('send.html')

#telegram에서 정보를 받는 코드
#telegram 이 나에게 주는 방식이 POST.
@app.route(f'/{token}', methods=["POST"])
def telegram():
    # 챗봇에서 내가쓴 데이터 읽어오기
    re_data=request.get_json()

    # json데이터에서 원하는 정보뽑기
    re_id= re_data['message']['chat']['id']
    text=re_data['message']['text']

    if text=="안녕":
        return_text= "안녕하세요."
    elif text =="로또":
        numbers = range(1,46)
        return_text= sorted(random.sample(numbers, 6))
    elif text=="영화":
        key="a42fdafda11bba9cf32dcbf11326b918"
        day="20191219"
        url= f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={key}&targetDt={day}"
        req = requests.get(url).json()
        movie=req["boxOfficeResult"]["dailyBoxOfficeList"][0]["movieNm"]
        return_text= f"박스오피스 1위는 {movie}입니다."
    else:
        return_text="지금 지원하는 채팅은 '안녕'입니다."

    # 챗봇에게 다시보내기
    requests.get(f'{url}{token}/sendmessage?chat_id={re_id}&text={return_text}')

    #200은 접속성공을 의미하는 숫자임!
    return "ok", 200   


if __name__ == ("__main__"):
    app.run(debug=True)