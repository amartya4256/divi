from decider import *
from flask_cors import CORS
from flask import Flask,request
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
        print(a)
        return a
    return "Success"

@app.route('/login')
def login():
    data = requests.data
    pass









if __name__ == '_main_':
    app.run()