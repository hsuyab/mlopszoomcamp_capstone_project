#!/usr/bin/env python
# coding: utf-8

import mlflow
import pandas as pd
from pycaret.datasets import get_data
from pycaret.regression import predict_model
from flask import Flask, request, jsonify



def read_data():
    data = get_data('diamond')
    data.drop('Price')
    return data

def predict():
    data = read_data()
    predictions = predict_model(model_pipeline_final, data=data)
    predictions.head()

app = Flask('duration-prediction')


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    diamond = request.get_json()    
    pred = (
        predict(diamond['Carat Weight'],
                diamond['Cut'],
                diamond['Color'],
                diamond['Polish'],
                diamond['Symmetry'],
                diamond['Report'])
        )

    result = {
        'price prediction': pred
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
