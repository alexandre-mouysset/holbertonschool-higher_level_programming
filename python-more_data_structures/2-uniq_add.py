#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_number = []
    for i in range(len(my_list)):
        if my_list[i] not in sum_number:
            sum_number.append(my_list[i])
    total = sum(sum_number)
    return total
