import os 
import time 
import playsound
import speech_recognition as sr 
from gtts import gTTS 
import requests
import json



def speak(text):
  tts = gTTS(text=text, lang="en")
  filename = 'voice.mp3'
  tts.save(filename)
  playsound.playsound(filename)
  
  
apiData_get = requests.get('https://corona.lmao.ninja/v2/countries/ghana')

apiData_toJSON = apiData_get.json()
text =  f'Corona Virus update for ghana. Number of Confirmed Cases : {apiData_toJSON ["cases"]}\n.Number of Deaths: {apiData_toJSON ["deaths"]}\n.Critical Cases: {apiData_toJSON ["critical"]}\n.Recoveries: {apiData_toJSON ["recovered"]}\n.Numbers Tested: {apiData_toJSON ["tests"]}\n.Population: {apiData_toJSON ["population"]}'

speak(text)  