import requests
from flask import Flask, render_template, flash, request, redirect
app = Flask(__name__)


@app.route('/' , methods = ['GET' , 'POST'])
def home():
    if(request.method == 'POST'):
        city = request.form.get('city')
        print(city + " test")
    return render_template('index.html')

@app.route('/result' , methods = ['GET' , 'POST'])
def result():
    user_city = request.args.get('city',None)

    return render_template('result.html' , city = user_city)


if __name__ == "__main__":
    app.run(debug=True)
