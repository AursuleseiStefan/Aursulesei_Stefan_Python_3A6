#Write a function that, for a text given as a parameter, 
# censures words that begin and end with vowels. 
# Censorship means replacing characters from odd positions with *.

import re

def ex6(text):
    x = []
    for word in text.split():
        x.append(re.sub("^[aeiou]\w*[aeiou]","*",word))
    return x
    

if __name__=="__main__":
    print(ex6("ana are mere"))