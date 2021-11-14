# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 21:22:57 2021

@author: PETER
"""

from flask import Flask,render_template,url_for,request
import pandas as pd 

import pickle

# load the model from disk
loaded_model=pickle.load(open('random_forest_regressor.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    df=pd.read_csv('Data/Real-Data/real_2018.csv')
    def transform_dropna(dataframe):
        #Transforming my columns to float datatype
        cols = list(dataframe.columns)
        for col in cols:
            #for each column cast from string to float and for non digits change NaN
            dataframe[col] = pd.to_numeric(dataframe[col], downcast='float',errors='coerce')
        #Drop NaN values
        dataframe = dataframe.dropna()
        return dataframe
    df = transform_dropna(df)
    my_prediction=loaded_model.predict(df.iloc[:,:-1].values)
    my_prediction=my_prediction.tolist()
    return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)