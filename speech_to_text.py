import os
from google.cloud import speech

# Instantiates a client
client = speech.SpeechClient()

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
