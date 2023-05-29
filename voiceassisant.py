import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import pywhatkit 
import sys
import pyautogui
import time
import operator
import requests
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 120)
def speak(audio):
 engine.say(audio)
 engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<14:
        speak("Good Afternoon!") 
    else: 
        speak("Good Evening!")
    
    speak("Ready To Comply. What can I do for you ?")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e: 
          print("Say that again please...") 
          return "None"
    return query
if __name__ == "__main__":
     wishMe()
     while True:
        query = takeCommand().lower()
        if 'play' in query:
                song = query.replace('play', '')
                speak('playing ' + song)
                pywhatkit.playonyt(song)
        elif 'search on youtube' in query:
            query = query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")
        elif 'open youtube' in query:
            speak("what you will like to watch ?")
            qrry = takeCommand().lower()
            pywhatkit.playonyt(f"{qrry}") 
        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")
        elif 'close youtube' in query:
            os.system("taskkill /f /im msedge.exe")   
        elif 'open google' in query:
            speak("what should I search ?")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=2)
            speak(results)    
        elif 'close google' in query:
            os.system("taskkill /f /im msedge.exe")
        elif 'music' in query:
            music_dir = 'Music'
            songs = os.listdir(music_dir) 
            os.startfile(os.path.join(music_dir, random.choice(songs)))
        elif 'close music' in query:
            os.system("taskkill /f /im vlc.exe")  
        elif 'what time ' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"Sure, the time is {strTime}")  
            print()
        elif 'who is' in query:
            person = query.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)    
        elif "open notepad" in query:
            npath = "C:\WINDOWS\system32\\notepad.exe" 
            os.startfile(npath)
        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")         
        elif 'write' in query: #10
            query = query.replace("write", "")
            pyautogui.write(f"{query}") 
        elif "calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("ready")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {'+' : operator.add,'-' : operator.sub,'x' : operator.mul,'divided' : operator.__truediv__, }[op]
            def eval_bianary_expr(op1,oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_bianary_expr(*(my_string.split())))
        elif "what is your name" in query:
            print('My Name Is Elsa')
            speak('My Name Is Elsa')
            print('I can Do Everything that my creator programmed me to do')
            speak('I can Do Everything that my creator programmed me to do')
        elif "who created you" in query:
                print('Created by Reethika, I created with Python Language, in Visual Studio Code.')
                speak('Created by Reethika, I created with Python Language, Visual Studio Code.')    
        elif 'joke' in query:
            speak(pyjokes.get_joke())
             
             
#