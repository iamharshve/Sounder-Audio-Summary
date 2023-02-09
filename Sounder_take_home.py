#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[8]:


import pandas as pd


# In[10]:


import os


# In[18]:


os.chdir('Sounder_AI_ML_Engineering_Practical_Dataset')


# In[3]:


get_ipython().system('pip install requests')


# In[4]:


import requests
import json
from time import sleep


# ### Retrieve API key from Assembly AI and define headers and upload endpoints

# In[43]:


API_key = "426dc48e0e0a4a3b8774aaa0ca685571" 

headers = {
    'authorization': API_key, 
    'content-type': 'application/json',
}

upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcription_endpoint = "https://api.assemblyai.com/v2/transcript"


# ### Upload Function for Audio File

# In[44]:


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


# ### Transcribe the audio file

# In[37]:


def transcribe(upload_url): 

    json = {"audio_url": upload_url, "auto_chapters": True}
    
    response = requests.post(transcription_endpoint, json=json, headers=headers)
    transcription_id = response.json()['id']

    return transcription_id


# ### Response through get request

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


# ### Running the whole pipeline
# 

# In[39]:


upload_url = upload("masters-of-scale_build-the-right-flywheel.wav")

transcription_id = transcribe(upload_url)

response = get_result(transcription_id)

response


# ### Now Let's look at Summary for any paragraph or chapter i.e 4

# In[49]:


response["chapters"][4]['summary']


# ### Looking at start and end timestamp of chapter 4 in audio file

# In[47]:


response["chapters"][4]['start']


# In[48]:


response["chapters"][4]['end']


# ### Summary of Chapter 2

# In[45]:


response["chapters"][2]['summary']


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




