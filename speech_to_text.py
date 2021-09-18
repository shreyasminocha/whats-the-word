import os
from google.cloud import speech

# Instantiates a client
client = speech.SpeechClient()

media_uri = ""

audio = speech.RecognitionAudio(uri=media_uri)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="en-US",
)