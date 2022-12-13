
from fastapi import FastAPI, Request

import pickle
from typing import List

from limpieza import preprocess

from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

import requests, responses

import json

import pandas as pd

from youtube_scrapper import comment_threads

app = FastAPI()
# configure header parameters to access

# Conection with react port
origins = [
    "http://localhost:3000",
    "localhost:3000"
]
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

@app.get("/predict_youtube_comment")
async def predict_youtubeVid(prompt:str):
    video_id = prompt
    YOUR_API_KEY = "AIzaSyB96OJnpVcFcf3IJ1_FQqc7KQWnHkxNv3Y"

    response = requests.get(f"https://youtube.googleapis.com/youtube/v3/commentThreads?part=id%2C%20snippet&maxResults=5&videoId={video_id}&key={YOUR_API_KEY}")

   # From Json to Dataframe
    data = response.json()
    # print(data)
    print(type(data))
    #create a dict from the json and index only the comments from video
    
    #lista vacia con los reultados de los comentarios
    predictions= []
    
    x = range(5)
    for n in x:
      comments = dict(comment_threads= data['items'][n]['snippet']["topLevelComment"]["snippet"]['textDisplay'], index=[n])
      
    
      
    #create a df from the dict
      df = pd.DataFrame.from_dict(comments)
      print (df['comment_threads'])

# select only the comments column from the df
    
   

    #Apply ML model
      processed_data= preprocess(df['comment_threads'])
   
      print(processed_data)
      vectorised_data = vectoriser.transform(processed_data)
      print(vectorised_data)
      prediction = model.predict(vectorised_data)
      print('----------------PREDICTION---------------------')
      print(prediction)
    
      
      

      value = 'Toxic comment' if prediction == 1 else 'Not toxic'
      predictions.append(value)

    print(predictions)

    results = dict(zip(range(len(predictions)), predictions))

    print(results)
      

    

    

    

    

    

# 
#      

    
    
    return {
#     # If prediction is a data frame use this to respond to the client
        'Video Comments' : results
      }
    
    

    

# # @app.get("/youtube_scrapper")
# # # async def comment_scrapper(prompt2=str):
# # #     # comment_scrap = comment_threads(prompt2)

# # #     # print(comment_scrap)

# # #     return comment_scrapper






    

   
    
    
    



