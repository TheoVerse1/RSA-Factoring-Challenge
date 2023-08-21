#!/usr/bin/python3

import sys


def factorize(number):
    """Factorize a number into two smaller factors."""
    for i in range(2, number):
        if number % i == 0:
            return i, number // i
    return None, None


def main(filename):
    """Main function to read numbers from a file and factorize them."""
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        number = int(line.strip())
        p, q = factorize(number)
        if p and q:
            print(f"{number}={p}*{q}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)
