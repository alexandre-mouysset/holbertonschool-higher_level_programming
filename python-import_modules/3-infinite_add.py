#!/usr/bin/python3
import sys
if __name__ == "__main__":
    result = 0

    for count in range(1, len(sys.argv)):
        result = result + int(sys.argv[count])
    print("{}".format(result))
