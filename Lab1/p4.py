def transformString(s):
    s = s.replace(s[0], s[0].lower(), 1)
    for i in range(1, len(s)):
        if 'A' <= s[i] <= 'Z':
            s = s.replace(s[i], s[i].lower(), 1)
            s = s[:i] + '_' + s[i:]
    if 'A' <= s[-1] <= 'Z':
        s = s.replace(s[-1], s[-1].lower(), 1)
        s = s[:-1] + '_' + s[-1]

    return s


if __name__ == '__main__':
    string = input("stringul: ")
    print(transformString(string))
