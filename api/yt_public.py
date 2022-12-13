# -- coding: utf-8 --

import requests

def find_yt_comments ():
    YOUR_API_KEY = "AIzaSyB96OJnpVcFcf3IJ1_FQqc7KQWnHkxNv3Y"

    data = requests.get(f"https://youtube.googleapis.com/youtube/v3/commentThreads?part=id%2C%20snippet&maxResults=2&videoId=XTjtPc0uiG8&key={YOUR_API_KEY}")

    print(data.content)


//how to index range python?

