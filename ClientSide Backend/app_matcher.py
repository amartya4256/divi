import os
import fnmatch
from fuzzywuzzy import fuzz
import requests

def mul_dic_match(ref_dic,query):
    res_dic = dict()
    ref_list = list(ref_dic.keys())
    for keys in ref_list:
        if fuzz.token_set_ratio(keys,query)>50:
            res_dic[keys] = ref_dic[keys]
    if len(res_dic)==1:
        try:
            os.startfile(res_dic[list(res_dic.keys())[0]])
            return ("starting " + list(res_dic.keys())[0])
        except:
            return "Couldn't Start " + list(res_dic.keys())[0]
    else:
        return res_dic


def app_match(inp_array):
    #global checklist
    val = dict()
    checklist = dict()
    walk_list = ["C:\\ProgramData\\Microsoft\\Windows\\Start Menu", "C:\\Users\\" + os.getlogin() + "\\AppData\\Roaming\\Microsoft"]
    for paths in walk_list:
        for root, dir, files in os.walk(paths):
            #print(root)
            # print ("")
            for items in fnmatch.filter(files, "*"):
                #print(root + r'\\' + items)
                path = root + r'\\' + items
                if "uninstall" not in items.lower()[:-4] and fuzz.token_set_ratio(items.lower()[:-4],inp_array)>60:
                    val[items[:-4]] = fuzz.token_set_ratio(items.lower()[:-4],inp_array)
                    checklist[items[:-4]] = path

############################ Search Optimization ##########################

    main_checklist = dict()
    for key in val.keys():
        if val[key] == 100:
            main_checklist[key] = checklist[key]
    if len(main_checklist) > 0:
        checklist = main_checklist

############################ File execution decision #########################

    if len(checklist.keys())==1:
        try:
            os.startfile(checklist[list(checklist.keys())[0]])
            return ("starting " + list(checklist.keys())[0])
        except:
            #print("Couldn't Start", list(checklist.keys())[0])
            return "Couldn't Start " + list(checklist.keys())[0]

    else:
        print("yaha aa gaye hum")
        #print(list(checklist.keys()), checklist)
        if checklist == {}:
            try:
                checklist = requests.post("http://192.168.43.204:8000/chatbot/",data= " ".join(inp_array) , timeout= 2.5).text
            except:
                checklist = "I and Internet are not talking right now."
        else:
            checklist['parsable'] = '1'
            for each in checklist.keys():
                checklist[each] = checklist[each].replace('\\', "$")
            print(checklist)
        return checklist
        #os.startfile(path)


#app_match('start xenovrse')




