import requests
import json
from flask import Flask, render_template, flash, request, redirect
from keys import *
from functions import *
app = Flask(__name__)


@app.route('/' , methods = ['GET' , 'POST'])
def home():
    if(request.method == 'POST'):
        city = request.form.get('city')

    return render_template('index.html')

@app.route('/result' , methods = ['GET' , 'POST'])
def result():
    user_city = request.args.get('city',None)
    
    weather = getWeather(user_city)


    return render_template('result.html' , city = user_city, weather = weather)


if __name__ == "__main__":
    app.run(debug=True)
