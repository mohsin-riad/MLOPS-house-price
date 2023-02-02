import pickle
import json
import pandas as pd
import numpy as np
from flask import Flask, request, app, jsonify, url_for, render_template
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

model = pickle.load(open('./regression_model.pkl', 'rb'))
sc = pickle.load(open('./scaler.pkl', 'rb'))

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/predict_api', methods=['POST'])

def predict_api():
    data = request.json['data']
    mod_data = sc.transform(np.array(list(data.values())).reshape(1,-1))
    output = model.predict(mod_data)
    return jsonify(output[0])

if __name__=="__main__":
    app.run(debug=True)