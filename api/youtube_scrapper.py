# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

from googleapiclient.discovery import build

from utils.comments import make_csv


    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyB96OJnpVcFcf3IJ1_FQqc7KQWnHkxNv3Y"

youtube = build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)


def comment_threads(videoId):
    
    data = []
    request = youtube.commentThreads().list(    
    part="snippet",
    videoId=videoId,
    maxResults=1,
    access_token="AIzaSyB96OJnpVcFcf3IJ1_FQqc7KQWnHkxNv3Y")
    
    response = request.execute()
    data = dict(comments= response['items'][0]['snippet']["topLevelComment"]["snippet"]['textDisplay'])
    return data

# print (comment_threads(videoId="XTjtPc0uiG8"))



    

    
    
    



