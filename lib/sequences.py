#!/usr/bin/env python3

def print_fibonacci(length):
    x = 0
    y = 1
    z = []
    for i in range(length):
        z.append(x)
        x, y = y, x + y
    
    print(z)
    