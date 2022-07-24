
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'natasha' in command:
                command = command.replace('natasha', '')
                print(command)
    except:
        pass
    return command


def run_natasha():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is?' in command:
        person = command.replace('who is?', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('haha, I am not answering that')
        
        
    elif 'are you taken' in command:
        talk('haha yes, by milions')
        
        
    
    
    elif 'open visual studio code' in command:
        path = "C:\\Users\\Aritrajit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path)
        
        
        
        
        
    elif 'open pycharm' in command:
        path = "C:\\Pycharm\\PyCharm Community Edition 2022.1.3\bin\\pycharm64.exe"
        os.startfile(path)
        
        
        
        
    elif 'open my sequel' in command:
        path = "C:\\Program Files\\MySQL\\MySQL Workbench 8.0\\MySQLWorkbench.exe"
        os.startfile(path)    
        
    
        
        
    elif 'play music' in command:
        music_dir = 'C:\\Users\\Aritrajit\\Desktop\\My projects\\Music App\\songs'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
        
        
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        
    else:
        talk('I did not get that, could you please repeat?')


while True:
    run_natasha()

   
