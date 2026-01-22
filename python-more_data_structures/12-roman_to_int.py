#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0

    Roman_Number = {"I": 1, "V": 5, "X": 10, "L": 50,
                    "C": 100, "D": 500, "M": 1000}
    Final_Number = 0

    lenght = len(roman_string)

    for i in range(lenght):
        value = Roman_Number[roman_string[i]]

    if i + 1 < lenght and value < Roman_Number[roman_string[i + 1]]:
        Final_Number -= value
    else:
        Final_Number += value

    return Final_Number
