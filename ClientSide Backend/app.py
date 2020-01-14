import json
from decider import *
from flask import Flask, request
from flask_cors import CORS
from os import startfile


app = Flask(__name__)
CORS(app)




@app.route('/speak',methods=['POST'])
def speakin():
    response = decide_speak()
    print(response)
    return response

@app.route('/type',methods=['POST'])
def typein():
    query= request.data
    query = query.decode('utf-8')
    print(query)
    response = decide_type(query)
    print(response)
    return response

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


if __name__ == '__main__':
    app.run()
