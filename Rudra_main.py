import cv2
import os
from threading import Thread
import pyttsx3
import speech_recognition as sr
import webbrowser
import requests
from bs4 import BeautifulSoup
import datetime
import random
from pygame import mixer
from plyer import notification
import pyautogui
import GreetMe
import game
from AppOpener import open, close

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 200)

'''for i in range(3):
    a = input("Enter Password to open Rudra :- ")
    pw_file = open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if a == pw:
        GreetMe.greetMe()
        break
    elif i == 2 and a != pw:
        exit()
    elif a != pw:
        print("Try Again")'''
GreetMe.greetMe()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 0.8
        r.energy_threshold = 1000  # Adjust this value as needed
        audio = r.listen(source, timeout=9)
    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Please try again.")
        return "None"
    except sr.RequestError:
        print("Sorry, I am facing some technical issues. Please try again later.")
        return "None"

def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

def play_video():
    video = cv2.VideoCapture('animation.mp4')
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    cv2.namedWindow('RUDRA', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('RUDRA', cv2.WND_PROP_TOPMOST, 2)

    background = cv2.imread('bg.jpg')
    if background is None:
        print("Error: Could not load background image.")
        video.release()
        cv2.destroyAllWindows()
        return

    desired_width = 380
    desired_height = 220

    while True:
        ret, frame = video.read()

        if not ret:
            video = cv2.VideoCapture('animation.mp4')
            continue

        background = cv2.resize(background, (desired_width, desired_height))
        resized_frame = cv2.resize(frame, (desired_width, desired_height))
        background[:] = resized_frame

        cv2.imshow('RUDRA', background)
        cv2.setWindowProperty('RUDRA', cv2.WND_PROP_TOPMOST, 2) 

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

def main():
    video_thread = Thread(target=play_video)
    video_thread.start()

    while True:
        query = takecommand().lower()

        if "go to sleep" in query:
            speak("Ok sir, You can call me anytime")
            break
        elif "hello" in query:
            speak("Hello sir, how are you ?")
        elif "i am fine" in query:
            speak("that's great, sir")
        elif "how are you" in query:
            speak("Perfect, sir")
        elif "thank you" in query:
            speak("you are welcome, sir")
        elif "google" in query:
            from SearchNow import searchGoogle
            searchGoogle(query)
        elif "youtube" in query:
            from SearchNow import searchYoutube
            searchYoutube(query)
        elif "wikipedia" in query:
            from SearchNow import searchWikipedia
            searchWikipedia(query)
        elif "temperature" in query:
            search = "temperature in delhi"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current{search} is {temp}")
        elif "weather" in query:
            search = "temperature in delhi"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current{search} is {temp}")
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")
        elif "finally sleep" in query:
            speak("Going to sleep, sir")
            exit()
        elif "open" in query:
            app_name = query.replace("open ","")
            open(app_name, match_closest=True)
        elif "close" in query:
            app_name = query.replace("close ","")
            close(app_name, match_closest=True, output=False)
        elif "set an alarm" in query:
            print("input time example:- 10 and 10 and 10")
            speak("Set the time")
            a = input("Please tell the time :- ")
            alarm(a)
            speak("Done, sir")
        elif "stop" in query:
            pyautogui.press("k")
            speak("video paused")
        elif "mute" in query:
            pyautogui.press("m")
            speak("video muted")
        elif "volume up" in query:
            from keyboard import volumeup
            speak("Turning volume up, sir")
            volumeup()
        elif "volume down" in query:
            from keyboard import volumedown
            speak("Turning volume down, sir")
            volumedown()
        elif "remember that" in query:
            rememberMessage = query.replace("remember that", "")
            rememberMessage = query.replace("Rudra", "")
            speak("You told me to" + rememberMessage)
            remember = open("Remember.txt", "a")
            remember.write(rememberMessage)
            remember.close()
        elif "what do you remember" in query:
            remember = open("Remember.txt", "r")
            speak("You told me to" + remember.read())
        elif "tired" in query:
            speak("Playing your favourite songs, sir")
            a = (1, 2, 3)  # You can choose any number of songs (I have only chosen 3)
            b = random.choice(a)
            if b == 1:
                webbrowser.open("https://www.youtube.com/watch?v=dCmp56tSSmA&ab_channel=DiljitDosanjh")
            elif b == 2:
                webbrowser.open("https://www.youtube.com/watch?v=rfTgO9rpqck")
            else:
                webbrowser.open("https://www.youtube.com/watch?v=jLNrvmXboj8")
        elif "news" in query:
            from NewsRead import latestnews
            latestnews()
        elif "calculate" in query:
            from Calculatenumbers import WolfRamAlpha
            from Calculatenumbers import Calc
            query = query.replace("calculate", "")
            query = query.replace("Rudra", "")
            Calc(query)
        elif "whatsapp" in query:
            from Whatsapp import sendMessage
            sendMessage()
        elif "shutdown the system" in query:
            speak("Are You sure you want to shutdown")
            shutdown = None
            shutdown = input("Do you wish to shutdown your computer? (yes/no)")
            if shutdown == "yes":
                os.system("shutdown /s /t 1")
            elif shutdown == "no":
                break
        elif "change password" in query:
            speak("What's the new password")
            new_pw = input("Enter the new password\n")
            new_password = open("password.txt","w")
            new_password.write(new_pw)
            new_password.close()
            speak("Done sir")
            speak(f"Your new password is{new_pw}")

        elif "schedule my day" in query:
            tasks = [] #Empty list 
            speak("Do you want to clear old tasks (Plz speak YES or NO)")
            query = takecommand().lower()
            if "yes" in query:
                file = open("tasks.txt","w")
                file.write(f"")
                file.close()
                no_tasks = int(input("Enter the no. of tasks :- "))
                i = 0
                for i in range(no_tasks):
                    tasks.append(input("Enter the task :- "))
                    file = open("tasks.txt","a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()
            elif "no" in query:
                i = 0
                no_tasks = int(input("Enter the no. of tasks :- "))
                for i in range(no_tasks):
                    tasks.append(input("Enter the task :- "))
                    file = open("tasks.txt","a")
                    file.write(f"{i}. {tasks[i]}\n")
                    file.close()
        elif "show my schedule" in query:
            file = open("tasks.txt","r")
            content = file.read()
            file.close()
            mixer.init()
            mixer.music.load("notification.mp3")
            mixer.music.play()
            notification.notify(
            title = "My schedule :-",
            message = content,
            timeout = 15
            )
        elif "open" in query:
                #EASY METHOD
            query = query.replace("open","")
            query = query.replace("Rudra","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")
        elif "play the game" in query:
            game.game_play()
        elif "screenshot" in query:
            import pyautogui #pip install pyautogui
            im = pyautogui.screenshot()
            im.save("ss.jpg")
        elif "click my photo" in query:
            pyautogui.press("super")
            pyautogui.typewrite("camera")
            pyautogui.press("enter")
            pyautogui.sleep(4)
            speak("SMILE")
            pyautogui.press("enter")
        elif "translate" in query:
            from Translator import translategl
            translategl()
    video_thread.join()

if __name__ == "__main__":
    main()