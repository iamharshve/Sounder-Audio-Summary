#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[8]:


import pandas as pd


# In[10]:


import os


# In[ ]:





# In[18]:


os.chdir('Sounder_AI_ML_Engineering_Practical_Dataset')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[3]:


get_ipython().system('pip install requests')


# In[4]:


import requests
import json
from time import sleep


# In[31]:


API_key = "426dc48e0e0a4a3b8774aaa0ca685571" 

headers = headers = {
    'authorization': API_key, 
    'content-type': 'application/json',
}

upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcription_endpoint = "https://api.assemblyai.com/v2/transcript"


# In[ ]:





# In[36]:


def upload(file_path):

    def read_audio(file_path):

        with open(file_path, 'rb') as f:
            while True:
                data = f.read(5_242_880)
                if not data:
                    break
                yield data

    upload_response =  requests.post(upload_endpoint, 
                                     headers=headers, 
                                     data=read_audio(file_path))

    return upload_response.json().get('upload_url')


# In[ ]:





# In[37]:


def transcribe(upload_url): 

    json = {"audio_url": upload_url, "auto_chapters": True}
    
    response = requests.post(transcription_endpoint, json=json, headers=headers)
    transcription_id = response.json()['id']

    return transcription_id


# In[ ]:





# In[38]:


def get_result(transcription_id): 

    current_status = "queued"

    endpoint = f"https://api.assemblyai.com/v2/transcript/{transcription_id}"

    while current_status not in ("completed", "error"):
        
        response = requests.get(endpoint, headers=headers)
        current_status = response.json()['status']
        
        if current_status in ("completed", "error"):
            return response.json()
        else:
            sleep(10)


# In[ ]:





# In[39]:


upload_url = upload("masters-of-scale_build-the-right-flywheel.wav")

transcription_id = transcribe(upload_url)

response = get_result(transcription_id)

response


# In[41]:


response["chapters"][4]['summary']


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




