import webbrowser
import subprocess
from app_matcher import app_match,mul_dic_match


'''C:\ProgramData\Microsoft\Windows\Start Menu\Programs'''


global cmd_reff



def camera():
    subprocess.run('start microsoft.windows.camera:', shell=True)
    return "Starting Camera"


def mail():
    pass


def browser():
    webbrowser.open('google.com')
    return "Starting Browser"


def music():
    subprocess.run('start microsoft.windows.groove:', shell=True)
    return "Playing Music"

def googleSearch(query):
    query = query.replace("google", "", 1)
    query = query.replace("search", "", 1)
    webbrowser.open("https://google.com/search?q=" + query)

######################### Executes command on the basis of regex matched ###########################

def command_caller(pos,query):
    print(pos)
    if pos == 'start_app':
        executed = cmd_reff[str(pos)](query)
        return executed
    elif pos == 'search' :
        cmd_reff[str(pos)](query)
        return "I found this on the web."
    else:
        executed = cmd_reff[str(pos)]()
        return executed

cmd_reff = {'picture':camera , 'mail':mail , 'brows er':browser , 'music':music, 'start_app':app_match, 'search' : googleSearch}

