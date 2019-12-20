from decouple import config 
import requests

token = config("TELEGRAM_BOT_TOKEN")
url = "https://api.telegram.org/bot"
ngrok_url = "https://2ccfe768.ngrok.io"

#setwebhook을 설정
data = requests.get(f'{url}{token}/setwebhook?url={ngrok_url}/{token}')
print(data.text)

