#!/usr/bin/python3

def uppercase(str):
    result = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            upper_char = chr(ord(char) - ord('a') + ord('A'))
            result += "{}".format(upper_char)
        else:
            result += "{}".format(char)
    print(result)
