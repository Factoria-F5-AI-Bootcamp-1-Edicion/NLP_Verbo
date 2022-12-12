#Importamos librerías que se utilizarán y se llama al archivo de limpieza
from fastapi import FastAPI, Request
import pickle
from limpieza import preprocess
from fastapi.middleware.cors import CORSMiddleware


#Se crea la app en fastapi
app = FastAPI()

# Conexión con el puerto de entrada 3000
origins = [
    "http://localhost:3000",
    "localhost:3000"
]
#Creamos un origen con el protocolo HTTP para conectarlo con el front-end
app.add_middleware(
    CORSMiddleware, # https://fastapi.tiangolo.com/tutorial/cors/
    allow_origins=['*'], # wildcard to allow all, more here - https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin
    allow_credentials=True, # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials
    allow_methods=['*'], # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Methods
    allow_headers=['*'], # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Headers
)





    


#Vectoriser
with open ('Vectoriser.pkl', 'rb') as d:
    vectoriser = pickle.load(d)
#Model 
with open ('xg_boost.pkl', 'rb') as f:
    model = pickle.load(f)


@app.get("/predict")
async def predict_hate(prompt:str):
    
    processed_data= preprocess([prompt])
    print(processed_data)
    vectorised_data = vectoriser.transform(processed_data)
    print(vectorised_data)
    prediction = model.predict(vectorised_data)
    print('----------------PREDICTION---------------------')
    print(prediction)
    
    value = 'Toxic comment' if prediction == 1 else 'Not toxic'

    
    
    return {
    # If prediction is a data frame use this to respond to the client
    
    'prediction': value
    
    
    }


    

   
    
    
    



