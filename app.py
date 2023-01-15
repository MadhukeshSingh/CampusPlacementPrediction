import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model_final.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['post'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    
    cols =['Gender','ssp', 'ssb', 'hsp', 'hsb', 'degreep', 'workexperience', 'etest_p', 'mbat', 'mbap', 'hss','dgreet']
    cols2=['gender', 'ssc_p', 'ssc_b', 'hsc_p', 'hsc_b', 'degree_p', 'workex', 'etest_p', 'specialisation', 'mba_p', 'hsc_s_Arts', 'hsc_s_Commerce', 'hsc_s_Science', 'degree_t_Comm&Mgmt', 'degree_t_Others', 'degree_t_Sci&Tech']

    features=[]
    for i in cols:
        features.append(str(request.form.get(i)))

    print(features)


    if(features[0]=="Male"):
        features[0]=1.0
    else:
        features[0]=0.0

    if(features[2]=="Other"):
        features[2]=0.0
    else:
        features[2]=1.0

    if(features[4]=="Central"):
        features[4]=1.0
    else:
        features[4]=0.0

    if(features[6]=="Yes"):
        features[6]=1.0
    else:
        features[6]=0

    if(features[8]=="Mkt&HR"):
        features[8]=0.0
    else:
        features[8]=1.0

    if(features[10]=="Arts"):
        features.append('1')
        features.append('0')
        features.append('0')    
    elif(features[10]=="Commerce"):
        features.append('0')
        features.append('1')
        features.append('0')
            
    elif(features[10]=="Science"):
        features.append('0')
        features.append('0')
        features.append('1')
        
    if(features[11]=="Comm&Mgmt"):
        features.append('1')
        features.append('0')
        features.append('0')    
    elif(features[11]=="Others"):
        features.append('0')
        features.append('1')
        features.append('0')
            
    elif(features[11]=="Sci&Tech"):
        features.append('0')
        features.append('0')
        features.append('1')
        
    givenIndex=10
    features.pop(givenIndex)
    features.pop(givenIndex)
    
    print(features)

    features = [float(x) for x in features]

    final_features = [np.array(features)]
    prediction = model[0].predict(final_features)
    prediction_2 = model[1].predict(final_features)
    output = round(prediction[0])
    if(output==0.0):
        output="Person is not placed"
    else:
        output="Person is Placed"+" with salary :  "+ str(prediction_2[0])


    return render_template('index.html', prediction_text=output)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
