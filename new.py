from sys import platlibdir
import speech_recognition as sr
from time import ctime
import time
import playsound
import os
import random
from gtts import gTTS
import webbrowser

rg=sr.Recognizer() 
  
def record_audio(ask=False):
 with sr.Microphone() as source:
  if ask:
        print(ask)
  audio=rg.listen(source)
  try:
      voice_input=rg.recognize_google(audio)
      print(voice_input)
  except  sr.UnknownValueError:
    luna_speak("Sorry i am unable to get that")
  except sr.RequestError:
    luna_speak("Sorry, speech service is down")
  return voice_input

def luna_speak(audio_string):
    tts=gTTS(text=audio_string, lang='en')
    r=random.randint(1,  10000000)
    audio_file='audio-' +str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file) 

    
def respond(voice_input):
    if "what is your name" in voice_input:
        luna_speak('My name is Luna')
    if "what time is it"   in voice_input:
        luna_speak(ctime())    
    if "search" in voice_input:
        search=record_audio('what do you want to search for?')   
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        luna_speak('here is what i found for you ' + search)
    if "find location" in voice_input:
        loc = record_audio('What location you wanna search for?')   
        url = 'https://google.nl/maps/place/' + loc + '/&amp'
        webbrowser.get().open(url)
        luna_speak('Here is the ' + loc)    


time.sleep(1)
luna_speak('How may I be of assistance?')
while 1:
    voice_input=record_audio()
    respond(voice_input)