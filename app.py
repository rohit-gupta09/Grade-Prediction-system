# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 15:43:09 2023

@author: DELL
"""

import uvicorn
from fastapi import FastAPI
from GradePrediction import Grade
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import pandas as pd
import joblib


app=FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    )

pickle_in=open("TraivisMODEL.joblib","rb")

model=joblib.load(pickle_in)

@app.get('/')
def index():
    return {'message':'Hello, stranger'}

@app.post('/predict')
def predict_species(data:Grade):
    data=data.dict()
    print(data)
    print("Helo")
    first=data['first']
    print(first)
    second=data['second']
    print(second)
    third=data['third']
    print(third)
    fourth=data['fourth']
    print(fourth)
    fifth=data['fifth']
    print(fifth)
    sixth=data['sixth']
    print(sixth)
    seventh=data['seventh']
    print(seventh)
    eight=data['eight']
    print(eight)
    ninth=data['ninth']
    print(ninth)
    tenth=data['tenth']
    print(tenth)
    eleventh=data['eleventh']
    print(eleventh)
    
    
    
    prediction=model.predict([[first,second,third,fourth,fifth,sixth,seventh,eight,ninth,tenth,eleventh]])
    if(prediction[0]==0):
        prediction="A"
    elif(prediction[0]==1):
        prediction="B"
    else:
        prediction="C"
    
    return{
        'prediction':prediction
        }

#Run the api with the unicorn on port 8000
if __name__ == '__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)

#uvicorn app:app --reload