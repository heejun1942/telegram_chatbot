from flask import Flask, render_template, request
from decouple import config
import requests

app = Flask(__name__)

token=config("TELEGRAM_BOT_TOKEN")
chat_id=config('CHAT_ID')
url = "https://api.telegram.org/bot"

@app.route('/')
def hello():
    return "hello world!"

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    text = request.args.get('text')
    requests.get(f'{url}{token}/sendmessage?chat_id={chat_id}&text={text}')
    return render_template('send.html')

#telegram 이 나에게 주는 방식이 POST.
@app.route('/{token}', methods=["POST"])
def telegram():
    #나에게 보낸사람의 id입력. > getUpdate에 있음
    # chat_id = request.get_json[][][]
    

    #200은 접속성공을 의미하는 숫자임!
    return "ok", 200   



if __name__ == ("__main__"):
    app.run(debug=True)