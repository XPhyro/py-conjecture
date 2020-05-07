#!/usr/bin/env python3


def get_collatz(n, m=0, l=[]):
    if n == 1:
        return m, l

    m += 1

    if n % 2 == 0:
        k = n / 2
        l.append(k)
        return get_collatz(k, m, l)
    else:
        k = 3 * n + 1
        l.append(k)
        return get_collatz(k, m, l)


N = input("Enter n: ")
m, l = get_collatz(int(N))
l = [int(i) for i in l]

print((m, l))
