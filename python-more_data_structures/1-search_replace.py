#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for position in range(len(my_list)):
        if my_list[position] == search:
            new_list[position] = replace
    return new_list
