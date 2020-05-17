import pyttsx3, csv
import speech_recognition as sr
import re
import pandas as pd
from command import *


global regex_data

regex_data = pd.read_csv("regex.csv")

#from nmtchatbot.modded_inference import *








def takecommand():
    '''take input as speech and
    gives string in return'''
    r = sr.Recognizer()                             #Take input from user
    with sr.Microphone() as source:                 #and converts into string
        print("listening.....")
        audio = r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=10)
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:

        print("say that again please...")
        return None
    #query = "open spotify"
    return query

def decide():
    #query = takecommand()
    query = input("Bol bro! :")

    if query is not None:
        query = query.lower()

##########################################################################################################################################
                                            #Decider checks for the type of command in regex
##########################################################################################################################################
        response  = None

        for row, key in zip(regex_data["regex"],regex_data["key"]):
            if re.match(row, query) is not None:
                if re.match(row, query).group() == query:
                    response = command_caller(key, query)
                    print(response)
                    #if len(response)==2:

                        #################################Prompt to choose window###############################################
                        ################################mul_dic_match(response[1])#############################################
                    break
        if response is None:

            reply = ""
            return reply

if __name__ == "__main__":
    while True:
        if(input("Speak?")=="Y"):
            pos = decide()
        else:
            exit()











