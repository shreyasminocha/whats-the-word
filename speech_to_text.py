import os
from google.cloud import speech
from google.oauth2 import service_account

# Instantiates a client

credentials_info = service_account.Credentials.from_service_account_file('whats-the-word-326419-18451736e7c6.json')

client = speech.SpeechClient(credentials=credentials_info)

media_uri = "gs://lecture_audio_files/Phil Lempert's 2 minute Speech Demo.mp3"

audio_aud = speech.RecognitionAudio(uri=media_uri)

config_aud = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="en-US"
)

operation = client.recognize(
    config=config_aud,
    audio=audio_aud
)

response = operation.result()
print(response)