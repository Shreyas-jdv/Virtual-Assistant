import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import pywhatkit
import pygeoip
import pyautogui
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

# ----------------------------------------------------------------------------------------------------------------------
"""Subprocess:- This module is used for getting system subprocess details which are used in various commands i.e 
                Shutdown, Sleep, etc. This module comes buit-in with Python. 

Wolframalpha:- It is used to compute expert-level answers using Wolfram’s algorithms, knowledgebase and AI technology. 
               To install this module type the below command in the terminal.

                                      ( pip install wolframaplha )

Pyttsx3:- This module is used for conversion of text to speech in a program it works offline. 
          To install this module type the below command in the terminal.
                                      ( pip install pyttsx3 )

Tkinter:- This module is used for building GUI and comes inbuit with Python. 
          This module comes buit-in with Python.

Wikipedia:- As we all know Wikipedia is a great source of knowledge just like GeeksforGeeks we have used Wikipedia 
            module to get information from Wikipedia or to perform Wikipedia search. 
            To install this module type the below command in the terminal.
                                      ( pip install wikipedia )

Speech Recognition:- Since we’re building an Application of voice assistant, one of the most important things in this 
                     is that your assistant recognizes your voice (means what you want to say/ ask).
                     To install this module type the below command in the terminal.
                                      ( pip install SpeechRecognition )

Web browser:- To perform Web Search. 
              This module comes buit-in with Python.

Ecapture:- To capture images from your Camera.
           To install this module type the below command in the terminal.
                                      ( pip install ecapture )

Pyjokes:- Pyjokes is used for collection Python Jokes over the Internet. 
          To install this module type the below command in the terminal.
                                      ( pip install pyjokes )

Datetime:- Date and Time is used to showing Date and Time. 
           This module comes built-int with Python.

Twilio:- Twilio is used for making call and messages. 
         To install this module type the below command in the terminal.
                                      ( pip install twilio )
                                      
Requests: Requests is used for making GET and POST requests. 
          To install this module type the below command in the terminal.
                                      ( pip install requests )

BeautifulSoup: Beautiful Soup is a library that makes it easy to scrape information from web pages. 
          To install this module type the below command in the terminal.

"""
# ----------------------------------------------------------------------------------------------------------------------

"""
Unused modules:
tkinter
random
operator
feedparser
shutil
progress- clint.textui
beautifulSoup- bs4
win32com.client

Non working Functions:
 


tasks left to do:
automate email,
set reminder, stopwatch
set alarm
Greet user
Launch applications/softwares
Open any website
Tells about weather of any city
Open location of any place plus tells the distance between your place and queried place
Tells your current system status (RAM Usage, battery health, CPU usage)
Tells about your upcoming events (Google Calendar)
Send email (with subject and content)
Calculate any mathematical expression (example: Jarvis, calculate x + 135 - 234 = 345)
Answer any generic question (via Wolframalpha)
Take important note in notepad
Has a cool Graphical User Interface
https://flightaware.com/live/map  : tracks live flights

"""

"""
Now we will set our engine to Pyttsx3 which is used for text to speech in Python and sapi5 is
Microsoft speech application platform interface we will be using this for 
text to speech function.
"""
listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

wb.register('chrome', None)
wb.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe")
"""
voice Id = “0” for Male voice
voice Id = “1” for Female voice 
"""


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")


def usrname():
    speak("How may I Help you?")
    """
    speak("What is your name?")
    uname = takeCommand()
    speak("Welcome")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    #" print("anything".center(columns)) " to place it in centre
    print("=============================================================================================================")
    print("Welcome", uname)
    print("=============================================================================================================")
    """


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("...")
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("listening...")
        # query = r.recognize_google(audio, language='en-in')
        query = r.recognize_google(audio)
        print(f" - {query} -\n")

    except Exception as e:
        print(e)
        # print("Unable to Recognize your voice.")
        # speak("Sir, I am having difficulty hearing you, please speak up ")
        # speak("Sir,")
        return "None"
    return query


# ====================================================================================================================================================

if __name__ == '__main__':
    clear = lambda: os.system('cls')  # This Function will clean any command before execution of this python file
    clear()
    wishMe()
    usrname()

    while True:
        query = takeCommand().lower()
    # All the commands said by user will be stored here in 'query' and will be converted to
    # lower case for easily recognition of command

        # search/ play functions
        if "who is" in query:
            person = query.replace('who is ', '')
            if person:
                speak("Searching for" + person)
                info = wikipedia.summary(person, 10)
                print(info)
                speak(info)
            else:
                speak("Sorry sir, I don't know that, Please try again")

        elif "search" in query:
            info = query.replace("search", "")
            speak('searching' + info)
            print('searching' + info)
            wb.open('https://www.google.com/search?q=' + info)

        elif "find information on" in query:
            info = query.replace("find information on", "")
            speak('searching' + info)
            print('searching' + info)
            wb.open('https://www.google.com/search?q=' + info)

        elif "play" in query:
            song = query.replace('play', '')
            speak('playing' + song + 'on youtube')
            pywhatkit.playonyt(song)
            exit()

        # maps related functions
        elif "locate" in query:
            # 3.1 locate cities, mounments, on google earth
            location = query.replace("locate", "")
            speak("Locating" + location)
            wb.open("https://earth.google.com/web/search/" + location)

        elif "find" in query:
            # 3.2 locate places nearby on google maps
            location = query.replace("find", "")
            speak("finding" + location)
            wb.open("https://www.google.com/maps/search/" + location)

        # browser related functions
        elif 'open google chrome' in query or "google chrome" in query or "open chrome" in query or "open google" in query or "google" in query or "chrome" in query:
            # 4.1 opens google chrome browser app
            speak("Here you go to Google Chrome\n")
            wb.open("C:\Program Files\Google\Chrome\Application\chrome.exe")

        elif 'open opera' in query or "opera" in query or "opera browser" in query or "open opera browser" in query:
            speak("Here you go to Opera Gx Browser\n ")
            codePath = r"C:\Users\Lenovo\AppData\Local\Programs\Opera GX\launcher.exe"
            os.startfile(codePath)

        elif 'open tor' in query or "tor browser" in query or "open private browsing" in query:
            # 4.3 opens tor browser
            speak("Here you go to tor browser\n")
            codePath = r"D:\Shreyas\My needs\Tor Browser\Browser\firefox.exe"
            os.startfile(codePath)

        # meetings related functions
        elif "open zoom" in query or "zoom" in query or "open zoom meetings" in query or "zoom meeting" in query:
            # 5.1 opens Zoom meetings
            speak("Here you go to Zoom Meetings\n")
            codePath = r"C:\Users\Lenovo\AppData\Roaming\Zoom\bin\Zoom.exe"
            os.startfile(codePath)

        # website related functions
        elif "open youtube" in query or "youtube" in query:  # 6.1 opens youtube
            speak("Here you go to Youtube\n")
            wb.open("https://www.youtube.com/")

        elif "open stock market" in query or "open my portfolio" in query or "portfolio" in query \
                or "stock market" in query:
            # 6.2 opens  my stock market analysis necessary websites
            speak("Here you go to your stocks portfolio \n")
            wb.open("https://www.moneycontrol.com/")
            wb.open("https://www.tickertape.in/")
            wb.open("https://in.investing.com/")
            wb.open("https://www.screener.in/")

        elif "check bitcoin" in query or "bitcoin" in query:
            speak("here you go to explore bitcoin")
            wb.open("https://www.livecoinwatch.com/price/Bitcoin-BTC")
            time.sleep(10)

        # social media sites functions
        elif "open facebook" in query or "facebook" in query:  # 6.3.1 opens facebook
            speak("Here you go to Facebook\n")
            wb.open("https://www.facebook.com/")

        elif "open instagram" in query or "instagram" in query:  # 6.3.2 opens instagram
            speak("Here you go to Instagram \n")
            wb.open("https://www.instagram.com/")

        # mailing sites functions
        elif "open gmail" in query or "open my mail" in query or "gmail" in query:  # 6.4.1 opens gmail
            speak("Here you go to gmail\n")
            wb.open("https://mail.google.com/mail/u/0/#inbox")

        # random websites
        elif "get me lyrics" in query or "lyrics" in query or "I want some idea for lyrics" in query:  # 6.5.1
            speak("Here you go to get some lyrics\n")
            wb.open("https://deepbeat.org/")
            wb.open("https://creators.aiva.ai/")

        elif "animate face" in query or "animate photo" in query:  # 6.5.2
            speak("Here you go for seeing live reactions\n")
            wb.open("https://www.myheritage.com/deep-nostalgia")

        elif "edit photos" in query or "edit pics" in query or "edit photo" in query:  # 6.5.3
            speak("Here you go to edit pics\n")
            wb.open("https://hotpot.ai/")
            wb.open("https://icons8.com/upscaler")

        elif "non existing people" in query or "unknown people" in query:  # 6.5.4
            speak("Here you go to find some unknown people\n")
            wb.open("https://thispersondoesnotexist.com/")

        elif "story" in query or "write a story" in query or "complete a story" in query:  # 6.5.5
            speak("Here you go to write a story\n")
            wb.open("https://app.inferkit.com/generate")

        elif "open stackoverflow" in query or "stack overflow" in query:  # 6.5.6
            speak("Here you go to Stack Over flow k,")
            wb.open("https://stackoverflow.com/")

        # applications related functions

        # messenger app functions
        elif "open whatsapp" in query or "open whatsup" in query or "whats app" in query:  # 7.1.1
            speak("opening whatsapp messenger")
            power = r"C:\Users\Lenovo\AppData\Local\WhatsApp\WhatsApp.exe"
            os.startfile(power)

        elif "open telegram" in query or "telegram" in query or "teli gram" in query:  # 7.1.2
            speak("opening telegram messenger")
            power = r"C:\Users\Lenovo\AppData\Roaming\Telegram Desktop\Telegram.exe"
            os.startfile(power)

        # microsoft office functions
        elif "open power point presentation" in query or "open PPT" in query or "power point presentation" in query or \
                "open powerpoint presentation" in query or "open microsoft powerpoint" in query or \
                "open microsoft power point" in query or \
                "open powerpoint" in query or "power point= " in query:  # 7.2.1
            speak("opening  Microsoft Power Point presentation")
            power = r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
            os.startfile(power)

        elif "open word" in query or "open microsoft word" in query or "word" in query:  # 7.2.2
            speak("opening Microsoft Word")
            power = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
            os.startfile(power)

        elif "open Excel" in query or "microsoft excel" in query or "ek sell" in query or "excel" in query:  # 7.2.3
            speak("opening Microsoft Excel")
            power = r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
            os.startfile(power)

        elif "open settings" in query or "settings" in query:  # not working
            speak("opening settings")
            power = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
            os.startfile(power)

        elif 'open bluestack' in query:
            power = r"C:\Program Files\BlueStacks\Bluestacks.exe"
            os.startfile(power)

        elif 'open snipping tool' in query:
            speak("Switching")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            power = r"% windir%\system32\SnippingTool.exe"
            os.startfile(power)

        elif "whatsapp message" in query or "send whatsapp message" in query:
            speak("Please Enter the Phone ,Number, don't forget to add the country code.")
            phno = input("Phone Number: ")
            speak("Please Enter the Message you want to send.")
            Message = input("Message: ")
            speak("Enter the time at which the message is to be sent.")
            print(
                "\n 1 PM = 13 \n 2 PM = 14 \n 3 PM = 15 \n 4 PM = 16 \n 5 PM = 17 \n 6 PM = 18 \n"
                " 7 PM = 19 \n 8 PM = 20 \n 9 PM = 21 \n 10 PM = 22 \n 11 PM = 23 \n 12 PM = 00")
            hour = int(input("Hours: "))
            minute = int(input("Minutes: "))
            speak("Sending message")
            pywhatkit.sendwhatmsg(phno, Message, hour, minute)
            # pywhatkit.sendwhatmsg_to_group( phno, Message, hour, minute)
            # pywhatkit.sendwhatmsg_instantly( phno, Message, hour, minute)
            # pywhatkit.send_mail( phno, Message, hour, minute)
            speak("Message sent.")

        elif 'tel news' in query or "tell news" in query or "news" in query or \
                "what's the news" in query or "daily news" in query:

            speak(" Sir, Do you want to hear Economic News ,or general news ")
            choice = takeCommand()
            if choice in ('economic' or 'anomic'):
                speak("okay sir, telling economic news")


                def NewsFromBBC():

                    query_params = {
                        "source": "bbc-news",
                        "sortBy": "top",
                        "apiKey": "92218b33c55a4f388dea2f32b6bcb973"
                    }
                    main_url = "https://newsapi.org/v2/top-headlines?country=in&category=business"

                    res = requests.get(main_url, params=query_params)
                    open_bbc_page = res.json()
                    article = open_bbc_page["articles"]
                    results = []

                    for ar in article:
                        results.append(ar["title"])

                    for i in range(len(results)):
                        print(i + 1, results[i])

                    from win32com.client import Dispatch
                    speak = Dispatch("SAPI.Spvoice")
                    speak.Speak(results)


                if __name__ == '__main__':
                    NewsFromBBC()
                    speak("")
                    speak("Sir, do you want to read it in detail")
                    choice = takeCommand()
                    if choice in 'yes':
                        speak("okay sir, Here you go to the website\n")
                        wb.open("https://economictimes.indiatimes.com/")
                    else:
                        speak("okay sir, call me if you need me.")

            elif choice in 'general':
                speak("okay sir, telling general news")


                def NewsFromBBC():

                    query_params = {
                        "source": "bbc-news",
                        "sortBy": "top",
                        "apiKey": "92218b33c55a4f388dea2f32b6bcb973"
                    }
                    main_url = "https://newsapi.org/v2/top-headlines?country=in"

                    res = requests.get(main_url, params=query_params)
                    open_bbc_page = res.json()
                    article = open_bbc_page["articles"]
                    results = []

                    for ar in article:
                        results.append(ar["title"])

                    for i in range(len(results)):
                        print(i + 1, results[i])

                    from win32com.client import Dispatch
                    speak = Dispatch("SAPI.Spvoice")
                    speak.Speak(results)


                if __name__ == '__main__':
                    # function call
                    NewsFromBBC()

                    speak("Sir, do you want to read it in detail")
                    choice = takeCommand()
                    if choice in 'yes':
                        speak("okay sir, Here you go to the website\n")
                        wb.open("https://timesofindia.indiatimes.com/india")
                    else:
                        speak("okay sir, call me if you need me.")

            else:
                speak("Sorry sir, I did not understand that, please try again")
                print(" Please speak 'Tell news'")

        elif "take screenshot" in query or "take a screenshot" in query or "capture the screen" in query:
            speak("By what name do you want to save the screenshot?")
            name = takeCommand()
            speak("Alright sir, taking the screenshot")
            img = pyautogui.screenshot()
            name = f"{name}.png"
            img.save(name)
            speak("The screenshot has been succesfully captured")

        elif "switch the window" in query or "switch window" in query or "switch" in query or "which" \
                in query or "window" in query:
            speak("Switching")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "paste" in query or "paste it" in query:
            speak("pasting")
            pyautogui.keyDown("ctrl")
            pyautogui.press("v")
            time.sleep(1)
            pyautogui.keyUp("ctrl")

        elif "scroll down" in query or "down" in query or "move down" in query:
            pyautogui.scroll(-400)
            speak("scrolled")

        elif "scroll back " in query or "back" in query or "move up" in query or "scroll up" \
                in query or "roll up" in query:
            pyautogui.scroll(400)
            speak("scrolled")

        elif "whats my ip address" in query or "my ip address" in query or "my ip" in query:
            ip = requests.get('https://api.ipify.org').text
            print(ip)
            speak(f"Your ip address is {ip}")
            time.sleep(2)

        elif "get this ip address" in query or "get ip address" in query:  # 25
            gip = pygeoip.GeoIP("GeoLiteCity.dat")
            speak("Please enter the  IP address. don't leave any spaces while entering the I P Address")
            ipadd = (input("Enter IP Address :"))
            speak("Getting information")
            res = gip.record_by_addr(ipadd)

            for key, val in res.items():
                results = '%s : %s' % (key, val)
                print(results)
                speak(results)

            lat = res["latitude"]
            lon = res["longitude"]

            data = '%s, %s' % (lat, lon)

            speak("Sir, do you want me to locate it")
            print("\n \n Should I locate it?")
            speak("")
            choice = takeCommand()
            if choice in ('yes' or 'yeah' or 'sure' or 'yes sure' or 'obviously'):
                speak("Okay sir, locating the ip address on map \n")
                wb.open("https://earth.google.com/web/search/" + data)
                time.sleep(10)
            elif choice in ('no' or 'no way' or 'crazy'):
                speak("okay sir, fine!")
            else:
                pass

        elif "what's the time" in query or "what is the time" in query or "time" in query:  # 26
            e = datetime.datetime.now()
            print(e.strftime("%I:%M %p \n %a, %b %d, %Y"))
            speak(e.strftime("sir, the time is %I %M %p"))
            speak(e.strftime("the date is  %b %d %Y"))
            speak("Have a great day!")

        elif "calculate" in query or "open simple calculator" in query:
            # main python program
            response = ['here you go to my smart calculator function',
                        'My name is DONNY, you are using my smart calculator function',
                        'Thanks for using me ', 'Sorry ,I dont know that one']
            # fetching tokens from the text command


            def extract_from_text(text):
                l = []
                for t in text.split(' '):
                    try:
                        l.append(float(t))
                    except ValueError:
                        pass
                return l


            # calculating LCM


            def lcm(a, b):
                L = a if a > b else b
                while L <= a * b:
                    if L % a == 0 and L % b == 0:
                        return L
                    L += 1


            # calculating HCF


            def hcf(a, b):
                H = a if a < b else b
                while H >= 1:
                    if a % H == 0 and b % H == 0:
                        return H
                    H -= 1


            # Addition


            def add(a, b):
                return a + b


            # Subtraction


            def sub(a, b):
                return a - b


            # Multiplication


            def mul(a, b):
                return a * b


            # Division


            def div(a, b):
                return a / b


            # Remainder


            def mod(a, b):
                return a % b


            # Response to command
            # printing - "Thanks for enjoy with me" on exit


            def end():
                speak(response[2])
                speak('press enter key to exit')
                input('')
                exit()


            def myname():
                speak(response[1])


            def sorry():
                speak(response[3])


            # Operations - performed on the basis of text tokens
            operations = {'ADD': add, 'PLUS': add, 'SUM': add, 'ADDITION': add,
                          'SUB': sub, 'SUBTRACT': sub, 'MINUS': sub, 'DIFFERENCE': sub,
                          'LCM': lcm, 'HCF': hcf,
                          'PRODUCT': mul, 'MULTIPLY': mul, 'MULTIPLICATION': mul,
                          'DIVISION': div, 'DIVIDE': div,
                          'MOD': mod, 'REMANDER': mod, 'REMAINDER': mod, 'MODULAS': mod}

            # commands
            commands = {'NAME': myname, 'EXIT': end, 'END': end, 'CLOSE': end, 'STOP': end, '': end}

            speak('--------------' + response[0] + '------------')
            # print('--------------' + response[1] + '--------------------')

            while True:
                print()
                speak("Please speak what should I to calculate")
                text = takeCommand()
                for word in text.split(' '):
                    if word.upper() in operations.keys():
                        try:
                            l = extract_from_text(text)
                            r = operations[word.upper()](l[0], l[1])
                            speak("the answer is ")
                            speak(r)
                            print(r)
                            time.sleep(3)
                        except:
                            speak('I did not get that one, please speak again !!')
                        finally:
                            break
                    elif word.upper() in commands.keys():
                        commands[word.upper()]()
                        break
                    else:
                        sorry()

        # ===========================================================================================================================================

        elif "send a mail" in query or "send e mail" in query or "mail" in query:
            # needs permission from google account
            sender_email = input("Sender's Email: ")
            sender_password = input("Password: ")

            try:
                speak("Whom do you want to email sir ?")
                receiver_email = input("Email To: ")
                if receiver_email:

                    speak("What is the subject sir ?")
                    subject = input("Subject: ")
                    speak("What should I say?")
                    message = input("Message: ")
                    msg = 'Subject: {}\n\n{}'.format(subject, message)
                    pywhatkit.send_mail(sender_email, sender_password, subject, msg, receiver_email)
                    speak("Email has been successfully sent")
                    time.sleep(2)

                else:
                    speak("I coudn't find the requested person's email in my database."
                          " Please try again with a different name")
            except:
                speak("Sorry sir, Couldn't send your mail."
                      " Please try again")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
            if 'fine' in query or "good" in query:
                speak("It's good to know that your fine")

        elif "change your name" in query or "change name" in query:
            speak("My name is DONNY. I am sorry, but I can't change who I am ")
            """
            query = query.replace("change my name to", "")
            ################################################
            assname = takeCommand()
            speak("Thanks for naming me")
            """

        elif "what's your name" in query or "name" in query:
            speak("I go by DONNY. It's a nickname, sort of ")

        elif 'see you later' in query:
            speak("See you!")
            exit()

        elif "bye" in query or "bhai" in query or "stop" in query or "exit" in query or "go away" \
                in query or "fuck off" in query:
            speak("Bye for now, call me when you need something")
            print("Bye! 🙂")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Shreyas Jadhav.")

        elif 'tell me a joke' in query or "tel me a joke" in query or "joke" in query or "tel a joke" in query:
            speak(pyjokes.get_joke())
            print("🙂🙂🙂🙂🙂🙂🙂")

        elif "make me happy" in query:
            speak("")

        elif "why you came to world" in query:
            speak("I was created to operate commands and navigate data for you. Thanks to Mister Shreyus Jadhav.")

        elif 'what is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your personal assistant created by Shreyus")

        elif 'reason for you' in query:
            speak("I was created to operate commands and navigate your data by  Mister Shreyus Jadhav")

        elif 'when were you created' in query or 'when were you made' in query:
            speak("I was created on sixteenth may two thousand twenty")

        elif 'change background' in query or "my background" in query or "the background" in query or \
                "background" in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, r"C:\Users\Lenovo\OneDrive\Pictures\Pictures\iron.jpg", 0)
            speak("Background changed succesfully")

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown/p/f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query or "wait" in query:  # check
            speak("for how much time you want to stop DONNY from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "go to sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "lock pc" in query or "lock" in query: # check
            pyautogui.keyDown("windows")
            pyautogui.press("l")
            time.sleep(1)
            pyautogui.keyUp("windows")

        elif "sign off" in query : #not working
            speak("Do you want to switch off laptop, sir")
            choice = takeCommand()
            if "yes" in choice:
                speak("Shutting down laptop ,Sir")
                os.system("shoutdown /s /t 30")
            if "no" in choice:
                speak("okay Sir, thank you")


        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('DONNY.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("opening my Notebook")
            file = open("DONNY.txt", "r")
            print(file.read())
            speak(file.read())

        elif "Donny" in query or "dhoni" in query or "dhani" in query or "doni" in query or \
                "johny" in query or "tony" in query or "jaani" in query:
            speak("Hello Sir! How can I help you")

        elif "weather" in query:  # not working

            # Google Open weather website
            # to get API of Open weather
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            city_name = input("City name : ")
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(
                    current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
                    current_pressure) + "\n humidity (in percentage) = " + str(
                    current_humidiy) + "\n description = " + str(weather_description))

            else:
                speak(" City Not Found ")

        elif "send message " in query:
            # You need to create an account on Twilio to use this service
            account_sid = 'Account Sid key'
            auth_token = 'Auth token'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(body=takeCommand(), from_='Sender No', to='Receiver No')

            print(message.sid)

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you sir")
            # speak(assname)

        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            speak("I'm fine sir, thank you for asking")

        elif "i love you" in query:
            speak("thank you!")

            """
        elif "what is" in query or "who is" in query:   #not working
            # Use the same API key
            # that we have generated earlier
            client = wolframalpha.Client("API_ID")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")
            """

        elif "when will" in query:
            info = query.replace("when will", "")
            speak("Sorry, I don't know that one.I can't predict the future")

        elif "hide all files" in query or "hide this folder" in query:
            os.system("attrib +h /s /d")
            speak("Sir, all the files in this folder are now hidden")

        elif "visible" in query or "make files visible" in query:
            os.system("attrib -h /s /d")
            speak("Sir, all the files in this folder are now visible to everyone. "
                  "I hope you are taking this decision in your own peace")

        elif "system information" in query:
            Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
            new = []
            for item in Id:
                new.append(str(item.split("\r")[:-1]))
            for i in new:
                print(i[2:-2])
                speak(i[2:-2])

        elif "call" in query:
            speak("")

        elif "track phone number" in query or "trace phone number" in query:
            speak("Please enter the mobile number with country code")
            number = input("Phone number")
            ch_number = phonenumbers.parse(number, "CH")
            print(geocoder.description_for_number(ch_number, "en"))
            service_number = phonenumbers.parse(number, "RO")
            print(carrier.name_for_number(service_number, "en"))
            time.sleep(1)
            speak(" Sir, Do you want to get information through Truecaller ")
            choice = takeCommand()
            if choice in 'yes':
                speak("okay sir, Here you go to truecaller")
                wb.open('https://www.truecaller.com/search/in/' + number)
                time.sleep(10)
