from flask import Flask, render_template, request
from decouple import config 
import requests


token = config("TELEGRAM_BOT_TOKEN")
url = "https://api.telegram.org/bot"


#ngrok 이용
ngrok_url = "https://cb123d25.ngrok.io"
data = requests.get(f'{url}{token}/setwebhook?url={ngrok_url}/{token}')


#python anywhere 이용
#paw_url = "https://heejun1942.pythonanywhere.com/"
# data = requests.get(f'{url}{token}/setwebhook?url={paw_url}{token}')

print(data.text)



#test
