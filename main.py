import pyttsx3
import speech_recognition
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
from googleapi import google  
import pywhatkit as kit
import sys
import pyjokes
import pyautogui
import time
import requests
import phonenumbers
from phonenumbers import timezone, geocoder, carrier
import qrcode as qr

#jarvis voice 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):

    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecomand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=2, phrase_time_limit=7)
    try:
        print("Recognizing.....")  
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        speak("say that again please.....")
        return "none"
    return query



def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning sir")
    elif hour>12 and hour<18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak("i am jarvis. please tell me how can i help you")

    
def news():
    main_url = ' https://newsapi.org/v2/top-headlines?country=in&apiKey=9163607f98da4a0aa6272b2cb069b152'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day =["first","second","third","fourth","fifth"]
    for ar in articles :
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")


# def trace():
    # number = input("enter your number")
    # phone = phonenumbers.parse(number)
    # time = timezone.time_zones_for_number(phone)
    # carr = carrier.name_for_number(phone,"en")
    # reg = geocoder.description_for_number(phone,"en")
    # print(phone)
    # print(time)
    # print(carr)
    # print(reg)



        
           








if __name__=="__main__":
    wish()
    while True:
    # if 1:
        query = takecomand().lower()

        if "open notepad" in query:
            npath = "C:\Windows\system32\\notepad.exe"
            os.startfile(npath)


        elif "open command prompt" in query:
            os.system('start cmd')


        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitkey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()


        elif "play music" in query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))



        elif "what is my ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip adress is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences =2)
            speak("according to wikipedia")
            speak(results)
            print(results)


       

        
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")

        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com/")
        
        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com/")
        
        elif "open whatsapp " in query:
            webbrowser.open("https://web.whatsapp.com/")
        
        elif 'open google' in query:
            speak("what should i search on google sir\n")
            cm = takecomand().lower()
            webbrowser.open(f"{cm}")
        

        elif "send message" in query:
            speak("what message should i send on whatsapp sir\n")
            msg = takecomand().lower()
            kit.sendwhatmsg_instantly("+917838472048",f"{msg}")


        elif"play a song on youtube" in query:
            speak("which song do you want to listen sir\n")
            playsong = takecomand().lower()
            kit.playonyt(f"{playsong}")

        elif 'what the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")   
            speak(f"Sir, the time is {strTime}")

        elif 'tell me bad word ' in query:
            speak("asshole")
            speak("or gaali du, Sir")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")


        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query 

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takecomand()
            speak("Thanks for naming me")     
 
        
        elif "what is your name" in query:
            speak("my name is jarvis.")
        
 
        elif 'tell me joke' in query:
            speak(pyjokes.get_joke())

        elif "who i am" in query:
            speak("If you talk then definitely your human.")
 
        elif "why you came to world" in query:
            speak("Thanks to Gaurav. further It's a secret")
 
        elif 'open power point presentation' in query:
            speak("opening Power Point presentation")
            power = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office"
            os.startfile(power)
 
        elif 'what is love' in query:
            speak("It is 7th sense that destroy all other senses")
 
        elif "who are you" in query:
            speak("I am your virtual assistant created by roshan raj")
 
        elif 'reason for you created' in query:
            speak("I was created as a Minor project by Roshan Raj ")

        elif 'what is your girlfriend name' in query:
            speak("my girlfriend name is....,siri but please don't tell anyone its a secret ")

        
        elif"no thanks"  in query:
            speak("thanks for using me, have a good day,  sir")
            sys.exit()
        
        elif"swith the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep
            pyautogui.keyUp("alt")

        elif"tell me news" in query:
            speak("please wait, fetching the top headlines news")
            news()

        elif"trace my mobile number" in query:
            speak("please wait enter your mobile number....")
            number = input(" enter your mobile number....")
            phone = phonenumbers.parse(number)
            time = timezone.time_zones_for_number(phone)
            carr = carrier.name_for_number(phone,"en")
            reg = geocoder.description_for_number(phone,"en")
            print(phone)
            print(time)
            print(carr)
            print(reg)
            
        elif"description of my mobile number" in query:
            from truecallerpy import search_phonenumber
            id = "a2i05--eaA2UXkUkfu-sVOrzMCzIpGtH92jn0OmpmOdYthjxzaosVpfZ16kXDefN"
            phone_number = input("enter phone number")
            response = (search_phonenumber(phone_number, "IN", id))
            print(response)
        
            
        elif"secret code" in query:
            speak("Enter Your Message....")
            msg = input("enter your message")
            img = qr.make(msg)
            img.save("qrcode.png")