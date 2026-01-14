#!/usr/bin/python3
for alphabet in range(97, 123):
    if alphabet not in (101, 113):
        print("{}".format(chr(alphabet)), end="")
