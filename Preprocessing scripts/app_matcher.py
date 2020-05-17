import os
import fnmatch
from fuzzywuzzy import fuzz

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
        return list(res_dic.keys()), res_dic


def app_match(inp_array):
    #global checklist
    checklist = dict()
    for root, dir, files in os.walk("C:\\ProgramData\\Microsoft\\Windows\\Start Menu"):
        #print(root)
        # print ("")
        for items in fnmatch.filter(files, "*"):
            #print(root + r'\\' + items)
            path = root + r'\\' + items
            if "uninstall" not in items.lower()[:-4] and fuzz.token_set_ratio(items.lower()[:-4],inp_array)>50:
                checklist[items[:-4]] = path
    if len(checklist.keys())==1:
        try:
            os.startfile(checklist[list(checklist.keys())[0]])
            return ("starting " + list(checklist.keys())[0])
        except:
            #print("Couldn't Start", list(checklist.keys())[0])
            return "Couldn't Start " + list(checklist.keys())[0]

    else:
        #print(list(checklist.keys()), checklist)
        return list(checklist.keys()), checklist
        #os.startfile(path)


#app_match('start xenovrse')




