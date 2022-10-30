from flask import Flask,render_template,request,jsonify

from models.utils import diabetes
import numpy as np
import config

app=Flask(__name__)
@app.route('/')
def sms():
    return render_template("home.html")

@app.route('/Endpoint',methods=["GET"])
def sachin():
    Input=request.args.get
    Glucose=eval(Input('Glucose'))
    BloodPressure=eval(Input('BloodPressure'))
    SkinThickness=eval(Input('SkinThickness'))
    Insulin=eval(Input('Insulin'))
    BMI=eval(Input('BMI'))
    DiabetesPedigreeFunction=eval(Input('DiabetesPedigreeFunction'))
    Age=eval(Input('Age'))

    print("Glucose,BloodPressure,skin,Insulin,bmi,diapf,age\n",Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    like=diabetes(Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    dia=like.prediction()
    
    return render_template("home.html",predict=dia)
if __name__=="__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER,debug=False)
