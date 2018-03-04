# <<<<<<< HEAD
# import io
# import os
#
# # Imports the Google Cloud client library
# from google.cloud import speech
# from google.cloud.speech import enums
# from google.cloud.speech import types
#
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\seanl\Downloads\CampusEar-2b476fe18f5a.json"
# # Instantiates a client
# client = speech.SpeechClient()
#
# # The name of the audio file to transcribe
# file_name = os.path.join(
#     os.path.dirname(__file__),
#     'resources',
#     'testAudio.flac')
#
# # Loads the audio into memory
# with io.open(file_name, 'rb') as audio_file:
#     content = audio_file.read()
#     audio = types.RecognitionAudio(content=content)
#
# config = types.RecognitionConfig(
#         encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
#         sample_rate_hertz=48000,
#         language_code='en-US')
#
# # Detects speech in the audio file
# response = client.recognize(config, audio)
# print("ended")
# for result in response.results:
#     print('Transcript: {}'.format(result.alternatives[0].transcript))
# =======
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def AudioReader():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,port=1037)
# >>>>>>> a2e8f411d4e0d31958dabdbc85563e74be151b4c
