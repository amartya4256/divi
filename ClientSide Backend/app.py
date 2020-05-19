import json

import requests
from decider import *
from flask import Flask, request
from flask_cors import CORS
from flask_mail import Mail
from os import startfile

import sys

# sys.stdout = sys.stderr = open('log.txt', 'w+')

app = Flask(__name__)
CORS(app)

#app.config.from_pyfile('mailconfig.cfg')

######################## Endpoint to activate microphone to speak ######################

@app.route('/speak',methods=['POST'])
def speakin():
    response = decide_speak()
    print(response)
    return response

######################## Endpoint to take input through keyboard #######################

@app.route('/type',methods=['POST'])
def typein():
    query= request.data
    query = query.decode('utf-8')
    print(query)
    response = decide_type(query)
    print(response)
    return response


######### Checks the value set by user for autolisten and saves it #################
######### value is the value set by user, 1 is On, 0 is Off #################

@app.route('/autolisten/<value>', methods = ['GET', 'POST'])
def autolisten(value):
    if str(value) == "0":
        f = open("auto_listen_last_state.txt", "w+")
        f.write("0")
        f.close()
    elif str(value) == "1":
        f = open("auto_listen_last_state.txt", "w+")
        f.write("1")
        f.close()
    elif str(value) == "getdata":
        f = open("auto_listen_last_state.txt", "r")
        a = f.read()
        f.close()
        print(a)
        return a
    return "Success"

################### Takes login information, matches with the database, logins in or restricts according to result ##########################

@app.route('/login', methods = ['POST'])
def login():
    data = request.data
    try:
        res = requests.post("http://192.168.43.204:8000/chatbot/login", data=data)
        res = json.loads(str(res.text))
    except:
        res = {"response" : "Cannot Connect to Server"}
        return res['response']

    print(res)
    if res['response'] == "Yes":
        f = open("cookie.txt", "w")
        f.write(res['cookie'])
        f.close()
        print("done")
        return "Success"
    else:
        print("no")
        return "Check your credentials!"

############## Reads cookie file, if cookie found, logs in, else moves to login page #######################

@app.route('/logincheck', methods = ['GET'])
def login_check():
    f = open("cookie.txt", "r")
    text = f.read()
    text = text.split(" ")
    print(text)
    try:
        data = json.dumps({"username":text[0], "password":text[1]})
        res = requests.post("http://192.168.43.204:8000/chatbot/loginchecker", data=data).text
    except:
        res = "No"
    return res

@app.route('/logout', methods = ['GET'])
def logout():
    print("logout")
    f = open("cookie.txt", "w")
    f.write("")
    f.close()
    return "Logged out!"

############### Directly executes apps using multimatcher selector #####################

@app.route('/app_executer', methods = ['POST'])
def app_executer():
    data = request.data
    data = data.decode('utf-8')
    new_data = eval(data)
    print(new_data)
    path = new_data['path'].replace('$', '\\')
    try:
        startfile(path)
        return "Success"
    except:
        return "Fail"

@app.route('/get-devices', methods = ['GET'])
def getDevices():
    f = open("cookie.txt", "r")
    text = f.read()
    text = text.split(" ")
    print(text)
    try:
        data = json.dumps({"username": text[0]})
        res = requests.post("http://192.168.43.204:8000/chatbot/get-devices", data=data).text
    except:
        res = list()
    return res

@app.route('/addDevice', methods = ['POST'])
def addDevice():
    req_data = request.data
    req_data = req_data.decode('utf-8')
    data = eval(req_data)
    f = open("cookie.txt", "r")
    text = f.read()
    text = text.split(" ")
    try:
        data = json.dumps({"username": text[0], "deviceName" : data["name"], "deviceIp" : data["ip"]})
        res = requests.post("http://192.168.43.204:8000/chatbot/add-device", data=data).text
    except:
        res = {"success" : False, "message" : "Cannot register device."}
    return res

@app.route('/removeDevice', methods = ['POST'])
def removeDevice():
    data = eval(request.data.decode('utf-8'))
    f = open("cookie.txt", "r")
    text = f.read()
    text = text.split(" ")
    try:
        data = json.dumps({"username": text[0], "deviceName" : data["name"]})
        res = requests.post("http://192.168.43.204:8000/chatbot/remove-device", data=data).text
    except:
        res = {"success" : False, "message" : "Cannot remove device."}
    return res

@app.route("/forgot-password", methods = ["POST"])
def forgotpassword():
    query= request.data
    query = eval(query.decode('utf-8'))
    print(query)

    url = 'http://192.168.43.204:8000/chatbot/forgot-password'
    query = json.dumps({'field': query})
    try:
        res = requests.post(url, data=query).text
        print(res)
    except:
        res = {"message" : "Cannot connect to server."}
    return res

@app.route("/signup", methods = ["POST"])
def signup():
    query = request.data
    query = eval(query.decode('utf-8'))
    print(query)

    url = 'http://192.168.43.204:8000/chatbot/sign-up'
    query = json.dumps(query)
    try:
        res = requests.post(url, data=query).text
        print(res)
    except:
        res = {"message" : "Cannot connect to server."}
    return res



if __name__ == '__main__':
    app.run()
