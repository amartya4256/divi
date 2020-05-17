import os

dir_name = "project data"
for files in os.listdir(dir_name):
    print(files)
    call_parser = 'python chatbot.py ' + files
    print(call_parser)
    os.system(call_parser)