# pip install SpeechRecognition
# pip install pyttsx3 - text to speech
# # pip install PyAudio
# pip install pywhatkit - searching
# pip install wikipedia
# pip install pyjokes

import pywhatkit

import speech_recognition as sr

import pyttsx3

import datetime

import wikipedia

import pyjokes

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
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if 'alexa' or 'soumil' or 'somil' in command:
                if 'alexa' in command:
                    command = command.replace('alexa', '')
                if 'soumil' in command:
                    command = command.replace('soumil', '')
                if 'somil' in command:
                    command = command.replace('somil', '')
    except:
        pass
    return command

def run_alexa():
    command = take_command()

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk('Current time is ' + time)
    elif 'who' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say it again.')
while(True):
    run_alexa()



