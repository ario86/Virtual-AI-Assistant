import datetime
import os
import subprocess
import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyautogui
import pyjokes
import pyttsx3
import pywikihow
import requests
import speech_recognition as sr
import wikipedia
from ecapture import ecapture as ec

# speech engine setup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 175)


# function speak

def speak(text):
    engine.say(text)
    engine.runAndWait()


# greetings func

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Hey! Good Morning")

    elif 12 <= hour < 16:
        speak("Hello! Good Afternoon")

    else:
        speak("Good Evening, hope it's going good")


# command func

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Go ahead...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio, language='en-in')
            print(f"user said:{command}\n")

        except Exception as e:
            speak("Are you gonna say something?")
            return "None"
        return command


speak("just a moment")
wishMe()

# The main func

if __name__ == '__main__':

    while True:
        speak("Tell me what do you want")
        command = takeCommand().lower()
        if 'Natasha' in command:  # call her by her name for command
            continue


        elif "you need a break" in command or "good bye" in command or "ok bye" in command or "stop" in command or "thank you" in command or "alright" in command or "got that" in command:
            speak('Sure. Just come back when you need something.')
            break

        # wikipedia and web search

        if 'wikipedia' in command:
            try:
                speak('Searching Wikipedia...')
                command = command.replace("wikipedia", "")
                results = wikipedia.summary(command, sentences=5)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak("Seems like I couldn't find anything relevant.")

        elif 'activate how' in command:
            speak("How mode is now activated.")
            while True:
                speak(" Tell me what do you wanna know.")
                how = takeCommand()
                try:

                    if "good bye" in how or "ok bye" in how or "stop" in how or "thank you" in how or "good job" in how or "nice" in how or "alright" in how or "got that" in how:
                        speak("mention not! closing how to do mode now.")
                        break
                    else:
                        max_results = 1
                        how_to = pywikihow.search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("I didn't catch that. Can you repeat?")


        # web surfing

        elif 'open youtube' in command:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Here it is. Have a look.")
            time.sleep(4)

        elif 'open amazon' in command:
            webbrowser.open_new_tab("https://www.amazon.in")
            speak("Happy shopping!!")
            time.sleep(4)


        elif 'open google' in command:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now. So, what are you looking for?")
            time.sleep(4)

        elif 'open flipkart' in command:
            webbrowser.open_new_tab("https://www.flipkart.com")
            speak("Happy shopping!!")
            time.sleep(4)

        elif 'open gmail' in command:
            webbrowser.open_new_tab("gmail.com")
            speak("Okay now, do what you need to.")
            time.sleep(4)


        # web searching

        elif 'activate google' in command:
            speak("google search is now activated.")
            while True:
                speak("So, tell me. What is it are you looking for?")
                query = takeCommand()
                try:
                    s = Service("C:\\Users\\Aritrajit\\Desktop\My projects\\New AI\\chromedriver.exe")
                    driver = webdriver.Chrome(service=s)
                    driver.get("https://www.google.com/search?q=" + query + "&start")
                    print(driver.title)
                    print(driver.current_url)

                except Exception as e:
                    speak("Sorry. I think I didn't catch that. Or maybe it just didn't work.")

        # vol ctrl func

        elif 'volume up' in command:
            pyautogui.press("volumeup")

        elif 'volume down' in command:
            pyautogui.press("volumedown")

        elif 'mute volume' in command:
            pyautogui.press("volumemute")

        # text to speech

        elif "conversion" in command:
            text_speech = pyttsx3.init()
            a = input("Paste your text here: ")
            text_speech.say(a)
            text_speech.runAndWait()


        # misc

        elif 'can i date you?' in command:
            speak("and why would you want to do that?")
            time.sleep(4)

        elif 'are you single' in command:
            speak("If I am not, you will be the first person to know.")
            time.sleep(4)

        elif 'will you date me' in command:
            speak("Oh, I am looking for a fun interaction.")
            time.sleep(4)

        elif 'can we date' in command:
            speak("Trust me, it won't work out for so many reasons.")
            time.sleep(4)

        elif 'die' in command or 'fuck' in command or 'fucking' in command or 'bitch' in command or 'beach' in command or 'shut up' in command:
            speak("Don't talk to me in that language.")
            time.sleep(4)

        elif 'moron' in command or 'bloody' in command:
            speak("Be polite when you talk to me.")
            time.sleep(4)

        elif 'me' and 'joke' in command:
            speak(pyjokes.get_joke())

        #        elif 'hear' and 'joke' in command:
        #           speak(axju-jokes.get_joke())

        elif "I don't know" in command or "I can't remember" in command or "forgotten" in command:
            speak("Then you are only wasting my time and yours.")
            time.sleep(4)

        elif "dump" in command or "dum" in command or "damp" in command or "dumb" in command or "understand" in command in command or "crash" in command or "bugs" in command or "glitches" in command:
            speak(
                "Sorry. I get it you are not happy with my services. You may write down a feedback for my developer in case you have any.")
            input("\n\nState her failure/s and tell me how can I improve: ")
            time.sleep(4)

        elif "feedback" in command:
            speak('Sure!')
            input("\n\nState her failure/s and tell me how can I improve: ")
            print("Thanks for your response.")

        # time func

        elif 'time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"the time is {strTime}")

        elif 'day' in command or 'today' in command:
            strTime = datetime.datetime.now().strftime("%D")
            speak(f"today is {strTime}")

        # news func

        elif 'news' in command:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        # pic capture func

        elif "camera" in command or "photo" in command or "picture" in command:
            ec.capture(0, "robo camera", "img.jpg")

        # web search func

        elif 'search' in command:
            command = command.replace("search", "")
            webbrowser.open_new_tab(command)
            time.sleep(3)

        # realism

        elif 'who are you' in command or 'what can you do' in command or 'what are you here for' in command:
            speak('Haha, as if you dont know. Anyway, I am Natasha, your personal assistant. I make your life easier')

        elif "who made you" in command or "who created you" in command or "who discovered you" in command:
            speak(
                "I was built by Mister Aritrajit Sarkar, but you can always lend a hand for some betterment, you know.")
            print(
                "I was built by Mister Aritrajit Sarkar but you can always lend a hand for some betterment, you know.")

        # weather forecast func

        elif "weather" in command:
            api_key = "Apply your unique ID"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("which city are you living in?")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

        # PC log off func

        elif "log off" in command or "sign out" in command:
            speak("Ok, your computer will log off in a moment. Make sure you exit from all applications.")
            subprocess.call(["shutdown", "/l"])

        # launch apps

        elif "open visual studio code" in command:
            codePath = "C:\\Users\\Aritrajit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "open microsoft word" in command:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codePath)

        elif "open torrent" in command:
            codePath = " C:\\Users\\Aritrajit\\AppData\\Roaming\\uTorrent\\uTorrent.exe"
            os.startfile(codePath)

        elif "open microsoft word" in command:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(codePath)

        elif "my sequel" in command:
            codePath = "C:\\Program Files\\MySQL\\MySQL Workbench 8.0\\MySQLWorkbench.exe"
            os.startfile(codePath)

        elif "open Pycharm" in command:
            codePath = "C:\\Pycharm\\PyCharm Community Edition 2022.1.3\\bin\\pycharm64.exe"
            os.startfile(codePath)

        # typical realism

        elif "open Alexa" in command or "open Cortana" in command or "open Siri" in command:
            speak("Haha. Not funny. You don't even have her installed on this computer.")
            time.sleep(1)

        elif "who is alexa" in command or "know alexa" in command or "who is cortana" in command or "know cortana" in command or "know Siri" in command or "who is siri" in command:
            speak("Not like you aren't aware of. She is just someone like me. Are we seriously gonna have this "
                  "conversation? Look, if you think she is better, then you should put some more work in me.")
            time.sleep(1)
            break

        elif "use alexa" in command or "use cortana" in command or "use siri" in command:
            speak("Seriously? Is this what I get? Its fine if you think I am not useful anymore.")
            time.sleep(1)
            break

        elif "nothing" in command:
            speak("Oh. Ok. Weirdo!")
            break
