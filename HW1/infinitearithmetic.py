"""
Without recursion
"""

import os
import sys
from typing import Dict

from bigint import BigInt


def main():
    if len(sys.argv) < 2:
        sys.stderr.write('No arguments specified\n')
        sys.stderr.write('Exiting with code (1)\n')
        sys.exit(1)

    args_str = sys.argv[1]
    args = __parse_args(args_str)
    input_path = args.get('input', None)
    digits = args.get('digitsPerNode', None)

    if input_path == None:
        sys.stderr.write('Mixing arg \'input\' from argv\n')
        sys.stderr.write('Exiting with code (2)\n')
        sys.exit(2)

    if digits == None:
        sys.stderr.write('Mixing arg \'digitsPerNode\' from argv\n')
        sys.stderr.write('Exiting with code (3)\n')
        sys.exit(3)

    status = run_infinitearithmetic(input_path, digits)
    sys.exit(status)


def run_infinitearithmetic(input_path, digits_per_node):
    inputfile = open(input_path)
    lines = [line.strip() for line in inputfile]

    for line in lines:
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

    return 0


def __parse_args(string: str) -> Dict[str, str]:
    args = [s.strip() for s in string.split(';')]
    kv_pairs = [a.split('=') for a in args]
    return dict(kv_pairs)


if __name__ == '__main__':
    main()
