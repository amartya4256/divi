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










if __name__ == '_main_':
    app.run()