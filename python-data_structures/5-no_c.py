#!/usr/bin/python3
def no_c(my_string):
    my_string_clone = ""
    for i in my_string:
        if i == "c" or i == "C":
            continue
        my_string_clone = my_string_clone + i
    return (my_string_clone)
