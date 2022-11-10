#Write a function that receives as a parameter a string of
# text characters and a list of regular expressions and 
# returns a list of strings that match on at least one 
# regular expression given as a parameter.

import re

def ex3(text,listaRegex):
    rezultat=[]
    for regex in listaRegex:
        match_uri=re.findall(regex,text)
        if match_uri:
            rezultat.extend(match_uri)
    rezultat=list(set(rezultat))
    rezultat.sort()
    return rezultat
print(ex3("ana 54 are 324 mere",["\w+","\d+"]))#d-digits s-spatiu