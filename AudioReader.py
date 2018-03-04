from flask import Flask, render_template
from flask import request
import smtplib
import io
import os
import time
# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

from subprocess import Popen

app = Flask(__name__)

usr_loc = None
usr_eml = None
num_mins = None
phrases = None
police = None
transcrpt = 'Williams College'

@app.route('/', methods=['GET','POST'])

def AudioReader():
    global usr_loc
    usr_loc = request.form.get('Location')
    global usr_eml
    usr_eml = request.form.get('Email')
    global num_mins
    num_mins = request.form.get('NumMinutes')
    global phrases
    phrases = request.form.get('Phrases')
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True,port=1051)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\seanl\Downloads\CampusEar-2b476fe18f5a.json"
# # Instantiates a client
client = speech.SpeechClient()
while True:

# The name of the audio file to transcribe
    Popen("script.bat", cwd=r"C:\Users\seanl\Documents\GitHub\CampusEar")
    time.sleep(4)
    for file_name in os.listdir(r"C:\Users\seanl\Documents\GitHub\CampusEar\resources\output"):
        print(file_name)

# Loads the audio into memory
        with io.open(r"C:\Users\seanl\Documents\GitHub\CampusEar\resources\output" +"\\" + file_name, 'rb') as audio_file:
            content = audio_file.read()
            audio = types.RecognitionAudio(content=content)
            
        config = types.RecognitionConfig(
                encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
                sample_rate_hertz=44100,
                language_code='en-US')#
    # Detects speech in the audio file
        response = client.recognize(config, audio)
        # print("ended")
        for result in response.results:
            transcrpt = ('Transcript: {}'.format(result.alternatives[0].transcript))
            # print(transcrpt)
        print(phrases)
        print(transcrpt)

        if (phrases != None) and (phrases in transcrpt):
            print("we have a match!!!!!")
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("campusear@gmail.com", "campusearpassword")
            
            msg = "\r\n".join([
                    "From: " + "campusear@gmail.com",
                    "To: " + usr_eml,
                    "Subject: Something of interest came up",
                    "",
                    transcrpt
                    ])
            server.sendmail("campusear@gmail.com", usr_eml, msg)
            print(msg)
            server.quit()


        os.remove(r"C:\Users\seanl\Documents\GitHub\CampusEar\resources\output" +"\\" + file_name)



