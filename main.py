from bs4 import BeautifulSoup
import requests
from flask import Flask
import json

perguntas = {"perguntas": []}

app = Flask(__name__)

@app.route('/')
def hello():

    html =requests.get("https://www.respostas.com.br/perguntas-biblicas-faceis/").content
    res = BeautifulSoup(html, 'html.parser')
    respostas = res.find("div", class_="article--body")
    return respostas.prettify()

if __name__ == "__main__":
    app.run()