from flask import Flask, render_template
from flask import request
import smtplib
import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

app = Flask(__name__)

usr_loc = None
usr_eml = None
num_mins = None
phrases = None
police = None
transcrpt = 'Williams College'

@app.route('/', methods=['GET','POST'])

def AudioReader():

    usr_loc = request.form.get('Location')
    usr_eml = request.form.get('Email')
    num_mins = request.form.get('NumMinutes')
    phrases = request.form.get('Phrases')

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"/Users/Xiao/Desktop/appstuff/CampusEar/CampusEar-2b476fe18f5a.json"

# # Instantiates a client
    client = speech.SpeechClient()
# The name of the audio file to transcribe
    for file_name in os.listdir("/Users/Xiao/Desktop/appstuff/CampusEar/resources/output"):
        
        #file_name = os.path.join(
            #os.path.dirname(__file__),
            #'resources',
            #'output'
            #audio)#change this later
# Loads the audio into memory
        with io.open(file_name, 'rb') as audio_file:
            content = audio_file.read()
            audio = types.RecognitionAudio(content=content)
            
        config = types.RecognitionConfig(
                encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
                sample_rate_hertz=48000,
                language_code='en-US')#
    # Detects speech in the audio file
        response = client.recognize(config, audio)
        print("ended")
        for result in response.results:
            transcrpt = ('Transcript: {}'.format(result.alternatives[0].transcript))

            
            # print(usr_loc)
    #print(usr_eml)
    #print(num_mins)
    #print(phrases)
            
#do one phrase for now, we can figure out how to do multiple phrases later
        if (phrases != None) and (phrases in transcrpt):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("campusear@gmail.com", "campusearpassword")
            
            msg = transcrpt
            server.sendmail("campusear@gmail.com", "qz3@williams.edu", msg)
            server.quit()
        os.remove(file_name)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,port=1051)

