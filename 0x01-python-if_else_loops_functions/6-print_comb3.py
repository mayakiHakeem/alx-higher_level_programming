#!/usr/bin/python3
for i in range(10):
    for j in range(1, 10):
        if i < j and (i != 8 and j != 9):
            print("{}{},".format(i, j), end=' ')
print("{}{}".format(i - 1, j))
