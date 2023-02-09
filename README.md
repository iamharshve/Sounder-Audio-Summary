# Sounder-Audio-Summary
Audio Summary Python Script

Github Repo Link - https://github.com/iamharshve/Sounder-Audio-Summary


How to Summarize Audio File?

1. Transcribe Audio File using API service and then it's broken into individual paragraphs
2. Summarization module of API summarizes individual paragraphs and returns audio summary


Steps are demonstrated below(please refer to python script for more details):

1. Get the API Token for Assembly AI(API service for transcription)

2. Install Libraries 

3. Send Transcription Requests

4. Define Authorization Key, Headers

5. Upload the Audio file

6. Transcribe the Audio File

7. Get the Result

8. Run the Pipeline

9. We can access the Summary with chapter key of resultant file




Alternative way to Accomplish the Summary of text would be to Input the text to Transformer Summarizer of BART or t5 or other similar pre-trained model.


Sample code below:


from transformers import pipeline

summarizer = pipeline("summarization", model = "t5-base", tokenizer = "t5-base", framework = "tf")

summary_text = summarizer(text, max_length = 100, min_length = 5, do_sample = False)[0]['summary_text']

print(summary_text)



