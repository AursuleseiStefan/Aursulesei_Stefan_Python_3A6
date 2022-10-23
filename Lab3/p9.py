def poz(*arg,**key):
    c = 0
    for i in arg:
        if i in key.values():
            c += 1
    return c


if __name__ == '__main__':
    print(poz(1, 2, 3, 4, x=1, y=2, z=3, w=5))