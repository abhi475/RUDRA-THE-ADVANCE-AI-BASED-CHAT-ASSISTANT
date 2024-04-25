import pyttsx3
import datetime
import intro
import video

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

import datetime

def greetMe():
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))  # Set timezone to IST
    hour = now.hour
    if 0 <= hour < 12:
        greeting = "Good Morning"
    elif 12 <= hour < 17:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    intro.play_sound()
    speak(f"{greeting}, sir. Please tell me, how can I help you?")

