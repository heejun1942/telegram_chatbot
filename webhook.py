from flask import Flask, render_template, request
from decouple import config 
import requests
from bs4 import BeautifulSoup


token = config("TELEGRAM_BOT_TOKEN")
url = "https://api.telegram.org/bot"
paw_url = "https://heejun1942.pythonanywhere.com/"

#setwebhook을 설정
data = requests.get(f'{url}{token}/setwebhook?url={paw_url}{token}')
print(data.text)

