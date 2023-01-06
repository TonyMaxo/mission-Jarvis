import speech_recognition as sr
import os
import pyttsx3
from time import sleep
from pyautogui import click
import pyjokes
import pywhatkit
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()

def epicstore(Query):
    store = ""
    os.startfile(store)
    Speak("Sir, opening the epic store")

def cmd(Query):
    cmd = "C:\\WINDOWS\\system32\\cmd.exe"
    os.startfile(cmd)
    Speak("Sir, opening the cmd")

def minecraft(Query):
    luncher = "C:\\Users\\SURYA\AppData\\Roaming\\.minecraft\\TLauncher.exe"
    os.startfile(luncher)
    sleep(15)
    click(x=893, y=734)
    Speak("Sir, opening the minecraft")

def code(Query):
    codePath = "E:\Surya0\Microsoft VS Code\Code.exe"
    os.startfile(codePath)
    Speak("Sir, opening the code")

def joke(Query):
    random_joke = pyjokes.get_joke()
    print(random_joke)
    Speak(random_joke)

def play(Query):
    song = Query.replace('play', '')
    Speak('playing ' + song)
    pywhatkit.playonyt(song)

def unity(Query):
    unity = "C:\\Program Files\\Unity\\Hub\\Editor\\2021.1.20f1\\Editor\\Unity.exe"  
    os.startfile(unity) 
    Speak("Sir, opening the unity") 
       