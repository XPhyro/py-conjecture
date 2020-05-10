#!/usr/bin/env python3


from time import time
from math import trunc


def is_catalan(x):
    m = (x - 1) ** (1 / 2)
    if m != trunc(m):
        return False

    m = (x + 1) ** (1 / 3)
    if m != trunc(m):
        return False

    return True


print("Be careful while computing up to high numbers, as this can use too much memory.")

maxX = int(input("Enter max x: "))
l = []

t0 = time()

for i in range(1, maxX + 1):
    l.append((i, is_catalan(i)))

t1 = time()

with open("catalans", "w+") as f:
    f.write(f"Time:\t{t1 - t0}\n")
    f.write(f"Catalans:\t{str(l)}")
