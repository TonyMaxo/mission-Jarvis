import os
from playsound import playsound
import datetime

extracted_time = open('E:\\Mission J.A.R.V.I.S\\Part 2\\Data.txt','rt')
time = extracted_time.read()
Time = str(time)

delete_time = open("E:\\Mission J.A.R.V.I.S\\Part 2\\Data.txt",'r+')
delete_time.truncate(0)
delete_time.close()

def RingerNow(time):

    time_to_set = str(time)
    time_now = time_to_set.replace("jarvis","")
    time_now = time_now.replace("set alarm for ","")
    time_now = time_now.replace("set ","")
    time_now = time_now.replace("alarm ","")
    time_now = time_now.replace("for ","")
    time_now = time_now.replace(" and ",":")

    Alarm_Time = str(time_now)

    while True:

        current_time = datetime.datetime.now().strftime("%H:%M")

        if current_time == Alarm_Time:
            print("Wake Up Sir , It's Time To Work .")
            playsound("E:\\Mission J.A.R.V.I.S\\Part 2\\DataBase\\Sounds\\1.mp3")
            

        elif current_time>Alarm_Time:
            break

RingerNow(Time)

