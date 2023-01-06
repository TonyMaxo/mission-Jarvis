
import pywhatkit
import wikipedia
from pywikihow import RandomHowTo, search_wikihow
import os
import speech_recognition as sr
import webbrowser as web
import bs4
import pyttsx3
from time import sleep
import requests
import wolframalpha

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
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip
    from time import sleep

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

 
    