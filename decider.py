import pyttsx3, csv
import speech_recognition as sr
import datetime
import re
import webbrowser
import subprocess
import pandas as pd



global regex_data, read_data
regex_data = open("regex.csv", newline = '')
read_data = csv.reader(regex_data, delimiter = ' ')
engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
def speak(audio):
    engine.say(audio)                               #Speaks for the AI
    engine.runAndWait()

def takecommand():
    '''take input as speech and
    gives string in return'''
    r = sr.Recognizer()                             #Take input from user
    with sr.Microphone() as source:                 #and converts into string
        speak("speak what you want")
        print("listening.....")
        audio = r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=10)
        with open("audio.wav", "wb") as f:
            f.write(audio.get_wav_data())
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-in')
        speak("please wait")
        print(f"user said: {query}\n")

    except Exception as e:

        print("say that again please...")
        return None
    #query = "open spotify"
    return query

def decide():
    query = takecommand()
    if query is not None:
        query = query.lower()
        speak(query)
##########################################################################################################################################
                                            #Decider checks for the type of command in regex
##########################################################################################################################################
        counter  = 0
        pos = 0
        for row in regex_data:
            #print(row[:-2], "oh lalala", query)
            if re.match(row[:-2], query) is not None:
                if re.match(row[:-2], query).group() == query:
                    print(pos)
                    exit()
            pos+=1
        print("Starting chatbot...")
        speak("Starting chatbot...")

if __name__ == "__main__":
    decide()











