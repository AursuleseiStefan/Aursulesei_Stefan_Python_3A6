import re

def ex1(text):
    variabila=re.findall("\w+",text)
    return variabila

if __name__=="__main__":
 print(ex1("asdfghjkjasdfghjksdfghjkl "))