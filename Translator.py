from googletrans import Translator
import googletrans
import gtts
import pyttsx3
import speech_recognition
import playsound

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def translategl():
    speak("SURE SIR")
    speak("please select the input and output languages by code from below list")
    print(googletrans.LANGUAGES)
    input_lang = input("Enter the input language code: ")
    output_lang = input("Enter the Output language code: ")
    r = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        print("Speak now")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language=input_lang)
            print("Text:", text)
        except speech_recognition.UnknownValueError:
            print("Sorry, could not understand audio")

    translator = googletrans.Translator()
    translation = translator.translate(text, dest=output_lang)
    print("Translated Text:", translation.text)

    converted_audio = gtts.gTTS(translation.text, lang=output_lang)
    converted_audio.save("hello.mp3")
    playsound.playsound("hello.mp3")
