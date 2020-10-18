import requests
from functions import *
from flask import Flask, render_template, flash, request
app = Flask(__name__)

@app.route('/' , methods = ['GET' , 'POST'])
def home():
    deg = ""
    con_deg = ""

    if(request.method == 'POST'):
        num = request.form['degree']
        deg = ("Entered Degree: " + str(num))
        choice = request.form.get('degree_type')
        if(choice == 'F'):
            converted_num = ConvertCToF(float(num))
        elif(choice == 'C'):
            converted_num = ConvertFToC(float(num))
        con_deg = ("Converted Degree to " + choice + " " + str(converted_num))

    return render_template('index.html',degree = deg, converted_degree = con_deg)


if __name__ == "__main__":
    app.run(debug=True)
