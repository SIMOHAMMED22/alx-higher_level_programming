#!/usr/bin/python3

for num in range(100):
    if num < 10:
        print("0{:d}".format(num), end="")
    else:
        print("{:d}".format(num), end="")

    if num != 99:
        print(", ", end="")

print("")
