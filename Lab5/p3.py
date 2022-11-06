def f1(s):
    vowels = []
    for letter in s:
        if letter.lower() in ['a','e','i','o','u']:
            vowels.append(letter)
    return vowels

if __name__=="__main__":

    print(f1("Programming in Python is fun"))

    l2=[letter for letter in "Programming in Python is fun" if letter.lower() in ['a','e','i','o','u']]
    print(l2)

    l3=list(filter(lambda letter: letter.lower() in ['a','e','i','o','u'],"Programming in Python is fun" ))
    print(l3)