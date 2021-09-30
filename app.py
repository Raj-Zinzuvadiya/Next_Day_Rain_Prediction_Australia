from flask import Flask,render_template,request
import numpy as np
import pandas as pd 
import pickle
import jsonify
import requests



app = Flask(__name__)

model = pickle.load(open("model.pkl","rb"))



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods= ["POST"])
def predict():
    if request.method=='POST':
        mintemp  = float(request.form["mintemp"])
        maxtemp  = float(request.form["maxtemp"])
        RainFall  = float(request.form["RainFall"])
        WindGustDir  = request.form["WindGustDir"]
        WindGustSpeed  = float(request.form["WindGustSpeed"])
        WindDir9am  = request.form["WindDir9am"]
        WindDir3pm  = request.form["WindDir3pm"]
        WindSpeed9am  = float(request.form["WindSpeed9am"])
        WindSpeed3pm  = float(request.form["WindSpeed3pm"])
        Humidity9am  = float(request.form["Humidity9am"])
        Humidity3pm  = float(request.form["Humidity3pm"])
        Humidity9am  = float(request.form["Humidity9am"])
        Pressure9am  = float(request.form["Pressure9am"])
        Pressure3pm  = float(request.form["Pressure3pm"])
        Cloud9am  = float(request.form["Cloud9am"])
        Cloud3pm  = float(request.form["Cloud3pm"])
        Temp9am  = float(request.form["Temp9am"])
        Temp3pm  = float(request.form["Temp3pm"])
        RainToday  = request.form["RainToday"]

        windkey = {'W': 13,
                    'WNW': 14,
                    'WSW': 15,
                    'NE': 4,
                    'NNW': 6,
                    'N': 3,
                    'NNE': 5,
                    'SW': 12,
                    'ENE': 1,
                    'SSE': 10,
                    'S': 8,
                    'NW': 7,
                    'SE': 9,
                    'ESE': 2,
                    'E': 0,
                    'SSW': 11}
        




        WindGustDir = windkey.get(WindGustDir)
        WindDir9am = windkey.get(WindDir9am)
        WindDir3pm = windkey.get(WindDir3pm)
        

        
        if RainToday=='Yes':
            RainToday=1
        else:
            RainToday=0
        
        data = np.array([[mintemp,maxtemp,RainFall,WindGustDir,WindGustSpeed,WindDir9am
        , WindDir3pm,WindSpeed9am,WindSpeed3pm, Humidity9am,Humidity3pm,Pressure9am,Pressure3pm,
        Cloud9am,Cloud3pm, Temp9am,Temp3pm,RainToday]])

        predict_text =  model.predict(data)
        if predict_text==1:
            predict_text ="Yes"
        else:
            predict_text ="No"

        return render_template("index.html",predict_text="Yes")
        
    else:
        return render_template("index.html")



if __name__ == "__main__":
    print(pickle.format_version)
    
    app.run()
