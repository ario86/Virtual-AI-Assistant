import speech_recognition as sr
import os

from pyttsx3 import speak


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Go ahead...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio, language='en-in')
            print(f"user said:{command}\n")

        except Exception as e:

            return "None"
        return command


while True:

    wakeUp = takeCommand()
    if "wake up" in wakeUp or "Natasha" in wakeUp:
        os.startfile("C:\\Users\\Aritrajit\\Desktop\\My projects\\New AI\\main.py")

    else:
        pass
