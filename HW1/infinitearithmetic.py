"""
Without recursion
"""

import os
from BigInt import BigInt


def main():
    path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(path) as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if '*' in line:
            values = line.split('*')
            x = BigInt.parse(values[0])
            y = BigInt.parse(values[1])
            result = x * y
            print(line.rstrip('\n') + '=' + str(result))

        elif '+' in line:
            values = line.split('+')
            x = BigInt.parse(values[0])
            y = BigInt.parse(values[1])
            result = x + y
            print(line.rstrip('\n') + '=' + str(result))

if __name__ == '__main__':
    main()
