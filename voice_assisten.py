import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pyjokes

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("recognizing....")
            data=recognizer.recognize_google(audio)
            print(data)

        except sr.UnknownValueError as error:
            print("Could not understand")
            # raise error


def speechtx(x):
    engine=pyttsx3.init()
    voices=engine.getProperty("voices")
    engine.setProperty("voice",voices[1].id)
    rate=engine.getProperty("rate")
    engine.setProperty("rate",170)
    engine.say(x)
    engine.runAndWait()
speechtx("hello, I am Nobel! how can i help you..?")

