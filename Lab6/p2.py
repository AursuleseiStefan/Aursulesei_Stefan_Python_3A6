#Write a function that receives as a parameter 
# a regex string, a text string and a whole number x,
# and returns those long-length x substrings that match
# the regular expression.

import re

def ex2(regex,text,x):
    lista=re.findall(regex,text)
    lista2=list()
    for el in lista:
        if len(el)==x:
            lista2.append(el)
    return lista2

print(ex2("\w+","abc abcd abcde bcd ",3))