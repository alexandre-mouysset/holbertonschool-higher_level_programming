#!/usr/bin/python3
def uppercase(str):
    total = ""
    for i in str:
        if 97 <= ord(i) <= 122:
            total = total + chr(ord(i) - 32)
        else:
            total = total + i
    print("{}".format(total))
