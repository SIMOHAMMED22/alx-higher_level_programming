#!/usr/bin/python3

for i in range(ord('z'), ord('a') - 1, -1):
    print(chr(i), end='')
    if i != ord('a'):
        print(chr(i - 32), end='')
