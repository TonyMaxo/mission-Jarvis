import os
import webbrowser as web
from datetime import datetime
from os import startfile
from time import sleep

import bs4
import geocoder
import pyautogui
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import wikipedia
import wolframalpha
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
from keyboard import press, press_and_release, write
from notifypy import notify
from pyautogui import click
from pywikihow import RandomHowTo, search_wikihow

from Main import speak

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

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

def WhatsappMsg(name,message):
     
    startfile("C:\\Users\\bemot\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

    sleep(10)

    click(x=195, y=115)

    sleep(1)

    write(name)

    sleep(0.5)

    click(x=188, y=249)

    sleep(0.5)

    click(x=571, y=690)

    sleep(0.5)

    write(message)

    press('enter')

def WhatsappCall(name):

    startfile("C:\\Users\\bemot\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

    sleep(10)

    click(x=195, y=115)

    sleep(1)

    write(name)

    sleep(1)

    click(x=188, y=249)

    sleep(1)

    click(x=571, y=690)

    sleep(1)

    click(x=1198, y=63)

def WhatsappChat(name):

    startfile("C:\\Users\\bemot\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

    sleep(10)

    click(x=195, y=115)

    sleep(1)

    write(name)

    sleep(1)

    click(x=188, y=249)

    sleep(1)

    click(x=571, y=690)

    sleep(1)

def ChromeAuto(command):

    query = str(command)

    if 'new tab' in query:

        press_and_release('ctrl + t')

    elif 'close tab' in query:

        press_and_release('ctrl + w')

    elif 'new window' in query:

        press_and_release('ctrl + n')

    elif 'history' in query:

        press_and_release('ctrl + h')

    elif 'download' in query:

        press_and_release('ctrl + j')

    elif 'bookmark' in query:

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

    elif open in query:

        name = query.replace("open ","")

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

def YouTubeAuto(command):

    query = str(command)

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

    elif 'increase' in query:

        press_and_release('SHIFT + .')

    elif 'decrease' in query:

        press_and_release('SHIFT + ,')

    elif 'previous' in query:

        press_and_release('SHIFT + p')

    elif 'next' in query:

        press_and_release('SHIFT + n')
    
    elif 'search' in query:

        click(x=667, y=146)

        Speak("What To Search Sir ?")

        search = TakeCommand()

        write(search)

        sleep(0.8)

        press('enter')

    elif 'mute' in query:

        press('m')

    elif 'unmute' in query:

        press('m')

    elif 'my channel' in query:

        web.open("https://www.youtube.com/channel/UC7A5u12yVIZaCO_uXnNhc5g")

    else:
        Speak("No Command Found!")

def WindiowsAuto(command):

    query = str(command)

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

    else:
        Speak("Sorry , No Command Found!")

def GoogleMaps(Place):

    Url_Place = "https://www.google.com/maps/place/" + str(Place)

    geolocator = Nominatim(user_agent="myGeocoder")

    location = geolocator.geocode(Place , addressdetails= True)

    target_latlon = location.latitude , location.longitude

    web.open(url=Url_Place)

    location = location.raw['address']

    target = {'city' : location.get('city',''),
                'state' : location.get('state',''),
                'country' : location.get('country','')}

    current_loca = geocoder.ip('me')

    current_latlon = current_loca.latlng

    distance = str(great_circle(current_latlon,target_latlon))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)


    Speak(target)
    Speak(f"Sir , {Place} iS {distance} Kilometre Away From Your Location . ")

def OnlinClass(Subject):

    Speak("Joining The Class Sir .")

    if 'science' in Subject:

        from DataBase.OnlineClasses.Links import Science

        Link = Science()

        web.open(Link)


        click(x=773, y=511)

        Speak("Class Joined Sir .")

    elif 'mathematics' in Subject:

        from DataBase.OnlineClasses.Links import Maths

        Link = Maths()

        web.open(Link)


        click(x=773, y=511)


        Speak("Class Joined Sir .")

    elif 'social' in Subject:

        from DataBase.OnlineClasses.Links import sst

        Link = sst()

        web.open(Link)


        click(x=773, y=511)

        Speak("Class Joined Sir .")

    elif 'hindi' in Subject:

        from DataBase.OnlineClasses.Links import Hindi

        Link = Hindi()

        web.open(Link)


        click(x=773, y=511)

        Speak("Class Joined Sir .")

    elif 'english' in Subject:

        from DataBase.OnlineClasses.Links import English

        Link = English()

        web.open(Link)

        click(x=773, y=511)

        Speak("Class Joined Sir .")

def Notepad():

    Speak("Tell Me The Query .")
    Speak("I Am Ready To Write .")

    writes = TakeCommand()

    time = datetime.now().strftime("%H:%M")

    filename = str(time).replace(":","-") + "-note.txt"

    with open(filename,"w") as file:

        file.write(writes)

    path_1 = "D:\\Mission J.R.V.I.S\\" + str(filename)

    path_2 = "D:\\Mission J.R.V.I.S\\MainDisk\\Documents\\notepad files\\" + str(filename)

    os.rename(path_1,path_2)

    os.startfile(path_2)

def CloseNotepad():

    os.system("TASKKILL /F /im Notepad.exe")

def TimeTable():

    Speak("Checking....")

    from DataBase.TimeTable.TimeTable import Time

    value = Time()

    Noti = notify()

    Noti.title = "TimeTable"

    Noti.message = str(value)

    Noti.send()

    Speak("AnyThing Else Sir ??")

def window():
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")
    speak('switching the window. sir,')

def GoogleSearch(term):
    query = term.replace("jarvis","")
    query = query.replace("what is","")
    query = query.replace("how to","")
    query = query.replace("what is","")
    query = query.replace(" ","")
    query = query.replace("what do you mean by","")

    writeab = str(query)

    oooooo = open('E:\\Mission J.A.R.V.I.S\\Part 2\\MainDisk\\Documents\\alarm files\\Data.text','a')
    oooooo.write(writeab)
    oooooo.close()

    Query = str(term)

    pywhatkit.search(Query)

    os.startfile('E:\\Mission J.A.R.V.I.S\\Part 2\\DataBase\\ExtraPro\\start.py')

    if 'how to' in Query:

        max_result = 1

        how_to_func = search_wikihow(query=Query,max_results=max_result)

        assert len(how_to_func) == 1

        how_to_func[0].print()

        Speak(how_to_func[0].summary)

    else:

        search = wikipedia.summary(Query,2)

        Speak(f": According To Your Search : {search}")

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    Speak("This Is What I Found For Your Search .")
    pywhatkit.playonyt(term)
    Speak("This May Also Help You Sir .")

def Alarm(query):

    TimeHere = open('E:\\Mission J.A.R.V.I.S\\Part 2\\Data.txt','a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("E:\\Mission J.A.R.V.I.S\\Part 2\\DataBase\\ExtraPro\\Alarm.py")

def DownloadYouTube():
    from time import sleep

    import pyperclip
    from pyautogui import click, hotkey
    from pytube import YouTube

    sleep(2)
    click(x=942,y=59)
    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value) # Important 

    def Download(link):


        url = YouTube(link)


        video = url.streams.first()


        video.download('E:\\Mission J.A.R.V.I.S\\Part 2\\DataBase\\YouTube\\')


    Download(Link)


    Speak("Done Sir , I Have Downloaded The Video .")

    Speak("You Can Go And Check It Out.")


    os.startfile('E:\\Mission J.A.R.V.I.S\\Part 2\\DataBase\\YouTube\\')

def SpeedTest():

    os.startfile("E:\\Mission J.A.R.V.I.S\\Part 2\\DataBase\\Gui Programs\\SpeedTestGui.py")

def DateConverter(Query):

    Date = Query.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")

    return str(Date)

def My_Location():

    op = "https://www.google.com/maps/place/" + str()

    Speak("Checking....")

    web.open(op)

    ip_add = requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_q = requests.get(url)

    geo_d = geo_q.json()

    state = geo_d['city']

    country = geo_d['country']

    Speak(f"Sir , You Are Now In {state , country} .")

def WolfRam(Query):

    api_key = "YEG38R-J9Y375Q9UJ"

    requester = wolframalpha.Client(api_key)

    requested = requester.query(Query)

    try:
        answer = next(requested.results).text
    
        return answer

    except:

        Speak("unable to answer sir,")
        
def calculator(Query):

    term = str(Query)

    term = term.replace("jarvis","")
    term = term.replace("into","*")
    term = term.replace("plus","+")
    term = term.replace("minus","-")
    term = term.replace("divide","/")
    term = term.replace("persontage","%")

    final = str(term)

    try:

       result = WolfRam(final)
       Speak(f"{result}")

       
    except:

        Speak("unable to answer sir,")

def temp (Query):

    term = str(Query)

    term = term.replace("jarvis" ,"")
    term = term.replace("temperature", "")
    term = term.replace("what is the temperature", "")

    temp_Query = str(term)
    
    if 'out side' in temp_Query:

        var1 = "temperature in Delhi"
         
        answer = WolfRam(var1)

        Speak(f"{var1} is {answer} .")

    else:
        var2 = "temperature in" + temp_Query

        answ = WolfRam(var2)

        Speak(f"{var2} is {answ} . ")

 
    

    
    

