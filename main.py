import base64
import speech_recognition as sr
from flask import Flask, jsonify

def decode_audio(string1,filename):
    image=base64.b64decode(string1)
    with open(filename, 'wb') as f:
        f.write(image)
        f.close()

def sp_to_txt(audiofile):
    file = audiofile
    r = sr.Recognizer()

    with sr.AudioFile(file) as source:
        # reads the audio file. Here we use record instead of
        # listen
        audio = r.record(source)

    text = r.recognize_google(audio)

    print(text)
    return text



