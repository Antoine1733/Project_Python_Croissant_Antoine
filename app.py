from flask import Flask, request, redirect, url_for, flash, jsonify , render_template
import numpy as np
import pandas as pd
import pickle as p
import json
from wtforms import Form, FloatField, validators



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/prediction', methods=['GET', 'POST'])
def prediction(): 
        result = None
        result2 = ""
        if request.method == 'POST':
            # data = [list(map(float,np.random.randint(1,high=255,size=36)))]
            data_id = int(request.form['data_id'])
            data=[[float(data_test.values[data_id][j]) for j in range(data_test.shape[1]-1)]]
            result = np.array2string(model.predict(data))
            if result == "[1]" :
                result2 = "red soil"
            if result == "[2]" :
                result2 = "cotton crop"
            if result == "[3]" :
                result2 = "grey soil"
            if result == "[4]" :
                result2 = "damp grey soil"
            if result == "[5]" :
                result2 = "soil with vegetation stubble"
            if result == "[7]" :
                result2 = "very damp grey soil"

            headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        return render_template('prediction.html', result=result2)



if __name__ == '__main__':
    modelfile = 'final_prediction.pickle'
    model = p.load(open(modelfile, 'rb'))
    data_test = pd.read_csv('sat.tst.csv', sep = ' ', header = None)
    app.run(debug=True, host='127.0.0.1')