#!/usr/bin/python3

for i in range(0, 10):
    for ii in range(i + 1, 10):
        if i == 8 and ii == 9:
            print("{}{}".format(i, ii))
        else:
            print("{}{},".format(i, ii), end=" ")
