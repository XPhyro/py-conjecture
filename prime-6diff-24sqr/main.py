#!/usr/bin/env python3


import math
import input_helper as ih
import num_helper as nh


p = ih.get_int_lambda("Enter a prime number.", lm=nh.is_prime)

if not p + 1 % 6:
    k = (p - 1) / 6
else:
    k = (p + 1) / 6

k = math.trunc(k)
m = math.trunc(((p * p) - 1) / 24)

print(f"k = {k}\nm = {m}")
