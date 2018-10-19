from flask import Flask, render_template
import mysql.connector as mariadb
import requests
from envparse import env
from nytdatabase import DataBase
from datetime import datetime


env.read_envfile()
nytkey = env.str('nytapikey')

ny_database=DataBase()


app = Flask(__name__)

@app.route('/')
def home():

    payload = {'api-key': nytkey}

    r = requests.get('https://api.nytimes.com/svc/topstories/v2/home.json', params=payload)

    render_data = []
    data = r.json()["results"]
    for i, value in enumerate(data):
        if i<5:
            print(data[i])
            d = {}
            d['title'] = data[i]['title']
            d['byline'] = data[i]['byline']
            d['url'] = data[i]['url']
            d['published_date'] = data[i]['published_date']

            render_data.append(d)

    #capture data from the api to the database
    ny_database.insert_data(render_data,datetime.now())
    #print(render_data)
    return render_template('home.html', render_data= render_data)


@app.route('/about/')
def about():
	return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=True)