#!/usr/bin/python3
def uppercase(str):
    total = ""
    for i in str:
        if 97 <= ord(str) <= 122:
            total = total + chr(ord(str) - 32)
        else:
            total = total + str
    print("{}".format(total))
