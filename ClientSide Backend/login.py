import requests

def login_req(some_fun):
    def doer(*args, **kwargs):
        f = open("cookie.txt", "r")
        cookie = f.read()
        if cookie!= '':
            return some_fun(*args, **kwargs)
        else:
            return "You need to login first."

    return doer