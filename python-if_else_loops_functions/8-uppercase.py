#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            transform = ord(c) - 32
        else:
            transform = ord(c)
        print("{}".format(chr(transform)), end="")
    print("")
