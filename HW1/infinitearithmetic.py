"""
Without recursion
"""

import os
from BigInt import BigInt


def infinitearithmetic():
    path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(path) as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if '*' in line:
            values = line.split('*')
            x = BigInt(values[0])
            y = BigInt(values[1])
            x.multiply(y)
            print(line.rstrip('\n') + '=' + str(x))

        elif '+' in line:
            values = line.split('+')
            x = BigInt(values[0])
            y = BigInt(values[1])
            x.add(y)
            print(line.rstrip('\n') + '=' + str(x))


infinitearithmetic()
