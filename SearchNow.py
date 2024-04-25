import pyttsx3
import speech_recognition as sr  # Added import statement
import pywhatkit
import wikipedia
import webbrowser

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, timeout=4)
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

def speak(audio):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", 170)
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        query = query.replace("jarvis", "").replace("google search", "").replace("google", "")
        speak("This is what I found on google")
        try:
            pywhatkit.search(query)
            result = wikipedia.summary(query, sentences=1)
            speak(result)
        except wikipedia.DisambiguationError as e:
            result = "Too many matches found. Please be more specific."
            speak(result)
        except wikipedia.PageError as e:
            result = "No information found. Please try again."
            speak(result)

def searchYoutube(query):
    if "youtube" in query:
        if "play" in query:
            query = query.replace("play", "").replace("youtube", "").replace("jarvis", "")
            pywhatkit.playonyt(query)
        elif "search" in query:
            query = query.replace("search", "").replace("youtube", "").replace("jarvis", "")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
        else:
            query = query.replace("youtube search", "").replace("youtube", "").replace("jarvis", "")
            web = "https://www.youtube.com" + query
            webbrowser.open(web)

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia", "").replace("search wikipedia", "").replace("jarvis", "")
        try:
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia..")
            print(results)
            speak(results)
        except wikipedia.DisambiguationError as e:
            result = "Too many matches found. Please be more specific."
            speak(result)
        except wikipedia.PageError as e:
            result = "No information found. Please try again."
            speak(result)

query = takeCommand()

searchGoogle(query)
searchYoutube(query)
searchWikipedia(query)
