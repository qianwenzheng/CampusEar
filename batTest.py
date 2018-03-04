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
print("we have a match!!!!!")
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("campusear@gmail.com", "campusearpassword")

msg = None + !
server.sendmail("campusear@gmail.com", "qz3@williams.edu", msg)
server.quit()
