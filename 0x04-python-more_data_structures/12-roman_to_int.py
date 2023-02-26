#!/usr/bin/python3

def roman_to_int(roman_string):
    """converts a roman numeral to an integer"""

    intValue = 0

    dic = {}
    dic['I'] = 1
    dic['V'] = 5
    dic['X'] = 10
    dic['L'] = 50
    dic['C'] = 100
    dic['D'] = 500
    dic['M'] = 1000

    if not str or type(roman_string) != str:
        return 0

    else:
        for i in range(len(roman_string)):
            if i + 1 > len(roman_string):  # if there's a next character
                if dic[roman_string[i]] < dic[roman_string[i + 1]]:
                    intValue -= dic[roman_string[i]]
            else:
                intValue += dic[roman_string[i]]

        return intValue
