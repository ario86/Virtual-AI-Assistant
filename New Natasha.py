import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say('natasha. at your service')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Speak now...')
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

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 4)
        print(info)
        talk(info)

    elif 'what is' in command:
        item = command.replace('what is', '')
        info = wikipedia.summary(item, 4)
        print(info)
        talk(info)


    elif 'date' in command:
        talk('I dont have that kind of time')

    elif 'are you single' in command:
        talk('As if you have a chance. hahaha')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('Repeat that.')


while True:
    run_natasha()