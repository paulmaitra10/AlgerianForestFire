import pickle
from flask import Flask, request, jsonify,render_template
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

## import regressor model and standard scaler pickle
reg_model = pickle.load(open('models/regressor.pkl','rb'))
standard_scaler = pickle.load(open('models/scaler.pkl','rb'))


## route for home page
@app.route('/')
def index():
    # return render_template('index.html')
    return render_template('index.html')

## for prediction
@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        ## first read data and then interact with pickle file (use request)
        ## the order of input should be same as in the model file
        Temperature = float(request.form.get('Temperature'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        
        
        new_data_scaled = standard_scaler.transform([[Temperature,Rain,FFMC,DMC,ISI]])
        result = reg_model.predict(new_data_scaled)
        
        if result > 15:
            return render_template('home1.html',result="Fuel Moisture Code index is {:.4f} ---- Warning!!! High hazard rating".format(result[0]))
        else:
            return render_template('home1.html',result="Fuel Moisture Code index is {:.4f} ---- Safe.......Low hazard rating".format(result[0]))
        
    else:
        return render_template('home1.html')
        # return render_template('home.html')

if __name__=="__main__":
    app.run(debug=True, port=5000)
