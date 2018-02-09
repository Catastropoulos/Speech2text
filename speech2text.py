# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 02:24:23 2018

@author: Ayoub
"""

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print ('Say Something!')
    audio = r.listen(source)
try:
    print(r.recognize_google(audio, language='fr-FR'))
except:
    pass
