#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            offset = ord('A') - ord('a')
            print("{}".format(chr(ord(char) + offset)), end="")
        else:
            print("{}".format(char), end="")
