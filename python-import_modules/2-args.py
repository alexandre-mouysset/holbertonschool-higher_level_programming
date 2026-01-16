#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv) - 1

    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc))
    else:
        print("{} arguments:".format(argc))

    for arg_number in range(1, len(sys.argv)):
        print("{}: {}".format(arg_number, sys.argv[arg_number]))
