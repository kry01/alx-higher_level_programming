#!/usr/bin/python3
i = 32
for c in range(122, 96, -1):
    if i == 32:
        i = 0
    else:
        i = 32
    c = chr(c - i)
    print("{}".format(c), end='')
