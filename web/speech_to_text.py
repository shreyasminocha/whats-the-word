import os
from google.cloud import speech
from google.oauth2 import service_account
import re

def speech_to_text(media_uri):
    '''
    Returns the separated sentences from text-to-speech.
    In
        media_uri; filepath of the video
    Out
        list containing the sentences as strings; separating by periods (.)
    '''
    # Instantiates a client

    #media_uri = "gs://lecture_audio_files/Class 1, Part 2 - Economic Growth Theory and the Direct Elements in Innovation-n0QLcw-CHmk.mp3"

    #media_uri = "gs://lecture_audio_files/Phil Lempert's 2 minute Speech Demo.mp3"


    credentials_info = service_account.Credentials.from_service_account_file('whats-the-word-326419-18451736e7c6.json')

    client = speech.SpeechClient(credentials=credentials_info)


    audio_aud = speech.RecognitionAudio(uri=media_uri)

    config_aud = speech.RecognitionConfig(
        #encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
        enable_automatic_punctuation=True,
        enable_word_time_offsets=False
    )

    operation = client.long_running_recognize(
        config=config_aud,
        audio=audio_aud,
    )

    sentences =  ""
    response = operation.result()

    for item in response.results:
        sentences = sentences + format(item.alternatives[0].transcript)

    sentences = re.split('[\.?!]', sentences)
    return sentences


