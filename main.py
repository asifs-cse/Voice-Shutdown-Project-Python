import pyttsx3
import speech_recognition as sr
import os
def take_comments():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio)
            print("the query is printed= '", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
        import time
        time.sleep(2)
        return Query
def Speak(audio):
        engine = pyttsx3.init()
        engine.say(audio)
        engine.runAndWait()
Speak("Do you want to shuddown your computer sir?")
while True:
    command = take_comments()
    if "no not now" in command:
        Speak("Thank you sir, i will not shutdown your computer!")
        break
    if "yes" in command:
        Speak("Shutting the computer")
        os.system("shutdown /s /t 30")
        break
    Speak("Say that again sir")