def noOfOccurences(s1, s2):
    if len(s2) < len(s1):
        return 0
    elif len(s2) == len(s1):
        if s1 == s2:
            return 1
        else:
            return 0
    else:
        return s2.count(s1)


if __name__ == '__main__':
    s1 = input("Primul string: ")
    s2 = input("Al doilea string: ")
    appearances = noOfOccurences(s1, s2)
    print("nr de aparitii: ", appearances)
