import requests
import os
from flask import Flask
import dotenv

dotenv.load_dotenv()
IMDB_API_KEY = os.environ['IMDB_API_KEY']
app = Flask(__name__)

@app.route('/')
def hello_world():
    url = "https://imdb-api.com/en/API/Title/{}/tt1832382".format(IMDB_API_KEY)
    payload = {}
    headers= {}


    response = requests.request("GET", url, headers=headers, data = payload)

    return response.text.encode('utf8')
