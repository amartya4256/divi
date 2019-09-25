import pyttsx3, csv
import speech_recognition as sr
import re
import pandas as pd
from command import *

global regex_data

regex_data = pd.read_csv("regex.csv")

from nmtchatbot.modded_inference import *

nmt_chatbot("First response")




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
    #query = "what is the color of the sky"

    if query is not None:
        query = query.lower()
        speak(query)

##########################################################################################################################################
                                            #Decider checks for the type of command in regex
##########################################################################################################################################
        response  = None

        for row, key in zip(regex_data["regex"],regex_data["key"]):
            if re.match(row, query) is not None:
                if re.match(row, query).group() == query:
                    response = command_caller(key)
                    print(response)
                    speak(response)
        if response is None:
            reply = nmt_chatbot(query)
            print(reply)
            speak(reply)

if __name__ == "__main__":
    while True:
        if(input("Speak?")=="Y"):
            pos = decide()
        else:
            exit()











