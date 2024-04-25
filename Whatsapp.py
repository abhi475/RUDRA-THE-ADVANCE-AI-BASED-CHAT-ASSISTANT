
import pyttsx3
import speech_recognition as sr
import pyautogui
import time

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

# Function to convert text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to recognize voice command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 350
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
        return query
    except Exception as e:
        print(e)
        print("Sorry, I didn't catch that. Could you please repeat?")
        return "None"

# Function to send WhatsApp message
def sendMessage():
    speak("Who do you want to message?")
    recipient = takeCommand()

    speak("What's the message?")
    message = takeCommand()

    if recipient != "None" and message != "None":
        # Open WhatsApp
        pyautogui.hotkey('win', 's')
        time.sleep(1)
        pyautogui.write("WhatsApp")
        pyautogui.press('enter')
        time.sleep(2
                   )  # Waiting for WhatsApp to open

        # Clicking on the search box
        pyautogui.click(x=100, y=100)  # Adjust coordinates according to your screen
        time.sleep(2)

        # Typing recipient name
        pyautogui.write(recipient)
        time.sleep(2)

        # Clicking on the recipient
        pyautogui.click(x=250, y=220)  # Adjust coordinates according to your screen
        time.sleep(2)

        # Typing and sending message
        pyautogui.write(message)
        time.sleep(1)
        pyautogui.press('enter')

        speak("Message sent successfully!")
    else:
        speak("Sorry, I couldn't understand the recipient or the message. Please try again.")

# Main function
if __name__ == "__main__":
    sendMessage()
