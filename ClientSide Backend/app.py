import json

from decider import *
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

global login_res

# f = open("cookie.txt", "w+")
# user_data = f.read()
# if user_data!='':
#     cookie = user_data.split(" ")[0]
#     res = requests.post("http://192.168.43.204:8000/login_check/", data=cookie)
#     login_res = res.text
#     if login_res != cookie.split(" ")[1]:
#         f.write("")
# f.close()

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
    res = requests.post("http://192.168.43.204:8000/chatbot/login", data=data)
    res = json.loads(str(res.text))
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
    return "yo"

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



if __name__ == '_main_':
    app.run()