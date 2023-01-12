from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
model1 = pickle.load(open('model1.pkl','rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        ssp = float(request.form['ssp'])
        hsp = float(request.form['hsp'])
        etest_p = float(request.form['etest_p'])
        degree_p = float(request.form['degree_p'])
        mbap = float(request.form['mbap'])
    
        Gender=request.form['Gender']
        if(Gender=='Male'):
                Gender=1        
        else:
                Gender=0
            
        workexperience=request.form['workexperience']
        if(workexperience=='Yes'):
            workexperience=1
        else:
            workexperience=0	

        mbat=request.form['mbat']
        if(mbat=='Mkt&HR'):
            mbat=1
        else:
            mbat=0

        ssb=request.form['ssb']
        if(ssb=='Central'):
            ssb=1
        else:
            ssb=0	

        hsb=request.form['hsb']
        if(hsb=='Central'):
            hsb=1
        else:
            hsb=0

        hss=request.form['hss']
        if(hss=='Science'):
            hss=1
        else:
            workexperience=0	
            
        dgreet=request.form['dgreet']
        if(dgreet=='Sci&Tech'):
            dgreet=1
        else:
            dgreet=0

        prediction=model.predict([[Gender,ssp,ssb,hsp,hsb,hss,degree_p,dgreet,workexperience,etest_p,mbat,mbap]])
        output=round(prediction[0],2)
        if(output==0.0):
         output="Person is not placed"
         return render_template('index.html',prediction_text="Sorry you are not placed")
        else:
         output="Person is Placed"
         prediction1=model1.predict([[Gender,ssp,ssb,hsp,hsb,hss,degree_p,dgreet,workexperience,etest_p,mbat,mbap]])
         output1=round(prediction1[0],2)
         return render_template('index.html',prediction_text="You are placed with salary of {}".format(output1))
   
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

