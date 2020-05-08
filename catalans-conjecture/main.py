#!/usr/bin/env python3


def get_catalan(x, y, max_a=51, max_b=51):
    for a in range(2, max_a + 1):
        for b in range(2, max_b + 1):
            m = x ** a - y ** b
            if m == 1:
                return a, b
    return None, None


max_x, max_y = int(input("Enter max x: ")), int(input("Enter max y: "))
max_a, max_b = int(input("Enter max a: ")), int(input("Enter max b: "))

l = []

for x in range(1, max_x + 1):
    for y in range(1, max_y + 1):
        l.append(((x, y), get_catalan(x, y, max_a, max_b)))

with open("catalans", "w+") as f:
    f.write("{\n")
    f.write(
        f"\t'max_x': {max_x}\n\t'max_y': {max_y}\n\t'max_a': {max_a}\n\t'max_b': {max_b}\n"
    )
    f.write(f"\t'((x, y), (a, b))': {str(l)}\n")
    f.write("}")
