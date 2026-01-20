#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_clone = my_list.copy()
    if idx >= len(my_list) or idx < 0:
        return my_list_clone
    else:
        my_list_clone[idx] = element
        return my_list_clone
