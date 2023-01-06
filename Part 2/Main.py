import datetime
import webbrowser as web
from time import sleep
from types import coroutine

import cv2
import pyttsx3
import requests
import speech_recognition as sr
from keyboard import press, press_and_release, write
import playsound
from pyautogui import click
from win10toast import ToastNotifier

from Features import GoogleSearch

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()

def make_request(url):
  response = requests.get(url)
  return response.text
def wishMe():
    playsound('E:\\Ai\\Mission J.A.R.V.I.S\\Part 2\\DataBase\\Sounds\\3.mp3') 
    vid = cv2.videocapture ("E:\\Ai\Mission J.A.R.V.I.S\\Part 2\\MainDisk\Videos\\Captures\LIVE WALLPAPER _ AI JARVIS - IRON-MAN _ STATUS REALM _ PC_DESKTOP _ (Download link in description).mp4")   

def TakeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:  
        return "None"
       
    return query
    
if __name__ == "__main__":

    wishMe()  
         
    while True:
    # if 1:
        query = TakeCommand().lower()

      
        if 'google search' in query:
            GoogleSearch(query)
        
        elif 'youtube search' in query:
            Query = query.replace("jarvis","")
            query = Query.replace("youtube search","")
            from Features import YouTubeSearch
            YouTubeSearch(query)

        elif 'set alarm' in query:
            from Features import Alarm
            Alarm(query)

        elif 'download' in query:
            from Features import DownloadYouTube
            DownloadYouTube()
            
        elif 'speed test' in query:
            from Features import SpeedTest
            SpeedTest()

        elif 'whatsapp message' in query:

            name = query.replace("whatsapp message","")
            name = name.replace("send ","")
            name = name.replace("to ","")
            Name = str(name)
            speak(f"Whats The Message For {Name}")
            MSG = TakeCommand()
            from Automations import WhatsappMsg
            WhatsappMsg(Name,MSG)

        elif 'call' in query:
            from Automations import WhatsappCall
            name = query.replace("call ","")
            name = name.replace("jarvis ","")
            Name = str(name)
            WhatsappCall(Name)

        elif 'show chat' in query:
            speak("With Whom ?")
            name = TakeCommand()
            from Automations import WhatsappChat
            WhatsappChat(name)

        elif 'space news' in query:


            speak("Tell Me The Date For News Extracting Process .")

            Date = TakeCommand()

            from Features import DateConverter

            Value = DateConverter(Date)

            from Nasa import NasaNews

            NasaNews(Value)

        elif 'about' in query:
            from Nasa import Summary
            query = query.replace("jarvis ","")
            query = query.replace("about ","")
            Summary(query)

        elif 'mars images' in query:

            from Nasa import MarsImage

            MarsImage()

        elif 'track earth' in query:

            from Nasa import IssTracker

            IssTracker()

        elif 'near earth' in query:
            from Features import DateConverter
            from Nasa import Astro
            speak("Tell Me The Starting Date .")
            start = TakeCommand()
            start_date = DateConverter(TakeCommand)
            speak("And Tell Me The End Date .")
            end = TakeCommand()
            end_date = DateConverter(end)
            Astro(start_date,end_date=end_date)

        elif 'my location' in query:

            from Features import My_Location

            My_Location()

        elif 'where is' in query:

            from Automations import GoogleMaps
            Place = query.replace("where is ","")
            Place = Place.replace("jarvis" , "")
            GoogleMaps(Place)

        elif 'online' in query:

            from Automations import OnlinClass

            speak("Tell Me The Name Of The Class .")

            Class = TakeCommand()

            OnlinClass(Class)

        elif 'write a note' in query:

            from Automations import Notepad
            Notepad()

        elif 'Exit' in query:

            from Automations import CloseNotepad

            CloseNotepad()

        elif 'time table' in query:

            from Automations import TimeTable

            TimeTable()
        
        elif 'temperature' in query:
            from Features import temp
            temp(query)

        elif 'calculat' in query:
            from Features import calculator
            calculator(query)

        elif 'search'in query:
           from Features import WolfRam
           result = WolfRam
           speak(result)
        
        elif 'open code' in query:
            from apps import code
            code(query)

        elif 'open new tab' in query:

           press_and_release('ctrl + n')

        elif 'close tab' in query:

            press_and_release('ctrl + w')

        elif 'open new window' in query:

            press_and_release('ctrl + n')

        elif 'show history' in query:

            press_and_release('ctrl + h')

        elif 'download' in query:

            press_and_release('ctrl + j')

        elif 'open bookmark' in query:

            press_and_release('ctrl + d')

            press('enter')

        elif 'incognito' in query:

            press_and_release('Ctrl + Shift + n')

        elif 'switch tab' in query:

            tab = query.replace("switch tab ", "")
            Tab = tab.replace("to","")
            
            num = Tab

            bb = f'ctrl + {num}'

            press_and_release(bb)

        elif 'open website ' in query:
          
            name = query.replace("open website ","")

            NameA = str(name)

            if 'youtube' in NameA:

                web.open("https://www.youtube.com/")

            elif 'instagram' in NameA:

                web.open("https://www.instagram.com/")

            else:

                string = "https://www." + NameA + ".com"

                string_2 = string.replace(" ","")

                web.open(string_2)
                speak(" opening" + query )

            if 'pause' in query:

                press('space bar')

            elif 'resume' in query:

                press('space bar')

            elif 'full screen' in query:

                press('f')

            elif 'film screen' in query:

                press('t')

            elif 'skip' in query:

                press('l')

            elif 'back' in query:

                press('j')

            elif 'increase volume' in query:

                press_and_release('SHIFT + .')

            elif 'decrease volume' in query:

                press_and_release('SHIFT + ,')

            elif 'open previous window' in query:

                press_and_release('SHIFT + p')

            elif 'open next window' in query:

                press_and_release('SHIFT + n')
            
            elif 'search' in query:

                click(x=667, y=146)

                speak("What To Search Sir ?")

                search = TakeCommand()

                write(search)

                sleep(0.8)

                press('enter')

            elif 'mute mike' in query:

                press('m')

            elif 'unmute mike' in query:

                press('m')

            else:
                speak("No Command Found!")
            

            if 'open home screen' in query:

                press_and_release('windows + m')

            elif 'minimize window' in query:

                press_and_release('windows + m')

            elif 'show start menu' in query:

                press('windows')

            elif 'open setting' in query:

                press_and_release('windows + i')

            elif 'open search' in query:

                press_and_release('windows + s')

            elif ' take a screenshot' in query:

                press_and_release('windows + SHIFT + s')

            elif' switch window' in query:
                from Automations import window
                window()

        elif 'open unity' in query:
            from apps import unity
            unity(query)
        
        elif 'open cmd' in query:
            from apps import cmd
            cmd(query)

        if 'home screen' in query:

            press_and_release('windows + m')

        elif 'minimize' in query:

            press_and_release('windows + m')

        elif 'show start' in query:

            press('windows')

        elif 'open setting' in query:

            press_and_release('windows + i')

        elif 'open search' in query:

            press_and_release('windows + s')

        elif 'screen shot' in query:

            press_and_release('windows + SHIFT + s')

        elif 'restore windows' in  query:

            press_and_release('Windows + Shift + M')

        elif 'open minecraft' in query:
          from apps import minecraft 
          minecraft(query)  

        elif 'tell me a joke' in query:
         from apps import joke 
         joke(query)

        elif 'what is the full form of jarvis' in query:
            speak("Just A Rather Very Intelligent System")

        if 'play' in query:
         from apps import play 
         play(query)
 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")


        elif 'sleep' in query:
            speak( "by sir, have nice day")
            break