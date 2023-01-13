import speech_recognition as sr
from time import ctime
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
    print("Sorry i am unable to get that")
  except sr.RequestError:
    print("Sorry, speech service is down")
  return voice_input
    
def respond(voice_input):
    if "what is your name" in voice_input:
        print('My name is Luna')
    if "what time is it"   in voice_input:
        print(ctime())    
    if "search" in voice_input:
        search=record_audio('what do you want to search for?')   
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('here is what i found for you ' + search)
    if "find location" in voice_input:
        loc = record_audio('What location you wanna search for?')   
        url = 'https://google.nl/maps/place/' + loc + '/&amp'
        webbrowser.get().open(url)
        print('Here is the ' + loc)    

print('How may I be of assistance?')
voice_input=record_audio()
respond(voice_input)