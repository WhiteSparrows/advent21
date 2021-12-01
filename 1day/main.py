#!/usr/bin/env python3
import os

filename = __file__[0:-7] + "/data1.txt"

#Main loop
with open(filename, "r") as f:
    data = f.read()
    measurements = data.splitlines()

measurements = list(map(int, measurements))
d = sum((measurements[i] > measurements[i-1]) for i in range(1, len(measurements)))
print("first result is : ", d)

a = sum(1 for i in range(1, len(measurements))if sum(measurements[i : i + 3]) > sum(measurements[i - 1 : i + 2]))
print("second result is : ", a)