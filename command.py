import webbrowser
import subprocess


'''C:\ProgramData\Microsoft\Windows\Start Menu\Programs'''
#def assistant(command):
 #   call out n where n = command

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

def command_caller(pos):
    executed = cmd_reff[str(pos)]()
    return executed

cmd_reff = {'picture':camera , 'mail':mail , 'browser':browser , 'music':music}

