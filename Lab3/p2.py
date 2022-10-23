def nrcaract(string):
    dicti = {}
    dicti = {caracter:string.count(caracter) for caracter in string}#pt caract in string,numara caract(google dictionary comprehention)
    for i in string:
        dicti[i] = string.count(i)
    return dicti

if __name__ == '__main__':
    string='Ana has apples.'
    print(nrcaract(string))
