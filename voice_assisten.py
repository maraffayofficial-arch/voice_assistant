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
            return data

        except sr.UnknownValueError as error:
            print("Could not understand")
            return ""   
        
        except sr.RequestError as error:
            print("Could not understand")
            return ""   


def speechtx(x):
    engine=pyttsx3.init()
    voices=engine.getProperty("voices")
    engine.setProperty("voice",voices[1].id)
    rate=engine.getProperty("rate")
    engine.setProperty("rate",250)
    engine.say(x)
    engine.runAndWait()
# speechtx("hello, I am Nobel! how can i help you..?")    

if __name__=="__main__":
#    if sptext().lower()=="hey Nobel":
    while True:
        data1= sptext().lower()
        if "your name" in data1:
           name="My name is Nobel"
           speechtx(name)
        elif "who are you" in data1:
            intro="I am Nobel a voice assistant created to help you."
            speechtx(intro)
        elif "how old are you" in data1:
            age="I am 2 years old "
            speechtx(age)
        elif "time" in data1:
            time=datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
        elif "youtube" in data1:
            webbrowser.open("https://www.youtube.com/")
            
        elif "google" in data1:
            webbrowser.open("https://www.google.com/")
        
        elif "instagram" in data1:
            webbrowser.open("https://www.instagram.com/")
        
        
        elif "joke" in data1:
            joke_1=pyjokes.get_joke(language="en",category="neutral")
            speechtx(joke_1)

        elif "exit" in data1:
           speechtx("Thank you! Nobel exiting...")

           break

        
