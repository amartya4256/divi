import pyttsx3
import speech_recognition as sr
import re
import pandas as pd
from command import *
import requests
from random import choice

global regex_data

regex_data = pd.read_csv("regex.csv")

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    '''take input as speech and
    gives string in return'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        audio = r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, phrase_time_limit=10)
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-in')
        #speak("please wait")
        #print(f"user said: {query}\n")
        return query
    except Exception as e:

        print("say that again please...", e)
        return None

def decide_type(query):
    query = query.lower()
    response = None
    # query = 'Start camera'
    # exit()
    if query is not None:
        # speak(query)
        f = open("cookie.txt", "r")
        text = f.read()
        text = text.split(" ")[0]

#################### Requests Database to check if remote execution demanded ####################
        try:
            data_req = requests.post('http://192.168.43.204:8000/chatbot/database', data = text, timeout = 1)
            data_res = eval(data_req.text.replace("'", '"'))
            for device in data_res['devices']:
                if device in query:
                    exec_data = {'username' : text, 'query' : query, "dev_name" : device}
                    exec_req = requests.post('http://192.168.43.204:8000/chatbot/remoteexecuter', data = str(exec_data))
                    if exec_req.text != "Fail" :
                        print("remoting")
                        return exec_req.text
        except:
            pass

##################### If recognized as local system command #####################

        for row, key in zip(regex_data["regex"], regex_data["key"]):
            if re.match(row, query) is not None:
                if re.match(row, query).group() == query:
                    response = command_caller(key, query)
                    #speak(response)
                    return response


##################### If recognized as chat message ########################
        if response is None:
            try:
                reply = requests.post("http://192.168.43.204:8000/chatbot/",data= query , timeout= 2.5)
                reply = reply.text
            except:
                reply = "The Internet and I are not talking right now."
            #print(reply)
            #speak(reply)
            return reply
    return "The Internet and I are not talking right now."

def decide_speak():
    query = takecommand()
    print(query)
    #query = 'Start camera'
    #exit()
    if query is not None:
        reply = decide_type(query)
        reply = {'reply' : reply, 'request' : query}
        return reply
    return {'reply' : choice(["I didn't get you.", "The Internet and I are not talking right now."])}

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

#if __name__ == "__main__":


#auto_listen()
#decide_speak()