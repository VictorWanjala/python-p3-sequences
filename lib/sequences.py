#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = [0]
    if length>1:
        fibonacci.append(1)
    while len(fibonacci) < length:
        next_number = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_number)
    print(fibonacci)

print_fibonacci(9)

