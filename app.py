import pickle
import pandas
import numpy 
from flask import Flask, request, app, jsonify, url_for, render_template

app = Flask(__name__)

model = pickle.load(open('./regression_model.pkl', 'rb'))

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])

def predict_api():
    data = request.get_json(force=True)
    print(data)