
from fastapi import FastAPI, Response
from pydantic import BaseModel
import pickle
import pandas
from limpieza import preprocess
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel


app = FastAPI()


#Vectoriser
with open ('Vectoriser.pkl', 'rb') as d:
    vectoriser = pickle.load(d)
#Model 
with open ('MultinomialNB_NLP.pkl', 'rb') as f:
    model = pickle.load(f)


@app.post("/predict")
async def predict_hate(prompt:str):
    
    
    processed_data= preprocess([prompt])
    print(processed_data)
    vectorised_data = vectoriser.transform(processed_data)
    print(vectorised_data)
    prediction = model.predict(vectorised_data)
    print('----------------PREDICTION---------------------')
    print(prediction)
    
    value = 'Toxic comment' if prediction == 1 else 'Not toxico'

    
    
    return {
    # If prediction is a data frame use this to respond to the client
    
    'prediction': value
    
    
    }


    

   
    
    
    



