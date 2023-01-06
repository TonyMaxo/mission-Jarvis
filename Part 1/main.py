from importlib import import_module
from time import time
from urllib.request import HTTPSHandler
import pyttsx3
from pywhatkit import main
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes
import requests
import pyautogui
from wikipedia.wikipedia import search 
from pywikihow import WikiHow
import sys
import random
from requests import get
import requests
#webbrowser.register('google-chrome',  instance=None,  preferred=False)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

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
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")   

    else:
        speak("Good Evening sir")  

    speak( 'i am jarvis , how can i help you')

def takeCommand():
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
        # print(e)    
        print("Say that. again please...")  
        return "None"
       
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your Email', 'Your Password')
    server.sendmail('Your Email', to, content)
    server.close()

def search_wikihow(query, max_results=10, lang ="en"):
    return list(WikiHow.search(query, max_results, lang))

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

         

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        if 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'joke' in query:
           random_joke = pyjokes.get_joke()
           print(random_joke)
           speak(random_joke)

        elif ' take screenshot' in query:
               speak('sir, please tell me name to save screen shot')        
               name = takeCommand().lower()
               speak('please sir, hold your screen  for few secounds. i taking screenshot ')
               img = pyautogui.screenshot()
               img.save(f'{name}.png')
               speak('i am done saved in main folder')         
          
        elif 'search on google' in query:
            import wikipedia as googlescrap
            query= query.replace('search on google', '')
            pywhatkit.search(query)
            speak(' this  is what i found on google')

            try:
                results = googlescrap.summary(query,2)
                speak(results)
            except Exception as e:
                speak('speakable data  available')

        elif 'search on youtube' in query:
            results = '//www.youtube.com/results?search_query=' + query
            webbrowser.open(results)
            speak(results)   
          
        elif 'switch window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")
            speak('switching the window. sir,')

        elif 'creat new screen' in query:
            pyautogui.keyDown("ctrl")
            pyautogui.keyDown("win")
            pyautogui.press("D")
            pyautogui.keyUp("ctrl")
            pyautogui.keyUp("win")
            speak('creating new screen')

        elif 'open  sever' in query:
            speak('sir,open minecraft sever ')
            webbrowser.open("https://aternos.org/server")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Sir, opening the youtube")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'open python' in query:
            webbrowser.open("coursera.org") 

        elif 'open fps game' in query:
            webbrowser.open("venge.io")   

        elif 'open mail' in query:
            webbrowser.open("mail.google.com")   
            speak("Sir, opening the mail")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Admin\\Music\\my.mp3'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "D:\surya0\vs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
            speak("Sir, opening the code")

        elif 'open google' in query:
            go = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(go)
            speak("Sir, opening the google")

        elif 'open epic store' in query:
            store = "D:\games\epic store\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe"
            os.startfile(store)
            speak("Sir, opening the epic store")
        
        elif 'open cmd' in query:
            cmd = "C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(cmd)
            speak("Sir, opening the cmd")

        elif 'open minecraft' in query:
            luncher = "C:\\Users\\SURYA\AppData\\Roaming\\.minecraft\\TLauncher.exe"
            os.startfile(luncher)
            speak("Sir, opening the minecraft")
    
        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "you@youremail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry surya, I couldn't send the email")

        elif 'are you there' in query:
          speak('i am online and ready sir,') 
          takeCommand() 
        
        elif 'shutdown' in query:
            speak('bye sir, see you again.')
            sys.exit()

        elif 'sleep' in query:
            speak('ok. sir, i am going to sleep. call me when you need me')   
            break

        #--------------------------------------to find my loacatoion using IP Address

        elif 'where i am' in query:
            speak('wait sir, let me check')
            try: 
                ipadd = requests.get('https://api.ipify.org').text
                print(ipadd)
                url = 'https://get.geojs.io'+ipadd+'.json'
                geo_reqests = requests.get(url)
                geo_data = requests.get.json()
                # print(geo_data)
                city = geo_data['city'] 
                # state = geo_data['state']
                country = geo_data['country']
                speak(f'sir, i am sure. we are  in {city}city of {country}country')
            except Exception as e:
                speak('sorry sir, due network issue  i am not able to find where we are')  
                pass

        elif 'open disk D' in query:
            disk = "D:\\"
            os.startfile(disk)
            speak('opening disk d sir,')
        
        elif 'open disk c' in query:
            disk = "C:\\"
            os.startfile(disk)
            speak('opening disk c sir,')
            
        elif 'open this pc'in query:
            thispc = "This pc"
            os.startfile(thispc)
            speak('opening this pc,')
        
        elif 'what is the full form of jarvis' in query:
            speak("Just A Rather Very Intelligent System")



